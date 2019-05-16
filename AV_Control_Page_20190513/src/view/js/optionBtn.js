var app = new Vue({
  el: "#app",
  data: {
    orderList: [],
    serverIP: ""
  },
  created(){
    this.loadData();
  },
  methods:{
    loadData(){
      axios.get("/api/order")
        .then(res => {
          const {code, data, message} = res.data;
          if (code !== 0) return this.$message.error(message); 
          this.orderList = data.orders;
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    },
    getTimestamp(time) {
      const times = time.split(":");
      return parseInt(times[0]) * 3600 + parseInt(times[1]) * 60 + parseInt(times[2]);
    },
    handlePublishOrder(order) {
      if(this.serverIP == "") return this.$message.error("请先输入服务器IP:端口号再发送指令！");
      let list = [];
      for (let i = 0; i < order.orderInfo.length; i++) {
        const info = order.orderInfo[i];
        const details = info.detail.map(item => {
          return {
            data: item.data,
            id: item.id,
            type: item.type
          }
        })
        list = list.concat(details);
        if (i + 1 < order.orderInfo.length) {
          const nextInfo = order.orderInfo[i + 1];
          const interval = this.getTimestamp(nextInfo.date) - this.getTimestamp(info.date);
          list.push({type: 0, id: 0, data:{time: interval}});
        }
      }
      let publishData = {
        ...order,
        orderInfo: list
      }
      
      var resOrderInfo = new Object();
      for(let idx = 0; idx < publishData.orderInfo.length; idx++){
        var paramName = idx + '';
        resOrderInfo[paramName] = publishData.orderInfo[idx];
      }
      var resPublishData = {
        id: publishData.id,
        name: publishData.name,
        orderInfo: resOrderInfo
      }
      axios({
        method: "post",
        url: "http://"+this.serverIP+"/",
        params: resPublishData
      }).then(res => {
        this.$message.success("发送成功");
      })
    }
  }
});