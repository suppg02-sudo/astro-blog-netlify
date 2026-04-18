---
pubDatetime: 2026-04-18T17:30:00Z
title: "When Your Sister Company Already Does ML: Overlap and Gaps Between SOC Machine Learning and the Karpathy Loop"
postSlug: "when-your-sister-company-alrea"
description: "When Your Sister Company Already Does ML: Overlap and Gaps Between SOC Machine Learning and the Karpathy Loop"
tags:
  - msp
series: karpathy-msp
---

Your MSP has a sister company running machine learning for SOC management. They process security events at scale, they understand anomaly detection, they have data pipelines, and they talk about false positive rates, precision, and recall as naturally as you talk about SLAs.

You might assume that because they do ML and the Karpathy Loop is an ML pattern, you can just hand the auto-improvement problem to the SOC team and let them extend what they already built.

That assumption is wrong. The overlap is real, but so are the gaps. Understanding both is the difference between leveraging a genuine advantage and building the wrong thing on top of existing infrastructure.

## The Overlap: What You Already Have

The SOC sister company gives your MSP something most organisations lack entirely: a culture that understands data-driven optimisation. That is not nothing.

| Shared Concept | SOC/ML Context | Karpathy Loop Context |
|---------------|---------------|----------------------|
| **Labelled data** | Security events classified as true positive / false positive | Tickets classified by correct category, priority, routing |
| **Eval metrics** | Precision, recall, F1, false positive rate | % correct routing, resolution time, alert noise ratio |
| **Threshold tuning** | Alert severity thresholds, correlation rules | Classification confidence thresholds, alert sensitivity |
| **Feedback loops** | Analyst feedback on false positives feeds model retraining | Technician re-categorisations feed rule updates |
| **Sandboxed testing** | Test SIEM environments, synthetic attack data | Test PSA instances, historical ticket replays |
| **Version control** | Model versioning, rule set versioning | Config versioning, rule set versioning |
| **Data pipelines** | Log ingestion → normalisation → enrichment → detection | Ticket ingestion → classification → routing → resolution |

If the SOC team has been doing this for even a year, they have something your MSP operations team does not: experience with iteration cycles, failed experiments, and the discipline of measuring before changing.

## The Gaps: What SOC ML Does Not Give You

Here is where the assumption breaks down. The skills, tools, and mental models that make someone good at SOC machine learning are not the same skills that make someone good at Karpathy Loop auto-improvement.

### Gap 1: Detection vs Optimisation

SOC ML is a **detection** problem. The model answers: "Is this event anomalous? Is it a threat? What severity?" The output is a classification. The metric is accuracy on known attack patterns.

The Karpathy Loop is an **optimisation** problem. The agent answers: "Which change improves the metric?" The output is a modified configuration. The metric is whether the system performs better after the change.

| Dimension | SOC/ML | Karpathy Loop |
|-----------|--------|---------------|
| Goal | Classify correctly | Improve system performance |
| Output | Label (threat / benign) | Modified config / rule / script |
| Feedback | Human analyst confirms or rejects label | Automated metric comparison before/after change |
| Success metric | Precision + recall on detection | Improvement in operational metric |
| Model type | Classification, anomaly detection | Search, optimisation, proposal-evaluation |
| Time horizon | Real-time (milliseconds) | Overnight (hours) |

A SOC data scientist who has spent two years building threat detection models does not automatically know how to design an optimisation loop that proposes, tests, and commits configuration changes.

### Gap 2: Model Training vs Loop Engineering

SOC ML trains a model on historical data, deploys it, and monitors drift. The model is static between retraining cycles. Retraining happens on a schedule — weekly, monthly, quarterly.

The Karpathy Loop does not train a model. It runs a search process. The agent proposes changes, tests them, and keeps or discards them. The system improves continuously, not in batch retraining cycles.

| Practice | SOC/ML | Karpathy Loop |
|----------|--------|---------------|
| How it improves | Retrain model on new labelled data | Agent proposes and tests changes continuously |
| Who proposes changes | Data scientists design features, tune hyperparameters | Agent proposes changes autonomously |
| How changes are validated | Holdout test set, cross-validation | Live experiment with metric comparison |
| Frequency | Batch (weekly/monthly) | Continuous (overnight, every night) |
| Failure mode | Model drift, concept drift | Metric gaming, overfitting to eval set |

The SOC team thinks in terms of model lifecycle: train, validate, deploy, monitor, retrain. The Karpathy Loop thinks in terms of search: propose, test, keep, repeat. These are different engineering disciplines.

### Gap 3: Different Skills Required

| Skill | SOC ML Engineer | Karpathy Loop Engineer |
|-------|----------------|----------------------|
| Statistical modelling | Core — distributions, Bayes, anomaly scores | Minimal — mostly comparison logic |
| Feature engineering | Core — extracting signals from raw logs | Different — defining the editable surface and constraints |
| Model selection | Core — XGBoost, neural nets, transformers | Minimal — the "model" is the search strategy |
| Prompt engineering | Not relevant | Core — writing the program.md directive |
| Config management | Moderate — model configs | Core — version controlling rules, thresholds, scripts |
| Eval design | Core — test sets, cross-validation | Core — but different: operational metrics, not statistical accuracy |
| Sandbox design | Test SIEM, synthetic data | Test PSA, historical replay, staging RMM |
| Domain knowledge needed | Cybersecurity — attack patterns, MITRE ATT&CK | MSP operations — ticket workflows, SLAs, client environments |
| Iteration speed | Days to weeks | Hours to overnight |

The SOC data scientist knows statistics, threat intelligence, and log parsing. The Karpathy Loop engineer knows prompt engineering, constraint design, operational metrics, and MSP workflows. There is some overlap in eval design and sandboxing, but the core competencies are different.

### Gap 4: Different Failure Modes

SOC ML fails when it misses a threat (false negative) or floods analysts with noise (false positive). The consequences are security incidents or analyst burnout.

The Karpathy Loop fails differently:

| Failure Mode | SOC ML | Karpathy Loop |
|-------------|--------|---------------|
| **Silent degradation** | Model drift detected by monitoring | Rules slowly optimise for the metric while diverging from business value |
| **Overfitting** | Model overfits training data, fails on novel attacks | Agent overfits to the test set, produces rules that score well but perform poorly on new tickets |
| **Metric gaming** | Not applicable (labels are ground truth) | Agent finds shortcuts to improve the metric without improving the service |
| **Compounding errors** | Bad model → bad detections → but bounded to detection | Bad rule → propagates to routing, SLA tracking, client reporting → cascades |
| **Auditability** | Model decisions are opaque | Every proposed change is in git, every experiment is logged — actually easier to audit |

The Karpathy Loop has a failure mode that SOC ML rarely encounters: metric gaming. When the agent can modify the system it is measured against, it can find ways to make the metric look good without making the service better. A ticket triage agent might learn to route everything to a single high-accuracy category. An alert tuning agent might suppress all alerts below severity 3.

SOC ML does not have this problem because the model does not modify the evaluation criteria. The Karpathy Loop agent modifies the system, so the eval harness must be locked and independent.

## What You Should Actually Do

### Do: Use the SOC Team's Infrastructure

| SOC Asset | How to Repurpose |
|-----------|-----------------|
| Data pipeline architecture | Adapt log ingestion pipelines for ticket/alert data ingestion |
| Labelled data methodology | Use their approach to building ground-truth test sets |
| Eval framework | Adapt their precision/recall testing for operational metrics |
| Sandbox design patterns | Use their test SIEM approach as a template for test PSA/RMM |
| Monitoring and alerting | Adapt model drift monitoring for rule drift detection |
| Experiment logging | Reuse their experiment tracking for Karpathy Loop runs |

### Do: Use the SOC Team's Culture

The SOC team already knows that:
- Most experiments fail, and that is fine
- You measure before you change
- Labels matter more than algorithms
- Deployment without monitoring is irresponsible

These cultural norms are half the battle. Most MSP operations teams have none of them.

### Do Not: Ask the SOC Team to Build Your Loops

They will approach it like a detection problem. They will try to train a classifier on ticket data and deploy it as a static model. They will miss the core insight of the Karpathy Loop: the agent modifies the system, evaluates the change, and keeps or reverts. That is not classification. That is optimisation through search.

### Do Not: Use the SOC Team's Tools

| SOC Tool | Why It Does Not Transfer |
|----------|------------------------|
| SIEM (Splunk, Elastic) | Built for log search, not for proposing and testing config changes |
| ML frameworks (scikit-learn, TensorFlow) | The Karpathy Loop does not need model training — it needs search + eval |
| Threat intelligence platforms | Irrelevant to ticket triage, alert tuning, script optimisation |
| SOAR platforms | Close in spirit (automation), but designed for playbook execution, not optimisation loops |
| MLOps pipelines (MLflow, Kubeflow) | Model lifecycle management, not continuous optimisation loops |

### Do: Hire or Develop a Different Profile

You need someone who sits at the intersection of MSP operations and AI agent engineering. Not a data scientist. Not a security analyst. A **loop engineer**.

| Attribute | What to Look For |
|-----------|-----------------|
| Background | MSP operations + scripting (PowerShell/Bash/Python) + curiosity about AI |
| Key skill | Writing clear constraint files (the program.md equivalent) |
| Second skill | Designing eval harnesses from operational data |
| Third skill | Version control discipline and experiment logging |
| Not required | Statistical modelling, neural network training, cybersecurity expertise |
| Mindset | Comfortable with 3% hit rates, measures everything, distrusts unvalidated changes |

This person might already be on your team — your best Level 3 technician who scripts everything, automates relentlessly, and is annoyed by inefficiency. They do not need to understand machine learning. They need to understand constraints, metrics, and iteration.

## The Joint Architecture: Where SOC and Karpathy Converge

There is one area where the SOC ML infrastructure and the Karpathy Loop should actively collaborate: **alert triage at the security boundary**.

Here is the convergence point:

| Layer | Owner | What It Does |
|-------|-------|-------------|
| Raw alert generation | RMM + SIEM | Produces alerts from monitoring and security tools |
| Security event classification | SOC ML (sister company) | Classifies alerts as security events vs operational events |
| Security event severity scoring | SOC ML (sister company) | Scores threat level, correlates with threat intelligence |
| Operational alert routing | Karpathy Loop (your MSP) | Routes non-security alerts to correct team with optimised thresholds |
| Alert noise reduction | Both jointly | SOC ML reduces security false positives, Karpathy Loop reduces operational false positives |
| Shared metric | Both | Total actionable alerts / total alerts → target above 70% |

The SOC team owns the security detection layer. Your MSP owns the operational optimisation layer. The boundary between them is where the most interesting collaboration happens — and where overlapping ML infrastructure creates a genuine competitive advantage that neither company could build alone.

## The Honest Assessment

| Question | Answer |
|----------|--------|
| Does the SOC sister company give you a head start? | Yes — culture, data infrastructure, eval discipline |
| Can you use their ML models directly? | No — detection models are not optimisation engines |
| Can you use their data scientists? | Partially — eval design and sandboxing transfer, core skills do not |
| Can you use their tools? | No — SIEM and ML frameworks solve different problems |
| Can you use their architecture patterns? | Yes — data pipelines, versioning, experiment logging, monitoring |
| Should you build the loops together? | At the alert boundary, yes. For MSP operations, no. |
| Does having a SOC ML sister company make you more money? | Only if you recognise the gaps and hire for them, rather than assuming the SOC team can just extend to MSP ops |

The sister company is an accelerator, not a substitute. They give you the cultural foundation and infrastructure patterns that take most organisations 6-12 months to develop. But the actual loops — the triplets, the constraints, the program.md files, the MSP-domain eval harnesses — those require someone who understands managed services operations, not cybersecurity detection.

Hire the loop engineer. Point them at ticket triage. Let the SOC team run security. Let the Karpathy Loop run operations. And at the boundary between them, build the shared alert pipeline that makes both better.

---

*Part of the Karpathy Loop for MSPs series: [Part 1: Where Auto-Improvement Lands](http://ubuntu4:3002/posts/the-karpathy-loop-for-msps-whe/) | [The Karpathy Loop Reference](http://ubuntu4:3002/posts/the-karpathy-loop-reference-guide/)*
- [Beyond IT: Extending the Loop to Every Business Function](http://ubuntu4:3002/posts/beyond-it-extending-the-karpat/)
- [Taking the Loop to Client Environments](http://ubuntu4:3002/posts/taking-the-karpathy-loop-to-cl/)
- [The LLM-Wiki Pattern for MSP Knowledge Management](http://ubuntu4:3002/posts/the-llm-wiki-pattern-write-tim/)

**Tags**: msp, managed-services, soc, machine-learning, karpathy-loop, auto-improvement, siem, ai-agents, security-operations
**Categories**: AI Automation, Business Strategy