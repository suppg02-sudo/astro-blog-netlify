---
pubDatetime: 2026-02-02T12:00:00Z
title: "LLM Observability with OpenTelemetry: A Practical Guide"
postSlug: "llm-observability-with-opentelemetry-practical-guide"
description: "LLM Observability with OpenTelemetry: A Practical Guide"
tags:
  - monitoring
  - ai
---

## The Black Box Problem

Large Language Models (LLMs) have quickly become the backbone of many modern applications — from chatbots to Retrieval-Augmented Generation (RAG) systems. But here's the challenge: these models often behave like **black boxes**.

Without observability, we're left guessing:
- Why did the model respond that way?
- Which prompt caused this hallucination?
- How much are we spending on tokens?
- What's the latency impact of retrieval vs generation?

This is where **OpenTelemetry (OTel)** steps in. By instrumenting our LLM applications, we can capture **traces, metrics, and logs** — turning the black box into a glass box.

## Core Observability Signals for LLMs

When instrumenting an LLM app, we focus on three pillars:

### 1. Request Traces

Traces help you follow a user query as it flows through your RAG pipeline — retrieval, prompt building, LLM generation. They provide visibility into **where time is spent** and **what inputs/outputs influenced the result**.

Key spans to create:
- **Retrieval** span (with metadata: source, number of documents, latency)
- **LLM inference** span (with metadata: model name, temperature, prompt, response length)

### 2. Metrics

Metrics provide **aggregated, time-series insights** into your system. While traces help debug individual requests and logs capture raw details, metrics allow you to **monitor trends** over time.

Essential metrics for LLM RAG pipelines:
- **Request Volume**: Counter of incoming user queries
- **Request Duration**: Histogram for latency distribution
- **Token Counters**: Number of tokens generated/consumed
- **Cost**: Gauge or counter for estimated token cost

### 3. Logs

Logs give you the **raw evidence** of what happened inside your LLM pipeline — including prompts, responses, and errors. Unlike traces (timing) and metrics (aggregates), logs capture **content and context**.

Structured JSON logs are best practice:
- Easy to parse with tools like Loki, Elasticsearch, or ETL pipelines
- Enables filtering and aggregation on fields (trace_id, span_id, user_id, etc.)
- Standardized format across services

{{< mermaid >}}
graph LR
    A[User Query] --> B[RAG Pipeline]
    B --> C[Traces]
    B --> D[Metrics]
    B --> E[Logs]
    C --> F[Debug Flow]
    D --> G[Monitor Trends]
    E --> H[Inspect Details]
    F --> I[Unified Dashboard]
    G --> I
    H --> I

    style A fill:#E1F5FE
    style I fill:#C8E6C9
    style C fill:#FFF9C4
    style D fill:#FFF9C4
    style E fill:#FFF9C4
{{< /mermaid >}}

## Tech Stack

For our comprehensive observability setup:

- **LLM runtime**: Ollama (local inference of Mistral)
- **Framework**: LangChain
- **Vector DB**: Chroma
- **Observability**: OpenTelemetry Python SDK
- **Backends**: Jaeger (traces), Prometheus (metrics), Loki (logs), Grafana (visualization)

## Architecture Overview

Our observability stack flows through the OpenTelemetry Collector to specialized backends:

{{< mermaid >}}
graph TD
    A[RAG Application] -->|OTLP| B[OpenTelemetry Collector]
    B --> C[Jaeger]
    B --> D[Prometheus]
    B --> E[Loki]
    C --> F[Grafana]
    D --> F
    E --> F

    style A fill:#E3F2FD
    style B fill:#FFF59D
    style C fill:#FFCCBC
    style D fill:#C5E1A5
    style E fill:#CE93D8
    style F fill:#81D4FA
{{< /mermaid >}}

## Instrumenting Traces

### Why Traces Matter

Traces are essential for:
- **Latency analysis**: Show whether slow responses are due to retrieval or LLM generation
- **Cost tracking**: Token counts let you estimate $ spend directly from traces
- **Debugging hallucinations**: Seeing prompts + responses helps identify if poor answers came from bad retrieval or bad generation
- **Model governance**: Attributes like model, temperature, top_p let you correlate behavior with configuration

### Python Implementation

Here's how to wire up OpenTelemetry traces for a RAG application:

```python
import time
import json

# --- OpenTelemetry Tracing ---
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Define resource attributes (metadata about the service)
resource = Resource.create({
    "service.name": "faq-rag",
    "service.version": "1.0.0",
    "app.environment": "dev",
    "app.owner": "observability-team",
    "telemetry.sdk.language": "python",
    "telemetry.sdk.name": "opentelemetry"
})

# --- Configure Tracing ---
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

# Configure OTLP exporter (sending traces to Jaeger/Collector)
otlp_trace_exporter = OTLPSpanExporter(endpoint="http://127.0.0.1:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_trace_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# --- LangChain + Ollama ---
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Initialize the Ollama model
model = OllamaLLM(
    model="mistral",
    temperature=0.7,
    top_p=0.9
)

# Define the prompt template
template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

# Build pipeline
chain = prompt | model

# --- Interactive Loop ---
while True:
    question = input("Ask your question (q to quit): ")

    if question.lower() == "q":
        break

    start_request = time.time()

    with tracer.start_as_current_span("rag-request") as span:
        span.set_attribute("rag.query", question)

        # --- Retrieval step ---
        with tracer.start_as_current_span("vector-retrieval") as retrieval_span:
            start_retrieval = time.time()
            reviews = retriever.invoke(question)
            retrieval_time = time.time() - start_retrieval
            retrieval_span.set_attribute("retriever.engine", "chroma")
            retrieval_span.set_attribute("retriever.search.k", 5)
            retrieval_span.set_attribute("retriever.latency.ms", retrieval_time * 1000)
            retrieval_span.set_attribute("retriever.documents.count", len(reviews))

            doc_previews = [
                (doc.page_content[:80] + "...") if len(doc.page_content) > 80 else doc.page_content
                for doc in reviews
            ]
            retrieval_span.set_attribute("retriever.documents.preview", json.dumps(doc_previews))

        # --- LLM Call ---
        formatted_prompt = prompt.format_prompt(
            reviews=reviews,
            question=question
        ).to_string()

        # --- LLM step ---
        with tracer.start_as_current_span("llm-call") as llm_span:
            llm_span.set_attribute("llm.provider", "ollama")
            llm_span.set_attribute("llm.model.name", "mistral")
            llm_span.set_attribute("llm.request.temperature", getattr(model, "temperature", None))
            llm_span.set_attribute("llm.request.top_p", getattr(model, "top_p", None))
            llm_span.set_attribute("llm.prompt.details", formatted_prompt)

            start_llm = time.time()

            result = chain.invoke({
                "reviews": reviews,
                "question": question
            })

            llm_latency = time.time() - start_llm
            tokens_in = len(formatted_prompt.split())
            tokens_out = len(str(result).split())
            cost_estimate = (tokens_in + tokens_out) * 0.000001  # fake cost

            # Response metadata
            llm_span.set_attribute("llm.response.details", str(result))
            llm_span.set_attribute("llm.response.tokens.input", tokens_in)
            llm_span.set_attribute("llm.response.tokens.output", tokens_out)
            llm_span.set_attribute("llm.response.tokens.total", tokens_in + tokens_out)
            llm_span.set_attribute("llm.response.cost.usd_estimate", cost_estimate)
            llm_span.set_attribute("llm.latency.ms", llm_latency * 1000)

        span.set_attribute("rag.answer.preview", str(result)[:120])

    print(f"\n{result}")
    print(80 * "-")
```

## Correlating Logs and Traces

### Why Correlation Matters

Connecting logs with traces enables:
- **From a trace in Jaeger**: Jump to corresponding logs in Loki by filtering on `trace_id`
- **From a log line**: Pivot back to full trace to see request lifecycle
- **Bridge high-cardinality events** (logs) with **low-cardinality context** (traces)

### JSON Logging Implementation

Instead of plain text logs, use structured JSON logs:

```python
# --- OpenTelemetry Logging ---
import logging
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter

# Setup logger provider
logger_provider = LoggerProvider(resource=resource)
log_exporter = OTLPLogExporter(endpoint="http://127.0.0.1:4317", insecure=True)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(log_exporter))

# Custom JSON Formatter
class JSONFormatter(logging.Formatter):
    def format(self, record):
        span = trace.get_current_span()
        span_context = span.get_span_context()
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "severity": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "trace_id": span_context.trace_id if span_context.is_valid else None,
            "span_id": span_context.span_id if span_context.is_valid else None
        }

        # Add extra attributes if available
        if hasattr(record, "args") and isinstance(record.args, dict):
            log_record.update(record.args)
        if hasattr(record, "extra") and isinstance(record.extra, dict):
            log_record.update(record.extra)

        return json.dumps(log_record)

# Attach JSON formatter to OTel handler
otel_handler = LoggingHandler(level=logging.INFO, logger_provider=logger_provider)
otel_handler.setFormatter(JSONFormatter())

logging.basicConfig(level=logging.INFO, handlers=[otel_handler])
logger = logging.getLogger("faq-rag")
```

Now you can emit structured logs that are automatically correlated with traces:

```python
logger.info("Received user query", extra={"query": question})

logger.info("Retrieved documents", extra={
    "query": question,
    "retriever.latency_ms": retrieval_time * 1000,
    "retriever.documents.count": len(reviews),
})

logger.info("LLM response generated", extra={
    "latency_ms": llm_latency * 1000,
    "tokens_in": tokens_in,
    "tokens_out": tokens_out,
    "cost_estimate": cost_estimate,
    "answer_preview": str(result)[:120]
})
```

## Collecting Metrics

### Why Metrics Matter

For LLM RAG pipelines, key metrics provide insights into:
- **Request Volume**: Traffic spikes, drops, or usage trends
- **Request Duration**: SLO/SLI monitoring and user experience
- **Token Usage**: Efficiency of prompts and cost correlation
- **Cost Estimation**: FinOps and controlling LLM usage bills

### Metrics Implementation

```python
# --- OpenTelemetry Metrics ---
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

# --- Configure Metrics ---
metric_exporter = OTLPMetricExporter(endpoint="http://127.0.0.1:4317", insecure=True)
reader = PeriodicExportingMetricReader(metric_exporter, export_interval_millis=5000)

provider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(provider)
meter = metrics.get_meter(__name__)

# Define custom metrics
request_counter = meter.create_counter(
    "rag_requests_total",
    unit="1",
    description="Total number of RAG requests"
)

request_duration_hist = meter.create_histogram(
    "rag_request_duration_ms",
    unit="ms",
    description="Duration of RAG requests in milliseconds"
)

token_input_counter = meter.create_counter(
    "rag_tokens_input_total",
    unit="tokens",
    description="Total input tokens sent to LLM"
)

token_output_counter = meter.create_counter(
    "rag_tokens_output_total",
    unit="tokens",
    description="Total output tokens generated by LLM"
)

token_total_counter = meter.create_counter(
    "rag_tokens_total",
    unit="tokens",
    description="Total tokens (input + output)"
)

cost_counter = meter.create_counter(
    "rag_cost_usd_total",
    unit="usd",
    description="Estimated total cost of LLM requests"
)
```

Emitting metrics in your RAG loop:

```python
# --- Emit Metrics ---
request_counter.add(1, {"rag.model": "mistral"})
request_duration_hist.record((time.time() - start_request) * 1000, {"rag.model": "mistral"})
token_input_counter.add(tokens_in, {"rag.model": "mistral"})
token_output_counter.add(tokens_out, {"rag.model": "mistral"})
token_total_counter.add(tokens_in + tokens_out, {"rag.model": "mistral"})
cost_counter.add(cost_estimate, {"rag.model": "mistral"})
```

## Complete Docker Compose Stack

Here's the complete observability stack with all components:

```yaml
services:

  otel-collector:
    container_name: otel-collector
    hostname: otel-collector
    image: otel/opentelemetry-collector-contrib:latest
    restart: always
    command: ["--config=/etc/otel-collector-config.yaml"]
    volumes:
      - ./config/otel-collector/otel-collector-config.yaml:/etc/otel-collector-config.yaml
    networks:
      - llm-obs-lab
    ports:
      - "4317:4317" # OTLP gRPC receiver
      - "4318:4318"

  jaeger:
    container_name: jaeger
    hostname: jaeger
    image: jaegertracing/all-in-one:latest
    restart: always
    volumes:
      - jaegar_data:/var/lib/jaeger
    networks:
      - llm-obs-lab
    ports:
      - "6831:6831/udp" # UDP port for Jaeger agent
      - "16686:16686" # Web UI
      - "14268:14268" # HTTP port for spans

  prometheus:
    container_name: prometheus
    hostname: prometheus
    image: prom/prometheus:latest
    restart: always
    command:
      - --storage.tsdb.retention.time=1d
      - --config.file=/etc/prometheus/prometheus.yml
    volumes:
      - prometheus_data:/prometheus
      - ./config/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
    networks:
      - llm-obs-lab
    ports:
      - "9090:9090"

grafana:
    container_name: grafana
    hostname: grafana
    image: grafana/grafana
    restart: always
    volumes:
      - grafana_data:/var/lib/grafana
      - "./config/grafana/datasources:/etc/grafana/provisioning/datasources"
    networks:
      - llm-obs-lab
    ports:
      - "3000:3000"

  loki:
    container_name: loki
    hostname: loki
    image: grafana/loki:latest
    restart: always
    command:
      - -config.file=/etc/loki/local-config.yaml
    volumes:
      - loki_data:/loki
      - "./config/loki/loki-config.yaml:/etc/loki/local-config.yaml"
    networks:
      - llm-obs-lab
    ports:
      - "3100:3100"

networks:
  llm-obs-lab:
    driver: bridge

volumes:
  loki_data: {}
  jaegar_data: {}
  grafana_data: {}
  prometheus_data: {}
```

## Configuration Files

### OTel Collector Configuration

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch: {}

extensions:
  health_check: {}

exporters:

  otlp/jaeger:
    endpoint: jaeger:4317
    tls:
      insecure: true

  prometheus:
    endpoint: "0.0.0.0:9090"

  otlphttp:
    endpoint: http://loki:3100/otlp

service:
  pipelines:

    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp/jaeger]

    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp]

    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [prometheus]
```

### Prometheus Configuration

```yaml
global:
  scrape_interval: 5s
scrape_configs:
  - job_name: 'otel-collector'
    static_configs:
      - targets: ['otel-collector:9090']
```

### Grafana Datasources

```yaml
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    url: http://prometheus:9090
    access: proxy
    basicAuth: false
    isDefault: true
    jsonData:
      tlsSkipVerify: true
    editable: false

  - name: Loki
    type: loki
    access: proxy
    url: http://loki:3100
    isDefault: false
    version: 1
    editable: false

  - name: Jaeger
    type: jaeger
    access: proxy
    url: http://jaeger:16686
    version: 1
    editable: false
```

## Bringing It All Together

### Start the Stack

```bash
docker-compose up -d
```

### Access Points

- **Jaeger UI** → http://localhost:16686/
- **Prometheus UI** → http://localhost:9090/
- **Grafana UI** → http://localhost:3000/ (user: `admin`, pass: `admin`)
- **Loki** → http://localhost:3100/

### Data Flow

Your **RAG app** exports telemetry via OTLP (`4317` gRPC, `4318` HTTP). **OTel Collector** ingests all telemetry, applies batching, and routes it:

- **Traces → Jaeger**
- **Metrics → Prometheus (scraped at `/metrics`)**
- **Logs → Loki**
- **Grafana** connects to all three for a unified view

{{< mermaid >}}
sequenceDiagram
    participant User as User
    participant RAG as RAG App
    participant OTEL as OTel Collector
    participant Jaeger as Jaeger
    participant Prom as Prometheus
    participant Loki as Loki
    participant Grafana as Grafana

    User->>RAG: Query
    RAG->>OTEL: Traces (OTLP)
    RAG->>OTEL: Metrics (OTLP)
    RAG->>OTEL: Logs (OTLP)
    OTEL->>Jaeger: Traces
    OTEL->>Prom: Metrics
    OTEL->>Loki: Logs
    Jaeger->>Grafana: Trace Data
    Prom->>Grafana: Metric Data
    Loki->>Grafana: Log Data
    Grafana->>User: Unified Dashboard
{{< /mermaid >}}

## Benefits of This Observability Setup

With this comprehensive observability stack, you now have **end-to-end observability for your RAG application**:

- **Debug request flow in Jaeger** - Trace every step from user query to final response
- **Track system health with Prometheus** - Monitor trends in request volume, latency, and costs
- **Investigate application logs in Loki** - Search and filter structured logs with full correlation
- **Combine all in Grafana dashboards** - Create unified views that span traces, metrics, and logs

### Key Insights You Can Gain

- **Latency analysis**: Traces show whether slow responses are due to retrieval or LLM generation
- **Cost tracking**: Token counts let you estimate $ spend directly from traces
- **Debugging hallucinations**: Seeing prompts + responses helps you identify if poor answers came from bad retrieval or bad generation
- **Model governance**: Attributes like `model`, `temperature`, `top_p` let you correlate behavior with configuration

## Conclusion

LLM observability is no longer optional — it's essential for production systems. OpenTelemetry provides a standardized, vendor-agnostic way to instrument your LLM applications and capture the telemetry you need to:

- Debug complex issues
- Optimize performance
- Control costs
- Ensure reliability

By implementing traces, metrics, and logs with OpenTelemetry and routing them to specialized backends like Jaeger, Prometheus, Loki, and Grafana, you transform your LLM from a mysterious black box into a transparent, observable system.

---

**References:**
- OpenTelemetry Documentation: https://opentelemetry.io/
- Jaeger Documentation: https://www.jaegertracing.io/
- Prometheus Documentation: https://prometheus.io/
- Loki Documentation: https://grafana.com/docs/loki/latest/
- Grafana Documentation: https://grafana.com/docs/