// var [get_team_list_url,post_player_id_url] = ['/api/teamlist',window.location.href];
var [get_team_list_url,post_player_id_url] = [window.location.href+'playerlist',window.location.href];

$(function(){
  $('select').chosen();
});

var [team_info_list,post_player_info] = [[],{team1:[],team2:[]}];
$.get({
  url: get_team_list_url
}).then(function (res) {
  var res_data = res.data;
  team_info_list = res_data.map(item => {
    return item;
  });
  var team_options = '';
  res_data.forEach(team => {
    team_options += '<option value="'+team['teamId']+'">'+team['teamName']+'</option>';
  });
  $(".set-team").html(team_options);
  $(".set-team").removeAttr('disabled');
  $(".set-team").trigger("liszt:updated");
  setTeam(1)
  setTeam(2);
});

var setTeam = (t_idx) => {
  var t_id = parseInt($('#set-t'+t_idx).val());
  var t_p_list = getPlayerListByTeamId(t_id);
  var player_options = '';
  t_p_list.forEach(p => {
    player_options+='<option value="'+p.playerId+'">'+ p.playerNick +'</option>';
  });
  $('.t'+t_idx).each(function(index){
    $(this).html(player_options);
    this.selectedIndex = index;
    $(this).removeAttr('disabled');
    $(this).trigger("liszt:updated");
    var p_selector_idx = t_idx === 1 ? (index+1) : (index+6);
    setPlayer(p_selector_idx);
  });
};

var getPlayerListByTeamId = (team_id) => {
  var res_list = [];
  team_info_list.forEach(team => {
    if(team_id === team.teamId){
      res_list = team.teamPlayers;
    }
  });
  return res_list;
};

var setPlayer = (p_idx) => {
  var t_key = p_idx < 6 ? 'team1' : 'team2';
  var p_list_index = p_idx < 6 ? (p_idx-1) : (p_idx-6);
  post_player_info[t_key][p_list_index] = $('#set-p'+p_idx).find("option:selected").text();
};

var sendPlayerId = () => {
  if(checkTeamAndPlayer() == false){alert('队伍选择重复！或！选手重复！');}
  else{$.post(post_player_id_url,{data : post_player_info});}
};

var checkTeamAndPlayer = () => {
  var check_state = 0;
  if($('#set-t1').val() === $('#set-t2').val() || isRepeat(post_player_info.team1) == true || isRepeat(post_player_info.team2) == true){
    check_state ++;
  }
  return check_state == 0 ? true : false;
};

var isRepeat = (arr) => {
  let  hash = {};
  for(let i in arr) {
    if(hash[arr[i]]) {return true;}
    hash[arr[i]] = true;
  }
  return false;
};