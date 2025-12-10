import { Router } from "express";

const router = Router();

router.get("/live", (req, res) => {
  res.setHeader("Content-Type", "text/event-stream");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");

  const interval = setInterval(() => {
    const event = {
      service: "auth-service",
      level: "info",
      message: "Ping from SSE demo",
      timestamp: Date.now()
    };

    res.write(`data: ${JSON.stringify(event)}\n\n`);
  }, 2000);

  req.on("close", () => {
    clearInterval(interval);
  });
});

export default router;
