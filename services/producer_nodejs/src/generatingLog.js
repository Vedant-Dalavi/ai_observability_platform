import { v4 as uuidv4 } from "uuid"

export default function randomLog() {
    return {
        id: uuidv4(),
        level: "INFO",
        message: "Test log",
        timestamp: new Date().toISOString()
    }
}
