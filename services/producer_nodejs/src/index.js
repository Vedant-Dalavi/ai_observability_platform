import kafka from "./kafka.js"
import randomLog from "./generatingLog.js"
import { Partitioners } from "kafkajs"

async function startProducer() {
    const producer = kafka.producer({
        createPartitioner: Partitioners.LegacyPartitioner
    })

    await producer.connect()
    console.log("Producer connected. Sending logs")

    setInterval(async () => {
        const log = randomLog()

        await producer.send({
            topic: "observability.logs",
            messages: [
                { value: JSON.stringify(log) }
            ]
        })

        console.log("Sent Log:", log)
    }, 2000)
}

startProducer().catch(console.error)
