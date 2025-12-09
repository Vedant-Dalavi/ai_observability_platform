# Day 1

## What I learned today:

- Kafka basics: producer, consumer, broker, topic, partitions.
- Docker basics and how to run Kafka using docker-compose.
- Created project structure.
- Successfully started Kafka locally.
- Created first Kafka topic: observability.logs.

# Day 2

## What I learned today:

- Kafka producer basics
- How messages flow from Node → Kafka
- How to generate synthetic microservice logs
- How to connect Node.js to Kafka using KafkaJS
- Successfully produced logs and validated them via kafka-console-consumer

# Day 3

## What I learned today:

- How Kafka consumers work
- How to use aiokafka in Python
- How to clean/validate logs
- How Parquet storage works
- Built consumer that writes Bronze layer data

# Day 4

## What I learned Today:

- What embeddings are and how they represent semantic meaning
- How sentence-transformers generates vectors for logs
- How to build a FastAPI embedding service
- How to test embeddings locally
- Prepared for vector database integration tomorrow

# Day 5

## What I learned today:

- What vector databases are and why they are used
- Qdrant collections, points, payloads, search
- How to embed logs and store them in Qdrant
- How to perform semantic search on logs

Outcome:
Completed semantic search engine. System can find similar logs based on meaning.

# Day 6

## What I learned today:

- How RAG works (retrieve → augment → generate)
- How to build retrieval using Qdrant
- How to build prompts for logs
- How to call an LLM (OpenAI or Ollama)
- Built the /rag/query API that gives complete incident analysis

Outcome:
My system now supports full AI reasoning over log data.
