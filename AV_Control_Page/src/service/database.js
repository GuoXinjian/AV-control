import path from "path"
const low = require('lowdb');
const FileSync = require('lowdb/adapters/FileSync');  // 有多种适配器可选择
const adapter = new FileSync(path.join(__dirname, '../db.json')); // 申明一个适配器
const db = low(adapter);
db.defaults({ orders: [], subOrders: []})
  .write()
export default db;