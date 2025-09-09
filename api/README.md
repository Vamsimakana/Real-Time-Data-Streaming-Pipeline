# Real-Time Data Streaming Pipeline

Quick start (dev):
1. docker-compose up -d
   - starts Kafka and Postgres
2. Create Kafka topic `events` if needed or produce directly (some Kafka images auto-create)
3. Run producer: python producer/producer.py
4. Run spark job (requires local PySpark): python spark-job/job.py
5. Start API: uvicorn api.main:app --reload
6. View aggregates: http://localhost:8000/aggregates

Notes: Local Spark + Kafka requires Java and enough memory. For cloud/production use managed services.
