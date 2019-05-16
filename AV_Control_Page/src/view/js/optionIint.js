const Type = {
  normal: 0,
  groupOrder: 1,
  subOrder: 2,
  action: 3,
}
var app = new Vue({
  el: "#app",
  data: {
    serverIP:"",
    name:"",
    description:"",
    curKey:"",
    selectOrder:{},
    selectGroupOrder: {},
    selectAction: {},
    orderList: [],
    actions:[],
    breadcrumbs: [],
    selectScreens: [],
    selectLamps: [],
    selectSounds: [],
    createModal: {
      visible: false,
      title: "添加命令",
      name: "",
      description: "",
      loading: false
    },
    type: Type.normal,
    addModal: {
      visible: false,
      id: 1,
      type: 1,
      date: '00:00:00'
    },
    screens: [],
    lamps: [],
    sounds: []
  },
  created(){
    this.loadData();
  },
  methods:{
    initData() {
      this.name = "";
      this.description = "";
      this.selectOrder = {};
      this.selectGroupOrder =  {};
      this.breadcrumbs =  [];
      this.type = Type.normal;
    },
    loadData(){
      axios.get("/api/order")
        .then(res => {
          const {code, data, message} = res.data;
          if (code !== 0) return this.$message.error(message); 
          this.actions = data.actions;
          this.actions[0].list = data.screens;
          this.actions[1].list = data.lamps;
          this.actions[2].list = data.sounds;
          this.screens = data.screens;
          this.lamps = data.lamps;
          this.sounds = data.sounds;
          this.orderList = data.orders;
        })
        .catch(error => {
          this.$message.error(error.message)
        })
    },
    handleOrder(group, item) {
      this.type=Type.subOrder;
      this.breadcrumbs = [group.name, item.name]
      this.description = item.description;
      this.name = item.name;
      this.selectOrder = item;
      this.selectGroupOrder = group;
      this.curKey = item.shortcutkey;
      this.formateSelectOrder(this.selectOrder.orderInfo);
    },
    handleMenuSelected(group, item) {
      this.breadcrumbs = [group.name, item.name]
      this.description = item.description;
      this.name = item.name;
      this.type = Type.action;
      this.selectAction = item;
    },
    handleGroupOrderClick(item) {
      this.type = Type.groupOrder;
      this.breadcrumbs = [item.name]
      this.name = item.name;
      this.description = item.description;
      this.selectGroupOrder = item;
    },
    addGroupOrderButtonClick() {
      this.type = Type.addGroupOrder;
      this.createModal = {
        visible: true,
        title: "添加命令组",
        name: "",
        description: "",
        loading: false,
        groupOrder: {}
      }
    },
    addOrderButtonClick() {
      this.createModal = {
        visible: true,
        title: "添加指令",
        name: "",
        description: "",
        loading: false,
        groupOrder: {}
      }
    },
    inputBlur() {
      if (this.type == Type.groupOrder) {
        this.selectGroupOrder.name = this.name;
        this.selectGroupOrder.description = this.description;
        axios.put('/api/order/group', {groupOrder: this.selectOrder}).then(res => {
          const {code, data, message} = res.data;
          if (code == 0) {
            this.orders = data.orders;
          } else {
            this.$message({
              message: message,
              type: 'error'
            });
          }
        }).catch(error => {
          this.$message.error(error.message)
        })
      } else if (this.type == Type.subOrder) {
        this.selectOrder.name = this.name;
        this.selectOrder.description = this.description;
        axios.put('/api/order', {order: this.selectOrder}).then(res => {
          const {code, data, message} = res.data;
          if (code == 0) {
            this.orders = data.orders;
          } else {
            this.$message({
              message: message,
              type: 'error'
            });
          }
        }).catch(error => {
          this.$message.error(error.message)
        })
      } else if (this.type == Type.action) {
        this.selectAction.name = this.name;
        this.selectAction.description = this.description;
        axios.put('/api/order/action', {action: this.selectAction}).then(res => {
          const {code, message} = res.data;
          if (code == 0) {
            this.loadData()
          } else {
            this.$message({
              message: message,
              type: 'error'
            });
          }
        }).catch(error => {
          this.$message.error(error.message)
        })
      }
    },
    keyboardChange(ev){
      var keyName = ev.key;
      var keyNo = ev.keyCode;
      if(this.curKey != keyName){
        this.$nextTick(() => {
          if(keyNo <= 90 && keyNo >= 48){
            this.curKey = keyName;
            if(this.type == Type.subOrder){
              var repeatNum = 0;
              for(var i = 0; i < this.orderList.length; i++){
                for(var j = 0; j < this.orderList[i]['subOrders'].length; j++){
                  if(keyNo == this.orderList[i]['subOrders'][j]['shortcutkeycode'] && this.selectOrder.id != this.orderList[i]['subOrders'][j]['id']){
                    repeatNum ++;
                  }
                }
              }
              // 如果没有重复的
              if(repeatNum == 0){
                this.selectOrder.shortcutkey = keyName;
                this.selectOrder.shortcutkeycode = keyNo;
                this.$message.success('快捷键设置成功')
                axios.put('/api/order', {order: this.selectOrder}).then(res => {
                  const {code, data, message} = res.data;
                  if (code == 0) {
                    this.orders = data.orders;
                  } else {
                    this.$message({
                      message: message,
                      type: 'error'
                    });
                  }
                })
              }else{
                this.curKey = "";
                this.$message({message: "快捷键已存在，请重新设置",type: 'error'});
              }
            }
          }else{ // 按键不是0~9或A~Z，就置空
            this.curKey = "";
            this.$message.error('按键无效，请将输入法调为英文，然后点击0~9或A~Z（不分大小写）重新设置');
            this.selectOrder.shortcutkey = "";
            this.selectOrder.shortcutkeycode = "";
            axios.put('/api/order', {order: this.selectOrder}).then(res => {
              const {code, data, message} = res.data;
              if (code == 0) {
                this.orders = data.orders;
              } else {
                this.$message({
                  message: message,
                  type: 'error'
                });
              }
            })
          }
        });
      }else{
        this.curKey = keyName;
      }
    },
    addAction() {
      let orderInfo = this.selectOrder.orderInfo.find(item => item.date == this.addModal.date)
      if (orderInfo) {
        orderInfo.detail.push({
          type: this.addModal.type,
          id: this.addModal.id
        });
      } else {
        this.selectOrder.orderInfo.push({
          "date": this.addModal.date,
          "detail": [{
            type: this.addModal.type,
            id: this.addModal.id
          }]
        })
      }
      this.selectOrder.orderInfo = this.selectOrder.orderInfo.sort((r1, r2) => {
        let rd1 = this.getTimestamp(r1.date);
        let rd2 = this.getTimestamp(r2.date);
        return rd1 > rd2 ? 1 : rd1 == rd2 ? 0 : -1;
      })
      
      axios.put('/api/order', {
        order: this.selectOrder
      }).then(res => {
        const {code, data, message} = res.data;
        if (code == 0) {
          this.orders = data.orders;
          this.selectOrder = data.updateSubOrder;
          this.formateSelectOrder(this.selectOrder.orderInfo);
          this.addModal.visible = false;
        } else {
          this.$message.error(message);
        }
      }).catch(error => {
        this.$message.error(error.message)
      })
    },
    handleDeleteOrderOption(timeDate, item) {
      this.selectOrder.orderInfo = this.selectOrder.orderInfo.map((time) => {
        if(timeDate.date == time.date) {
          time.detail = time.detail.filter(action => !(action.id == item.id && item.type == action.type));
        }
        return time;
      }).filter(item => !!item.detail.length)
      axios.put('/api/order', {
        order: this.selectOrder
      }).then(res => {
        const {code, data, message} = res.data;
        if (code == 0) {
          this.orders = data.orders;
          this.selectOrder = data.updateSubOrder;
          this.formateSelectOrder(this.selectOrder.orderInfo);
          this.addModal.visible = false;
        } else {
          this.$message({
            message: message,
            type: 'error'
          });
        }
      }).catch(error => {
        this.$message.error(error.message)
      })
      
    },
    getTimestamp(time) {
      const times = time.split(":");
      return parseInt(times[0]) * 3600 + parseInt(times[1]) * 60 + parseInt(times[2]);
    },
    formateSelectOrder(orderInfo) {
      this.selectLamps = [];
      this.selectScreens = [];
      this.selectSounds = [];
      orderInfo.forEach(item => {
        let screens = item.detail.filter(action => action.type == 1);
        if (screens.length) {
          this.selectScreens.push({
            date: item.date,
            detail: screens
          })
        } 
        let lamps = item.detail.filter(action => action.type == 2);
        if (lamps.length) {
          this.selectLamps.push({
            date: item.date,
            detail: lamps
          })
        } 
        let sounds = item.detail.filter(action => action.type == 3);
        if (sounds.length) {
          this.selectSounds.push({
            date: item.date,
            detail: sounds
          })
        } 
      });
    },
    addButtonClick() {
      if (this.type == Type.groupOrder) {
        this.addOrderButtonClick();
      } else {
        this.addModal = {
          visible: true,
          id: 1,
          type: 1,
          date: '00:00:00'
        }
      }
    },
    deleteButtonClick() {
      if (this.type == Type.groupOrder) {
        axios.delete("/api/order/group", {
          data: {
            groupOrderId: this.selectGroupOrder.id
          }
        }).then(res => {
          const {code, data, message} = res.data;
          if (code !== 0) return this.$message.error(message);
          this.initData();
          this.orderList = data;
        })
        .catch(error => {
          this.$message.error(error.message)
        })
      } else {
        axios.delete("/api/order", {
          data: {
            groupOrderId: this.selectGroupOrder.id,
            orderId: this.selectOrder.id
          }
        }).then(res => {
          const {code, data, message} = res.data;
          if (code !== 0) return this.$message.error('删除失败');
          this.initData();
          this.orderList = data;
        }).catch(error => {
          this.$message.error(error.message)
        })
      }
    },
    modalAddButtonClick() {
      if (this.type == Type.groupOrder) {
        this.addOrder();
      } else {
        this.addGroupOrder();
      }
    },
    addGroupOrder() {
      if (!this.createModal.name.length) {
        return this.$message.warning("请输入名称");
      }
      axios.post("/api/order/group", {
        order: {
          name: this.createModal.name,
          description: this.createModal.description
        }
      }).then(res => {
        let {code, data} = res.data;
        if (code !== 0) return this.$message.error("添加失败")
        this.orderList = data;
        this.createModal.visible = false;
      })
    },
    addOrder() {
      if (!this.createModal.name.length) {
        return this.$message.warning("请输入名称");
      }
      axios.post(`/api/order`, {
        groupOrderId: this.selectGroupOrder.id,
        order: {
          name: this.createModal.name,
          description: this.createModal.description
        }
      }).then(res => {
        let {code, data} = res.data;
        if (code !== 0) return this.$message.error("添加失败")
        this.orderList = data;
        this.createModal.visible = false;
      })
    },
    handlePublishOrder() {
      if (this.type == Type.subOrder && !this.selectOrder.orderInfo.length) return this.$message.error("当前操作项为空，请点击上方已添加的指令按钮再发送！");
      if(this.serverIP == "") return this.$message.error("请先输入服务器IP:端口号再发送指令！");
      let publishData = {};
      if (this.type == Type.subOrder) {
        let list = [];
        for (let i = 0; i < this.selectOrder.orderInfo.length; i++) {
          const info = this.selectOrder.orderInfo[i];
          const details = info.detail.map(item => {
            return {
              data: item.data,
              id: item.id,
              type: item.type
            }
          })
          list = list.concat(details);
          if (i + 1 < this.selectOrder.orderInfo.length) {
            const nextInfo = this.selectOrder.orderInfo[i + 1];
            const interval = this.getTimestamp(nextInfo.date) - this.getTimestamp(info.date);
            list.push({type: 0, id: 0, data:{time: interval}});
          }
        }
        publishData = {
          ...this.selectOrder,
          orderInfo: list
        }
      } else if (this.type == Type.action) {
        publishData = {
          id: this.selectAction.id,
          name: this.selectAction.name,
          orderInfo: [{
            data: this.selectAction.data,
            id: this.selectAction.id,
            type: this.selectAction.type
          }]
        }
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
      // console.log(resPublishData)
      // console.log(publishData)
      axios({
        method: "post",
        url: "http://"+this.serverIP+"/",
        params: resPublishData
      }).then(res => {
        this.$message.success("发送成功");
      })
    },
  }
});
