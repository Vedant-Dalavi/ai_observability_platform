import express from "express";
import cors from "cors";
import morgan from "morgan";
import ragRouter from "./routes/rag.js";
import logsRouter from "./routes/logs.js";
import servicesRouter from "./routes/services.js";
import eventsRouter from "./routes/events.js";


const app = express();

app.use(cors());
app.use(express.json());
app.use(morgan("dev"));

app.use("/events", eventsRouter);

app.get("/health", (req, res) => {
  res.json({ status: "ok", service: "api-nodejs" });
});

// Mount routers
app.use("/rag", ragRouter);
app.use("/logs", logsRouter);
app.use("/services", servicesRouter);

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`API Gateway running on http://localhost:${PORT}`);
});
