import path from "path"
import router from "./src/router"
const express = require('express');
const bodyParser = require('body-parser');
var request = require('request');

const hostname = 'localhost';
const port = 3001;
var app = express();

app.use(bodyParser.json());//定义数据解析器
app.use(bodyParser.urlencoded({extended: true}));//定义url编码方式，

app.use('/view', express.static(path.join(__dirname, './src/view') ))
app.use('/images', express.static(path.join(__dirname, './src/images')))
app.use(bodyParser.urlencoded({ extended: false }));
app.use('/api', router);
app.use('/AV_Control', express.static(path.join(__dirname, './')));


app.listen(port, () => {
  console.log(`服务运行在 http://${hostname}:${port}/`);
});