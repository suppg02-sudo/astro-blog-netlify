---
pubDatetime: 2026-02-08T00:12:00Z
title: "DataHub 2025 Roadmap: Discovery, Governance & Observability Enhancements"
postSlug: "datahub-2025-roadmap-discovery-governance-observability"
description: "DataHub 2025 Roadmap: Discovery, Governance & Observability Enhancements"
tags:
  - others
---

# DataHub 2025 Roadmap: Discovery, Governance & Observability Enhancements

## Introduction

DataHub 1.0 marks a significant milestone for the open-source metadata platform. In this comprehensive update, Maggie from the DataHub team walks through the exciting initiatives coming in 2025 across four core pillars: Discovery, Governance, Observability, and the Platform itself.

## Four Pillars of DataHub

The DataHub platform is built on four foundational pillars:

1. **Discovery** - Enable end users to discover and leverage relevant data assets
2. **Governance** - Ensure assets are well-documented, classified, and compliant
3. **Observability** - Provide unified visibility into data quality and ecosystem health
4. **Metadata Graph** - The core platform supporting all three pillars

## Discovery Initiatives for 2025

### Human-Centered Insights

DataHub is focusing on capturing and surfacing human context around data. This goes beyond technical metadata to include business context and team knowledge that makes data assets more discoverable and usable.

### Intelligent Exploration

When searching for data assets, users will have access to rich contextual information including:
- Technical metadata
- Logical metadata  
- Human context and documentation

### End-to-End Lineage Enhancement

Lineage is one of DataHub's core features. 2025 brings improvements to make lineage more:
- Robust and reliable
- Intuitive to navigate
- Comprehensive in coverage

### New Integrations

DataHub continues expanding connector coverage with new integrations:

**Recently Shipped:**
- MLflow
- CockroachDB
- Dbt ODB (with major improvements)

**In Development:**
- Hex
- Vertex AI (expected next month)

**Planned:**
- Cloud Dataflow
- Azure Data Lake
- Azure Synapse

### Hierarchical Lineage (Coming H2 2025)

Large lineage graphs can become overwhelming. Hierarchical lineage allows teams to "zoom out" and understand data flows at different levels:
- **Platform-to-platform** level
- **Schema-to-schema** level
- **Logical lineage** between data products and domains

This makes it easier to see your entire ecosystem at a glance without getting lost in granular details.

### Metrics Catalog (Coming H2 2025)

A new feature expanding on glossary term support, making it easy to:
- Register key metrics
- Associate metrics with data assets
- Document metric definitions

This addresses strong community demand for better metrics management within DataHub.

## Governance Initiatives for 2025

### Universal Data Discovery

The goal is complete visibility into every asset:
- Every dataset
- Every AI model
- Every transformation
- Every dashboard

DataHub becomes your central data registry.

### Centralized Compliance

DataHub positions itself as the central compliance hub for:
- **Ownership documentation**
- **Purpose statements** (critical for GDPR compliance)
- **PII classification**
- **Data lineage** for regulatory audits

### Policy Enforcement

Once assets are classified, enforce policies across your ecosystem:

**Currently in Development:**
- Tag and glossary term sync to external platforms (Snowflake, BigQuery, DBT)
- Open-sourcing Snowflake bidirectional sync

**For DataHub Cloud Users:**
- These features are already available - reach out to your account team

**Coming in 2025:**
- Parent-child logical datasets for unified asset management
- Cleaner definitions at parent level that propagate to materialized layers

This is especially useful for prod-to-warehouse flows where the same dataset is replicated across environments.

## Observability Initiatives for 2025

### Accessible Observability

Making data quality understanding available to all team members, not just technical experts.

### Collaborative Observability

DataHub 1.0 improvements include:
- **Enhanced assertions management** - Search, filter, and group data quality checks
- **Historical context viewing** - See past assertion outcomes
- **Enriched incident flow** - Set priority, manage stage, add assignments, and view full history in one place

Treat DataHub as your centralized incident tracking and resolution platform.

### Contextual Quality Insights

When responding to data quality issues, you have full context:
- How the data is used downstream
- How the data was produced
- Complete lineage and dependencies

## Platform & SDK Improvements

### Python SDK v2

Significant improvements to the Python SDK for:
- Registering data assets
- Enriching assets with metadata
- Retrieving data for external systems

**Already Shipped:**
- Search and Dataset SDKs (simplified, streamlined, performant)

**In Development:**
- Lineage SDK

**Planned:**
- Comprehensive documentation overhaul
- AI SDK for mapping AI tooling and systems

### Service Accounts

New feature for teams to:
- Create programmatic workflows
- Manage custom automations
- Scale DataHub across teams

Service accounts are decoupled from individual users, allowing team-level ownership and better access control at scale.

### APIs and SDKs

Core focus areas:
- Robust mechanisms for automation
- Developer experience quality
- Audit logging and tracing for compliance

## Summary

DataHub's 2025 roadmap is ambitious, focusing on:
1. **Better data discovery** through hierarchical lineage and intelligent exploration
2. **Stronger governance** with centralized compliance and policy enforcement
3. **Accessible observability** for data quality and incident management
4. **Better developer experience** with improved SDKs and APIs

The team is actively seeking feedback and collaboration on these initiatives. The best way to stay updated is through:
- DataHub blog
- DataHub Slack community
- Email newsletter

---

*Original video: [DataHub 2025 Roadmap Walkthrough](https://www.youtube.com/watch?v=dGs9ac7-nas)*