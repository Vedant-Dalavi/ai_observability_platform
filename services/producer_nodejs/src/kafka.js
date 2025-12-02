import { Kafka } from "kafkajs"

const kafka = new Kafka({
    clientId: "log-producer",
    brokers: ["localhost:9092"]   // or kafka:9092 if inside Docker
})

export default kafka
