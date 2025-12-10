import { Router } from "express";

const router = Router();

// Change if rag-orchestrator runs on different host/port
const RAG_URL = process.env.RAG_URL || "http://localhost:8002/rag/query";

router.post("/query", async (req, res) => {
    try {
        const { query } = req.body;

        if (!query) {
            return res.status(400).json({ error: "query is required" });
        }

        const ragRes = await fetch(RAG_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query })
        });

        if (!ragRes.ok) {
            const text = await ragRes.text();
            console.error("RAG error:", text);
            return res.status(500).json({ error: "RAG service failed" });
        }

        const data = await ragRes.json();
        res.json(data);
    } catch (err) {
        console.error("Error in /rag/query:", err);
        res.status(500).json({ error: "Internal server error" });
    }
});

export default router;
