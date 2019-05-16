import express from "express"
import order from "./order"
import action from "./action"
var router = express.Router()

router.use("/order", order)
router.use("/action", action)

export default router;