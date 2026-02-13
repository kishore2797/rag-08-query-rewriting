# 🔄 RAG Tutorial 08 — Query Rewriting & Expansion

<p align="center">
  <a href="https://github.com/kishore2797/mastering-rag"><img src="https://img.shields.io/badge/Series-Mastering_RAG-blue?style=for-the-badge" /></a>
  <img src="https://img.shields.io/badge/Part-8_of_16-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge" />
</p>

> **Part of the [Mastering RAG](https://github.com/kishore2797/mastering-rag) tutorial series**  
> Previous: [07 — Parent-Document Retrieval](https://github.com/kishore2797/rag-07-parent-document-retrieval) | Next: [09 — Re-ranking Pipeline](https://github.com/kishore2797/rag-09-reranking-pipeline)

---

## 🌍 Real-World Scenario

> A user asks your customer support bot: "it's not working." That's it. No product name, no error message, no context. Standard vector search finds... everything. **Multi-query expansion** rewrites it into: ["product not functioning properly", "error when using the application", "troubleshooting common issues"]. **Query decomposition** breaks it into: "What product is the user referring to?", "What error are they experiencing?". Suddenly, retrieval gets 3x better — all without asking the user to clarify.

---

## 🏗️ What You'll Build

A RAG system with three query optimization strategies: **HyDE** (Hypothetical Document Embedding), **multi-query expansion**, and **query decomposition**. Toggle each strategy on/off and see how retrieval results change.

```
"Why is my app slow?"
  ↓
HyDE:    Generate hypothetical answer → embed that instead of the raw query
Multi-Q: Expand to 3 rephrased queries → retrieve for each → merge results
Decomp:  Break into sub-questions → retrieve per sub-question → combine
```

## 🔑 Key Concepts

- **HyDE**: bridges the vocabulary gap between short queries and long documents
- **Multi-query**: catches different phrasings of the same user intent
- **Decomposition**: handles complex, multi-part questions
- **Retrieval improvement**: measure recall before/after rewriting

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11+ · FastAPI · ChromaDB · OpenAI/Gemini · LangChain |
| Frontend | React 19 · Vite · Tailwind CSS |

## 🚀 Quick Start

### Backend

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8001
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 — run queries with different rewriting strategies and compare.

## 📖 What You'll Learn

1. Why raw user queries often perform poorly in vector search
2. How HyDE generates synthetic documents to improve retrieval
3. When multi-query expansion helps (ambiguous queries)
4. When decomposition helps (complex, multi-part questions)
5. How to measure the retrieval improvement from each strategy

## 📋 Prerequisites

- Python 3.11+ and Node.js 18+
- A working RAG pipeline (concepts from [Tutorial 05](https://github.com/kishore2797/rag-05-basic-rag-pipeline))
- LLM API key (needed for HyDE and decomposition)

## ✏️ Exercises

1. **Head-to-head**: Use 20 test queries. Run each with raw query, HyDE, multi-query, and decomposition. Score which retrieves the most relevant chunks. Create a leaderboard.
2. **Latency measurement**: HyDE and decomposition need an extra LLM call. Measure the latency overhead. Is the quality improvement worth the extra 1–2 seconds?
3. **Bad query stress test**: Try deliberately vague queries ("stuff about that thing"), typos ("mashine lerning"), and mixed-language queries. Which strategy recovers best?
4. **Combine strategies**: Try HyDE + multi-query together. Does combining strategies compound the improvement or add noise?
5. **Cost analysis**: Calculate the extra API cost per query for each strategy. At 10K queries/day, what's the monthly cost difference?

## ⚠️ Common Mistakes

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| HyDE generates a bad hypothetical answer | The LLM hallucinates, and you embed that hallucination | Keep HyDE answers short (2–3 sentences); use a low temperature |
| Multi-query returns too many duplicates | Same chunks match multiple rephrased queries | Deduplicate results by chunk ID before passing to the LLM |
| Decomposition creates irrelevant sub-questions | LLM over-decomposes a simple query into 5+ parts | Limit decomposition to 2–3 sub-questions; skip for short, clear queries |
| Rewriting makes queries worse | Original query was already precise; rewriting adds noise | Add a "confidence check" — only rewrite if the original query's retrieval score is below a threshold |

## 📚 Further Reading

- [Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE)](https://arxiv.org/abs/2212.10496) — The original HyDE paper (Gao et al., 2022)
- [Query Expansion by Prompting Large Language Models](https://arxiv.org/abs/2305.03653) — Multi-query expansion research
- [Query2Doc](https://arxiv.org/abs/2303.07678) — Another approach to query expansion with LLMs
- [RAG Query Rewriting Best Practices](https://www.pinecone.io/learn/series/rag/rerankers/) — Pinecone's practical guide

## ➡️ Next Steps

You've optimized the query. Now optimize the results — head to **[Tutorial 09 — Re-ranking Pipeline](https://github.com/kishore2797/rag-09-reranking-pipeline)** to add cross-encoder re-ranking after retrieval.

---

<p align="center">
  <sub>Part of <a href="https://github.com/kishore2797/mastering-rag">Mastering RAG — From Zero to Production</a></sub>
</p>
