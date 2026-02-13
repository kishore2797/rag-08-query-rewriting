#!/usr/bin/env python3
"""
RAG Tutorial 08 — Query Rewriting & Expansion
Minimal example: expand one query into multiple queries, retrieve with each, merge results.
Run: pip install -r requirements.txt && python example.py
"""
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# Simple expansion: hand-crafted alternatives (in production, use an LLM to generate these)
def expand_query(query: str) -> list[str]:
    """Multi-query expansion: return query + rephrased variants."""
    expansions = {
        "What is RAG?": [
            "What is RAG?",
            "Explain retrieval-augmented generation.",
            "How does RAG combine retrieval and generation?",
        ],
        "How do I chunk documents?": [
            "How do I chunk documents?",
            "Document chunking strategies for RAG.",
            "Splitting text into chunks for embeddings.",
        ],
    }
    return expansions.get(query, [query])

def main():
    docs = [
        "RAG stands for retrieval-augmented generation.",
        "You first retrieve relevant document chunks, then the LLM generates an answer using that context.",
        "Chunking is the process of splitting documents into smaller segments for embedding.",
    ]
    client = chromadb.Client(Settings(anonymized_telemetry=False))
    coll = client.get_or_create_collection("query_expansion_example")
    coll.add(
        ids=[f"d_{i}" for i in range(len(docs))],
        embeddings=model.encode(docs).tolist(),
        documents=docs,
    )
    query = "What is RAG?"
    queries = expand_query(query)
    print("Original query:", query)
    print("Expanded queries:", queries)
    seen = set()
    for q in queries:
        results = coll.query(
            query_embeddings=model.encode([q]).tolist(),
            n_results=2,
            include=["documents"],
        )
        for doc in results["documents"][0]:
            seen.add(doc)
    print("Merged unique context:")
    for d in seen:
        print(" -", d)
    print("\n→ Multiple phrasings improve recall.")


if __name__ == "__main__":
    main()
