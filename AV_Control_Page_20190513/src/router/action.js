import express from "express"
import db from "../service/database"
var router = express.Router({
  mergeParams: true
})

router.post("/", function(req, res) {
  try {
    let {action, pitch} = req.body;
    action.id = `action_${Date.now()}`
    action.date = Date.now();
    action.data = {
      time: 0,
      velocity: 200,
      pitch: pitch
    }
    db.get("actions").push(action).write();
    res.json({
      code: 0,
      data: db.get("actions").value()
    })
  } catch (error) {
    res.json({
      code: -99,
      message: error.message
    })
  }
})

router.put("/:id", function(req, res) {
  try {
    let {action, pitch} = req.body;
    let id = req.params.id;
    action.date = Date.now();
    action.data = {
      time: 0,
      velocity: 200,
      pitch: pitch
    }
    db.get("actions").find({id: id}).assign(action).write()
    res.json({
      code: 0,
      data: db.get("actions").value()
    })
  } catch (error) {
    res.json({
      code: -99,
      message: error.message
    })
  }
})

export default router;