import { Router } from "express";

const router = Router();

// For now, hardcode or later load from config / DB
const services = [
  { name: "auth-service", description: "Handles authentication" },
  { name: "payment-service", description: "Payment flow" },
  { name: "order-service", description: "Order processing" },
  { name: "user-service", description: "User profiles" }
];

router.get("/", (req, res) => {
  res.json({ services });
});

export default router;
