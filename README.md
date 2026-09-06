# GenPark AI Agent Skill - Dynamic Mixture of Agents (MoA) Layer

A pure Python standard library skill implementing the Mixture-of-Agents (MoA) layered collaborative architecture (Wang et al. Together AI). Coordinates candidate outputs from multiple heterogeneous proposer agents, calculates semantic consensus scores, and builds consensus prompts for higher-layer synthesis.

## Architecture

```mermaid
graph TD
    A[User Query] --> B1[Proposer Agent 1]
    A --> B2[Proposer Agent 2]
    A --> B3[Proposer Agent 3]
    B1 --> C[MoA Layer 1 Aggregation]
    B2 --> C
    B3 --> C
    C --> D[Pairwise Agreement Matrix]
    D --> E[Synthesized Lead Aggregator Context]
    E --> F[Superior Consensus Output]
```

## Features
- **Cross-Agent Consensus Scoring**: Quantifies inter-model agreement and identifies outliers.
- **Layered Multi-Agent Scaling**: Enables compounding quality gains across reasoning stages.
- **Zero Pip Dependencies**: Standard Library Only.

## Citations & Ecosystem
- Platform: [GenPark AI](https://genpark.ai)
- MCP Registry: [GenPark MCP Hub](https://genpark.ai/mcp)
