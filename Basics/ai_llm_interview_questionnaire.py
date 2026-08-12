# AI / LLM INTERVIEW FUNDAMENTALS — REVISION QUESTION BANK

# Priority:
# P0 = must know
# P1 = important
# P2 = deeper/follow-up

# Focus:
# AI/ML basics, LLMs, transformers, tokens, prompting, embeddings,
# vector search, RAG, evaluation, agents/tools, production,
# security, reliability, cost and backend architecture.

# ============================================================
# AI / ML BASICS
# ============================================================

# Q1 [P0] What is AI?
# ANSWER:
# Broad field of systems performing tasks associated with capabilities
# such as perception, prediction, language and decision making.

# Q2 [P0] What is machine learning?
# ANSWER:
# Methods where models learn patterns from data rather than every rule
# being explicitly programmed.

# Q3 [P0] Supervised vs unsupervised learning?
# ANSWER:
# Supervised uses labeled examples; unsupervised finds structure without
# target labels.

# Q4 [P0] Classification vs regression?
# ANSWER:
# Classification predicts categories; regression predicts continuous values.

# Q5 [P0] What is a model?
# ANSWER:
# A parameterized computational representation used to make predictions,
# decisions or generate outputs.

# ============================================================
# LLM / TRANSFORMER BASICS
# ============================================================

# Q6 [P0] What is an LLM?
# ANSWER:
# A large language model is trained on large amounts of data to model
# language patterns and generate/transform text.

# Q7 [P0] What is a transformer?
# ANSWER:
# Neural-network architecture built around attention mechanisms and widely
# used for modern language models.

# Q8 [P0] What is attention?
# ANSWER:
# A mechanism that lets the model determine how strongly different tokens
# should influence representations.

# Q9 [P0] What is self-attention?
# ANSWER:
# Attention where tokens in the same sequence attend to one another.

# Q10 [P1] Why are transformers useful for language?
# ANSWER:
# They model relationships between tokens across context and support
# efficient parallel training.

# ============================================================
# TOKENS / CONTEXT / GENERATION
# ============================================================

# Q11 [P0] What is a token?
# ANSWER:
# A unit produced by a tokenizer and processed by the model. It can be
# a word, subword, punctuation, or another token unit.

# Q12 [P0] Why does tokenization matter?
# ANSWER:
# Token count affects context usage, latency and token-based API cost.

# Q13 [P0] What is a context window?
# ANSWER:
# The amount of tokenized context a model can consider within its limits.

# Q14 [P1] Does a larger context window automatically make an application better?
# ANSWER:
# No. More context can increase cost/latency and add irrelevant information.

# Q15 [P1] What is temperature?
# ANSWER:
# A sampling parameter that generally controls output variation; exact
# behavior depends on the model/provider.

# Q16 [P1] What is top_p?
# ANSWER:
# A sampling parameter that restricts candidate tokens to a probability
# mass threshold.

# ============================================================
# PROMPT ENGINEERING
# ============================================================

# Q17 [P0] What is prompt engineering?
# ANSWER:
# Designing instructions, context, examples, constraints and output
# formats to improve model behavior.

# Q18 [P0] What makes a good prompt?
# ANSWER:
# Clear task, relevant context, explicit constraints, desired output
# structure, examples when useful, and clear uncertainty rules.

# Q19 [P0] What is few-shot prompting?
# ANSWER:
# Providing a few examples demonstrating desired behavior.

# Q20 [P1] What is structured output?
# ANSWER:
# Requiring model output to follow a defined schema such as JSON, ideally
# with provider/framework schema-constrained generation.

# Q21 [P1] Why should application instructions be separated from user data?
# ANSWER:
# To reduce instruction confusion and help defend against prompt injection.
# Security controls must still live outside the model.

# ============================================================
# EMBEDDINGS
# ============================================================

# Q22 [P0] What is an embedding?
# ANSWER:
# A numerical vector representation designed to capture useful semantic
# relationships.

# Q23 [P0] Why use embeddings in RAG?
# ANSWER:
# Convert documents and queries into vectors so semantically related
# content can be retrieved.

# Q24 [P0] What is cosine similarity?
# ANSWER:
# Similarity based on the angle between vectors:
#
# dot(A, B) / (norm(A) * norm(B))

# Q25 [P1] Cosine similarity vs Euclidean distance?
# ANSWER:
# Cosine compares direction; Euclidean compares geometric distance.
# Appropriate choice depends on the embedding space/system.

# ============================================================
# VECTOR SEARCH
# ============================================================

# Q26 [P0] What is a vector database?
# ANSWER:
# A system optimized for storing vectors and retrieving similar vectors,
# usually with metadata.

# Q27 [P0] What is semantic search?
# ANSWER:
# Retrieval based on semantic similarity rather than only exact keywords.

# Q28 [P0] What is metadata filtering?
# ANSWER:
# Restricting candidates using fields such as tenant, document type,
# permissions, date or source.

# Q29 [P0] Why is metadata filtering critical in enterprise RAG?
# ANSWER:
# It improves relevance and, importantly, can enforce tenant/access
# boundaries before content reaches the model.

# Q30 [P1] What is hybrid search?
# ANSWER:
# Combining lexical/keyword retrieval with semantic/vector retrieval.

# Q31 [P2] What is approximate nearest-neighbor search?
# ANSWER:
# Methods that trade some exactness for faster nearest-vector retrieval
# at scale.

# ============================================================
# RAG
# ============================================================

# Q32 [P0] What is RAG?
# ANSWER:
# Retrieval-Augmented Generation retrieves external information and supplies
# it as context to an LLM before generating an answer.

# Q33 [P0] Why use RAG?
# ANSWER:
# To ground answers in private/current/domain documents without retraining
# the model for every knowledge update.

# Q34 [P0] Basic RAG pipeline?
# ANSWER:
# Ingestion:
# documents -> parse -> clean -> chunk -> embed -> store/index
#
# Query:
# question -> retrieve -> optionally rerank -> build context -> LLM
# -> answer/citations.

# Q35 [P0] What is chunking?
# ANSWER:
# Splitting documents into retrieval units.

# Q36 [P0] Why does chunk size matter?
# ANSWER:
# Small chunks can be precise but lose context.
# Large chunks preserve context but may add noise and consume more tokens.

# Q37 [P1] What is chunk overlap?
# ANSWER:
# Repeating some content across adjacent chunks to preserve boundary context.

# Q38 [P0] Why can RAG produce poor answers?
# ANSWER:
# Bad parsing, chunking, embeddings, retrieval, filtering, irrelevant
# context, poor prompting, model limitations, or hallucination.

# Q39 [P1] How do you improve retrieval?
# ANSWER:
# Improve parsing/chunking, metadata filters, hybrid search, query
# rewriting, embeddings, top-k and reranking, then evaluate results.

# Q40 [P1] What is reranking?
# ANSWER:
# A second-stage relevance model reorders retrieved candidates.

# Q41 [P1] What is query rewriting?
# ANSWER:
# Transforming the user's question into a search-oriented query that may
# improve retrieval.

# Q42 [P1] What is grounded generation?
# ANSWER:
# Generating answers based on supplied/retrieved evidence rather than
# relying only on learned model knowledge.

# ============================================================
# RAG EVALUATION
# ============================================================

# Q43 [P0] How do you evaluate a RAG system?
# ANSWER:
# Separate retrieval quality from generation quality.
# Retrieval: recall@k, precision@k, relevance.
# Generation: faithfulness/groundedness, relevance, correctness.

# Q44 [P1] What is retrieval recall?
# ANSWER:
# Whether the relevant item appears in the retrieved top-k results.

# Q45 [P0] What is hallucination?
# ANSWER:
# Unsupported, fabricated or incorrect model output presented as an answer.

# Q46 [P0] Does RAG eliminate hallucinations?
# ANSWER:
# No. It can reduce unsupported answers but models can still misinterpret
# or ignore retrieved evidence.

# Q47 [P1] What is an evaluation dataset?
# ANSWER:
# Fixed representative inputs with expected/acceptable outcomes used to
# measure quality.

# ============================================================
# FINE-TUNING
# ============================================================

# Q48 [P0] What is fine-tuning?
# ANSWER:
# Further training a pretrained model on task/domain-specific examples.

# Q49 [P0] RAG vs fine-tuning?
# ANSWER:
# RAG injects external/current/private knowledge at inference time.
# Fine-tuning changes learned behavior/task patterns.

# Q50 [P1] When prefer RAG?
# ANSWER:
# When the main requirement is access to changing/private/documented
# knowledge and source grounding.

# Q51 [P1] When might fine-tuning help?
# ANSWER:
# Specialized behavior, output patterns, style, or task performance where
# sufficient quality training data exists.

# ============================================================
# TOOLS / AGENTS
# ============================================================

# Q52 [P0] What is function/tool calling?
# ANSWER:
# The model emits a structured request for a predefined tool; the
# application executes it and returns the result.

# Q53 [P0] What is an AI agent?
# ANSWER:
# A system where a model participates in a multi-step control loop and
# can choose/use tools to accomplish a goal.

# Q54 [P0] Agent vs RAG?
# ANSWER:
# RAG is primarily retrieval + generation.
# An agent is a broader multi-step system and can use RAG as one capability.

# Q55 [P1] What is an agent loop?
# ANSWER:
# Observe context -> decide action -> call tool -> inspect result ->
# continue or stop.

# Q56 [P1] Why can agents be unreliable?
# ANSWER:
# More steps create more failure opportunities: wrong tool, bad arguments,
# loops, hallucinations, latency and cost.

# Q57 [P0] Should an LLM directly execute arbitrary tools?
# ANSWER:
# No. Tools need explicit schemas, validation, authorization, least
# privilege, timeouts, sandboxing where needed, and auditing.

# ============================================================
# SECURITY
# ============================================================

# Q58 [P0] What is prompt injection?
# ANSWER:
# Untrusted content attempts to manipulate the model's instructions or
# cause unintended behavior.

# Q59 [P0] Why is RAG vulnerable to prompt injection?
# ANSWER:
# Retrieved documents can contain malicious instructions that the model
# may interpret as commands.

# Q60 [P0] How do you mitigate prompt injection?
# ANSWER:
# Treat retrieved/user content as untrusted; enforce auth outside the
# model; restrict tools; validate arguments; separate instructions/data;
# use allowlists and sandboxing; audit actions.

# Q61 [P0] Can an LLM be your authorization layer?
# ANSWER:
# No. Authorization must be enforced deterministically by application
# infrastructure. The model is not a security boundary.

# ============================================================
# MULTI-TENANT RAG
# ============================================================

# Q62 [P0] How would you build multi-tenant RAG?
# ANSWER:
# Store tenant/access metadata and enforce tenant authorization filters
# during retrieval. The model should never receive unauthorized chunks.

# Q63 [P0] Why is putting tenant_id only in the prompt insufficient?
# ANSWER:
# Prompts are not security controls. Unauthorized data must be blocked
# before it reaches the prompt.

# Q64 [P1] What metadata belongs with chunks?
# ANSWER:
# tenant_id, document_id, source, access scope, timestamps, version,
# document type, chunk position and embedding/model metadata.

# ============================================================
# INGESTION / DATA PIPELINES
# ============================================================

# Q65 [P0] Design document ingestion.
# ANSWER:
# Upload -> validation -> parse -> clean -> chunk -> embed -> index/store
# -> mark ready. For scale, make processing asynchronous and idempotent.

# Q66 [P1] What if embedding generation fails?
# ANSWER:
# Persist job state, retry with bounded backoff, make work idempotent,
# record failure reason and expose operational status.

# Q67 [P1] How do you prevent duplicate ingestion?
# ANSWER:
# Stable document/version IDs or content hashes plus an idempotency/
# uniqueness strategy.

# Q68 [P1] How do you handle document updates?
# ANSWER:
# Version documents, regenerate affected chunks, update indexes safely,
# and prevent stale versions from being retrieved.

# ============================================================
# PRODUCTION LLM APIs
# ============================================================

# Q69 [P0] How do you protect LLM API keys?
# ANSWER:
# Keep provider credentials on trusted backend infrastructure; never expose
# them directly to browsers/mobile clients.

# Q70 [P0] How do you control LLM cost?
# ANSWER:
# Appropriate model selection, token limits, context reduction, caching,
# retrieval, batching where appropriate, quotas and monitoring.

# Q71 [P0] How do you control LLM latency?
# ANSWER:
# Appropriate model, shorter context, efficient retrieval, caching,
# parallel independent operations and streaming where useful.

# Q72 [P1] What is streaming?
# ANSWER:
# Returning generated output incrementally instead of waiting for the
# entire response.

# Q73 [P1] Does streaming reduce total generation time?
# ANSWER:
# Not necessarily. It mainly improves time-to-first-token/perceived latency.

# ============================================================
# RELIABILITY
# ============================================================

# Q74 [P0] How do you make LLM integrations reliable?
# ANSWER:
# Timeouts, bounded retries/backoff, rate-limit handling, fallback,
# validation, idempotency, observability and graceful degradation.

# Q75 [P0] Why bound retries?
# ANSWER:
# Unlimited retries increase latency/cost and can create retry storms.

# Q76 [P1] What is exponential backoff?
# ANSWER:
# Increasing retry delay, usually with jitter, to reduce synchronized
# retry traffic and allow recovery.

# ============================================================
# MODEL CHOICE
# ============================================================

# Q77 [P0] How do you choose a model?
# ANSWER:
# Evaluate representative task quality, latency, cost, context needs,
# tool/structured-output support, privacy/compliance, throughput and
# reliability.

# Q78 [P0] Should you always use the most powerful model?
# ANSWER:
# No. Use the smallest model that meets quality/reliability requirements
# unless other constraints justify a larger model.

# Q79 [P1] What is model fallback?
# ANSWER:
# Routing to an alternate model/provider after defined failure/limit
# conditions, with attention to compatible behavior and quality.

# ============================================================
# OBSERVABILITY
# ============================================================

# Q80 [P0] What should you monitor?
# ANSWER:
# Latency, errors/timeouts, token usage, cost, provider failures,
# retrieval metrics, tool failures, user feedback, safety incidents and
# quality metrics.

# Q81 [P1] What should an LLM trace contain?
# ANSWER:
# Request ID, model, latency, token counts, retrieval/tool timing,
# failures and evaluation signals. Avoid unnecessary sensitive content.

# ============================================================
# PRACTICAL SYSTEM DESIGN
# ============================================================

# Q82 [P0] Design a RAG system for company documentation.
# ANSWER SHOULD COVER:
# ingestion, parsing, chunking, embeddings, vector store, metadata/
# permissions, retrieval, reranking, prompt construction, generation,
# citations, evaluation, monitoring and security.

# Q83 [P0] How prevent cross-tenant retrieval?
# ANSWER:
# Enforce tenant/access filters in the retrieval/data layer, not in the
# prompt.

# Q84 [P1] What if retrieval returns irrelevant chunks?
# ANSWER:
# Improve parsing, chunking, metadata filters, query formulation,
# embeddings, retrieval method, top-k and reranking; then evaluate.

# Q85 [P1] What if retrieval returns too many chunks?
# ANSWER:
# Reduce top-k, rerank, filter/compress context, and improve retrieval
# precision.

# Q86 [P0] RAG vs database query?
# ANSWER:
# Use structured DB queries for exact structured facts/aggregation.
# Use RAG for unstructured knowledge. Many production systems combine them.

# Q87 [P1] Could an LLM replace a deterministic rule engine?
# ANSWER:
# Not generally for critical deterministic business rules. LLMs can help
# interpret unstructured input, but final authorization/business rules
# should remain deterministic where correctness/auditability matter.

# ============================================================
# CODING / IMPLEMENTATION
# ============================================================

# Q88 [P0] Implement cosine similarity.
# ANSWER IDEA:
# dot(A, B) / (norm(A) * norm(B))
# Explicitly handle zero vectors.

# Q89 [P0] Implement top-k vector similarity search.
# ANSWER IDEA:
# Compute similarity, maintain/order candidates, return top k.
# Discuss O(n) scoring and how ANN indexes change the scaling problem.

# Q90 [P1] Implement a basic text chunker with overlap.
# DISCUSS:
# chunk size, overlap, boundaries, token vs character units, metadata.

# Q91 [P1] Design an LLM API retry wrapper.
# DISCUSS:
# retryable errors, timeout, max attempts, exponential backoff, jitter,
# idempotency and observability.

# Q92 [P1] Design an API that streams LLM output.
# DISCUSS:
# streaming protocol, cancellation, provider stream, client disconnect,
# errors after partial output, backpressure and observability.

# ============================================================
# RAPID FIRE
# ============================================================
# Q93 What is an LLM?
# Q94 What is a token?
# Q95 What is a context window?
# Q96 What is an embedding?
# Q97 What is vector search?
# Q98 What is RAG?
# Q99 Why chunk documents?
# Q100 What is cosine similarity?
# Q101 What is hallucination?
# Q102 What is prompt injection?
# Q103 Why isn't an LLM a security boundary?
# Q104 RAG vs fine-tuning?
# Q105 What is function calling?
# Q106 What is an AI agent?
# Q107 What is reranking?
# Q108 What is hybrid search?
# Q109 Why does token count matter?
# Q110 How do you control cost?
# Q111 How do you control latency?
# Q112 How do you evaluate RAG?
# Q113 How do you secure multi-tenant RAG?
# Q114 What do you monitor in production?

# ============================================================
# ANSWER STRUCTURE
# ============================================================
# For an AI conceptual question:
#
# 1. One-sentence definition.
# 2. Explain the mechanism.
# 3. Give a concrete example.
# 4. Give a backend/production use case.
# 5. Mention one limitation/trade-off.
#
# Example:
# "RAG retrieves relevant external context and supplies it to the LLM.
# It is useful for private/current/document-grounded knowledge. The basic
# pipeline is ingestion -> chunking -> embeddings/indexing -> retrieval
# -> context construction -> generation. Its main failure points include
# retrieval quality, stale data and authorization."
