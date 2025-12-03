import asyncio
from aiokafka import AIOKafkaConsumer
from processor import clean_log
from writer import write_to_parquet

async def start_consumer():
    consumer = AIOKafkaConsumer(
        "observability.logs",
        bootstrap_servers="localhost:9092",
        group_id="etl-consumer-group"
    )

    await consumer.start()
    print("Python consumer connected...")

    buffer = []

    try:
        async for msg in consumer:
            cleaned = clean_log(msg.value)
            buffer.append(cleaned)

            # Write every 20 logs
            if len(buffer) >= 20:
                write_to_parquet(buffer)
                buffer = []

    finally:
        # on shutdown, write remaining records
        if buffer:
            await asyncio.to_thread(write_to_parquet, buffer)
        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(start_consumer())
