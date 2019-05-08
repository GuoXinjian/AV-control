import express from "express"
import order from "./order"
var router = express.Router()

router.use("/order", order)

export default router;