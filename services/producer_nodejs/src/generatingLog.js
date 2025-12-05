import { v4 as uuidv4 } from "uuid";

export default function randomLog() {
    const levels = ["INFO", "WARN", "ERROR", "DEBUG"];

    const messages = [
        "User logged in",
        "Database connection established",
        "Request timed out",
        "Cache miss detected",
        "Service started successfully",
        "Background job executed",
        "Failed to fetch data",
        "Retrying request",
        "Unauthorized access attempt",
        "Payment service responded slowly",
        "Configuration loaded",
        "Heartbeat check passed",
        "Memory usage increased",
        "New session created",
        "Queue processing delayed"
    ];

    return {
        id: uuidv4(),
        level: levels[Math.floor(Math.random() * levels.length)],
        message: messages[Math.floor(Math.random() * messages.length)],
        timestamp: new Date().toISOString()
    };
}
