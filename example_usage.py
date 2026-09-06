"""
Example usage of Dynamic Mixture of Agents MoA Layer Skill.
"""

from client import MixtureOfAgentsLayer


def main():
    print("=== Dynamic Mixture of Agents MoA Layer Demonstration ===")
    moa = MixtureOfAgentsLayer(layer_index=1)

    query = "What are the primary performance trade-offs of HNSW vector indexing?"

    proposals = [
        {
            "agent_id": "System_Architect_Agent",
            "response": "HNSW offers logarithmic query complexity O(log N) and high recall, but incurs significant RAM overhead for storing skip-list graph edges and slow index construction time."
        },
        {
            "agent_id": "Database_Engineer_Agent",
            "response": "Memory consumption is the main drawback due to graph links per vector. Build times scale with M and efConstruction parameters, though search latency is ultra-fast."
        },
        {
            "agent_id": "Algorithmic_Researcher_Agent",
            "response": "Trade-offs include large memory footprint, expensive updates/deletions requiring graph rewiring, balanced by sub-millisecond approximate nearest neighbor retrieval."
        }
    ]

    res = moa.aggregate_proposals(query, proposals)
    print(f"Layer {res['layer_index']} Aggregation:")
    print(f"  Proposers Count: {res['proposers_count']}")
    print(f"  Highest Consensus Agent: {res['highest_consensus_agent']} (Score: {res['consensus_score']})")
    print(f"  Mean Agreement: {res['mean_consensus']}")
    print("\nSynthesized Aggregator Prompt Preview (First 200 chars):")
    print(res["aggregator_prompt"][:200] + "...")


if __name__ == "__main__":
    main()
