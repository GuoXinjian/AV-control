import express from "express"
import db from "../service/database"
var router = express.Router()

router.post("/group", function(req, res) {
  try {
    let {order} = req.body;
    order.id = `group_order_${Date.now()}`
    order.date = Date.now();
    order.subOrders = [];
    db.get("orders").push(order).write();
    res.json({
      code: 0,
      data: getGroupOrders()
    })
  } catch (error) {
    res.json({
      code: -99,
      message: error.message
    })
  }
})

router.post("/",function(req, res){
  try{
    let {order, groupOrderId} = req.body;
    order.id = `order_${Date.now()}`
    order.date = Date.now();
    order.orderInfo = [];
    db.get('subOrders').push(order).write();
    db.get("orders").find({id: groupOrderId}).get("subOrders").push({id: order.id}).write()
    res.json({
      code: 0,
      data: getGroupOrders()
    })
  } catch(error){
    res.json({
      code: -99,
      message: error.message
    })
  }
});

router.put("/group",function(req, res){
  const {groupOrder} = req.body;
  try{
    db.get("orders").find({id : groupOrder.id}).assign(groupOrder).write()
    res.json({
      code: 0,
      data: {
        orders: getGroupOrders()
      }
    })
  }catch(error){
    res.json({
      code: -99,
      message: error.message
    })
  }
});

router.put("/",function(req, res){
  const {order} = req.body;
  try{
    db.get("subOrders").find({id : order.id}).assign(order).write()
    res.json({
      code: 0,
      data: {
        updateSubOrder: getSubOrder(order.id),
        orders: getGroupOrders()
      }
    })
  }catch(error){
    res.json({
      code: -99,
      message: error.message
    })
  }
});

router.delete("/group",function(req,res){
  const {groupOrderId} = req.body;
  try{
    const groupOrder = db.get("orders").find({id: groupOrderId}).value();
    groupOrder.subOrders.map(item => {
      db.get("subOrders").remove(item).write();
    })
    db.get("orders").remove({ id: groupOrderId}).write();
    res.json({
      code: 0,
      data: getGroupOrders()
    })
  }catch(error){
    res.json({
      code: -99,
      message: error.message
    })
  }
});

router.delete("/",function(req,res){
  const {orderId, groupOrderId} = req.body;
  try{
    db.get("orders").find({ id: groupOrderId}).get("subOrders").remove({id: orderId}).write();
    db.get("subOrders").remove({ id: orderId}).write();
    res.json({
      code: 0,
      data: getGroupOrders()
    })
  }catch(error){
    res.json({
      code: -99,
      message: error.message
    })
  }
});

router.get("/",function(req,res){
  try {
    res.json({
      code: 0,
      data: {
        orders: getGroupOrders(),
        actions: db.get("actions").value(),
        menuAction: db.get("menuAction").value(),
      }
    })
  } catch (error) {
    res.json({
      code: -99,
      message: error.message
    })
  }
});

router.put("/action", function(req, res) {
  try {
    const action = req.body.action;
    let key = "";
    if (action.type == 1) {
      key = "screens";
    } else if(action.type == 2) {
      key = "lamps";
    } else if(action.type == 3) {
      key = "sounds";
    }
    db.get(key).find({id: action.id}).assign(action).write();
    res.json({
      code: 0
    })
  } catch (error) {
    res.json({
      code: -99,
      message: error.message
    })
  }
})

function getGroupOrders() {
  var groupOrders = db.get("orders").cloneDeep().value();
  return groupOrders.map(group => {
    group.subOrders = group.subOrders.map(item => {
      return getSubOrder(item.id)
    })
    return group;
  })
}

function getSubOrder(id) {
  let subOrder = db.get("subOrders").find({id: id}).cloneDeep().value();
  subOrder.orderInfo = subOrder.orderInfo.map(order => {
    order.detail = order.detail.map(item => {
      let action =  db.get("actions").find({id: item.id}).cloneDeep().value();
      action.data.velocity = item.velocity
      return action;
    })
    return order;
  })
  return subOrder;
}

export default router;