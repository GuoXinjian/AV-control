function getTimestamp(time) {
  const times = time.split(":");
  return parseInt(times[0]) * 3600 + parseInt(times[1]) * 60 + parseInt(times[2]);
}
$(document).keydown(function(e){
  var curFocusDomTag = document.activeElement.tagName;
  if(curFocusDomTag != "TEXTAREA" && curFocusDomTag != "INPUT"){
    $.ajax({
      url: "/api/order",
      type: "get",
      async: true,
      dataType: "json",
      success: function(res){
        var all_order_list = res.data.orders;
        $(all_order_list).each(function(){
          $(this['subOrders']).each(function(){
            if(e.keyCode == this['shortcutkeycode']){
              let list = [];
              for (let i = 0; i < this.orderInfo.length; i++) {
                const info = this.orderInfo[i];
                const details = info.detail.map(item => {
                  return {
                    data: item.data,
                    id: item.id,
                    type: item.type
                  }
                })
                list = list.concat(details);
                if (i + 1 < this.orderInfo.length) {
                  const nextInfo = this.orderInfo[i + 1];
                  const interval = getTimestamp(nextInfo.date) - getTimestamp(info.date);
                  list.push({type: 0, id: 0, data:{time: interval}});
                }
              }
              const publishData = {
                ...this,
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
              var cur_ip_val = $('#ipInput').val();
              if(cur_ip_val.length > 0){
                // console.log('当前指令：',resPublishData.name,'内容：',resPublishData)
                axios({
                  method: "post",
                  url: "http://"+cur_ip_val+"/",
                  params: resPublishData
                })
              }else{
                alert("请先输入IP，再发送指令");
              }
            }
          });
        });
      },
      error:function (error) {
        console.log(error);
      }
    });
  }
});