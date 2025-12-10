import { Router } from "express";

const router = Router();

const SEARCH_URL = process.env.SEARCH_URL || "http://localhost:8001/search";

router.get("/", async (req, res) => {
    try {
        const { q = "", top_k = 10 } = req.query;

        if (!q) {
            return res.status(400).json({ error: "q (query) is required" });
        }

        const searchRes = await fetch(SEARCH_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: q, top_k: Number(top_k) })
        });

        if (!searchRes.ok) {
            const text = await searchRes.text();
            console.error("Search error:", text);
            return res.status(500).json({ error: "Search service failed" });
        }

        const data = await searchRes.json();
        res.json(data);
    } catch (err) {
        console.error("Error in /logs:", err);
        res.status(500).json({ error: "Internal server error" });
    }
});

export default router;
