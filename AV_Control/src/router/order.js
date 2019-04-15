import express from "express"
import db from "../service/database"
var router = express.Router()

router.post("/",function(req, res){
  try{
    let {order} = req.body;
    order.id = `order_${Date.now()}`
    
    db.get("orders").push(order).write()
    res.json({
      code: 0,
      data: db.get("orders").value()
    })
  } catch(error){
    res.json({
      code: -99,
      message: error.message
    })
  }
});

router.put("/",function(req, res){
  const {order} = req.body;
  try{
    db.get("orders").find({id : order.id}).assign(order).write()
    res.json({
      code: 0,
      data: db.get("orders")
    })
  }catch(error){
    res.json({
      code: -99,
      message: error.message
    })
  }
});

router.delete("/",function(req,res){
  const {orderId} = req.body;
  try{
    db.get("orders").remove({ id: orderId}).write();
    res.json({
      code: 0,
      data: db.get("orders")
    })
  }catch(error){
    res.json({
      code: -99,
      message: error.message
    })
  }
});

router.get("/",function(req,res){
  res.json({
    code: 0,
    data: db.get("orders")
  })
});

export default router;