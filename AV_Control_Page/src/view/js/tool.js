function time_to_date_str(curDate){
  var Y = curDate.getFullYear() + '-';
  var M = (curDate.getMonth()+1 < 10 ? '0'+(curDate.getMonth()+1) : curDate.getMonth()+1) + '-';
  var D = curDate.getDate() + ' ';
  var hh = curDate.getHours() + ':';
  var mm = curDate.getMinutes() + ':';
  var ss = curDate.getSeconds();
  return Y + M + D + hh + mm + ss;
}

function time_to_sec(time) {
  var s = '';
  var hour = time.split(':')[0];
  var min = time.split(':')[1];
  var sec = time.split(':')[2];
  s = Number(hour*3600) + Number(min*60) + Number(sec);
  return s;
};