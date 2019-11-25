import requests
from flask import Flask,render_template,request,jsonify,redirect,url_for
import json,threading,time
import mido


herodict={
    105:41,
    106:75,
    107:89,
    108:54,
    109:13,
    110:83,
    111:67,
    112:45,
    113:96,
    114:44,
    115:22,
    116:1,
    117:92,
    118:65,
    119:6,
    120:3,
    121:52,
    123:47,
    124:93,
    126:73,
    127:90,
    128:9,
    129:17,
    130:23,
    131:38,
    132:49,
    133:16,
    134:14,
    135:74,
    136:71,
    139:37,
    140:25,
    141:18,
    142:2,
    144:12,
    146:46,
    148:32,
    149:42,
    150:27,
    152:70,
    153:36,
    154:29,
    156:88,
    157:7,
    162:55,
    163:33,
    166:77,
    167:68,
    168:57,
    169:28,
    170:43,
    171:87,
    173:40,
    174:84,
    175:91,
    177:11,
    178:78,
    183:76,
    184:8,
    186:69,
    180:56,
    190:95,
    192:30,
    191:15,
    187:19,
    182:21,
    189:26,
    193:34,
    196:3,
    195:4,
    194:64,
    198:50,
    179:58,
    501:53,
    199:24,
    176:79,
    502:60,
    197:82,
    503:35,
    504:51,
    125:85,
    510:66,
    137:63,
    509:20,
    508:31,
    312:62,
    507:39,
    513:61,
    515:10,
    511:94,
    529:59,
    505:81,
    506:86,
    522:80,
    518:48,
    523:72

}

app=Flask(__name__)

channels=[]
@app.route('/', methods=['GET', 'POST'])
def index():
    global channels
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data=request.form.to_dict(flat=False)
        # print(data)
        channels=[]
        for key, value in data.items():
            for v in value:
                channels.append(v)
        # print(channels)
        return 'ok'

@app.route('/playerlist')
def teamlist():
    data=requests.get('http://120.27.151.217/api/teamlist').json() 
    # print(data)
    return jsonify(data)

def sendMsg():
    global channels
    print(channels)
    port=mido.open_output('USB MIDI Interface 1')
    while True: 
        if channels:
            data=requests.get('http://120.27.151.217/avcontrol',timeout=5).json()
            print(data)
            for i in range(len(data['data'])):
                print(data['data'][channels[i]])
                msg=mido.Message('note_on',channel=i,note=herodict[data['data'][channels[i]]])
                port.send(msg)
            if len(data['data'])==10:
                channels=[]
        time.sleep(2)

if __name__ == '__main__':
    # data=requests.get('http://120.27.151.217/avcontrol',timeout=5).json()
    # print(len(data['data']))
    # print(len(herodict))
    t1=threading.Thread(target=app.run)
    t2=threading.Thread(target=sendMsg)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
