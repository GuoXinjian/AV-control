'''服务端（UDP协议局域网广播）'''
 
import socket,struct
import time
class ArtNetToDMX512():
    def __init__(self, ip='<broadcast>',port=6454):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
 
        nRcvBufferLen = 64 * 1024;
 
        nSndBufferLen = 4 * 1024 * 1024;
 
        #nLen = sizeof(int);
 
        #self.s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,4 * 1024 * 1024*128)
        #self.s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4 * 1024 * 1024*128)
        #setsockopt(socket, SOL_SOCKET, SO_RCVBUF, (char *) & nRcvBufferLen, nLen);
        #self.s.setsockopt(socket, SOL_SOCKET, SO_SNDBUF, (char *) & nSndBufferLen, nLen);
        self.PORT = port
        self.network = ip
        #self.pixStyle=pix_style&0x0f
        #self.grb=grb
        #self.s.sendto('Client broadcast message!'.encode('utf-8'), (network, PORT))
    def formatDMXdata(self,dvcid,dat):
        #print(dat)
        sendBuf=[0x41, 0x72, 0x74, 0x2D, 0x4E, 0x65, 0x74, 0x00, 0x00, 0x50, 0x00, 0x0E, 0x77, 0x01]
 
        #sendBuf[14]设备节点
        #sendBuf[15] = 0x00;
        sendBuf.append(dvcid& 0xff)
        sendBuf.append(0x00)
 
        # 发送的字节数 512
        #sendBuf[16] = 0x02;
        #sendBuf[17] = 0x00;
        datlen = len(dat)
        #sendBuf.append((datlen & 0xff00) >> 8)
        sendBuf.append(0x02)
        #sendBuf.append(datlen & 0xff)
        sendBuf.append(0x00)
        # 发送的数据
        #sendBuf[17+n] = 0x00;
        #print( datlen)
        datlen=512
        for x in range(512):
            sendBuf.append( 0x00)
        #datlen = len(dat)
        #print(datlen)
        #print(dat[x])
        '''if(self.grb==1):
            for x in range(int(len(dat)/self.pixStyle)):
                r=dat[x*self.pixStyle]& 0xff
                g = dat[x * self.pixStyle+1]& 0xff
                b = dat[x * self.pixStyle+2]& 0xff
                sendBuf[17+x * self.pixStyle]=g
                sendBuf[17 + x * self.pixStyle+1] = r
                sendBuf[17 + x * self.pixStyle+2] = b
        else:
            for x in range(len(dat)):
                sendBuf[17+x]=(dat[x] & 0xff)'''
        for x in range(len(dat)):
            sendBuf[17+x]=(dat[x] & 0xff)
            #sendBuf.append((dat[x] & 0xff))#.to_bytes(1,'big')
        #data = [1, 2, 3]
        #buffer = struct.pack("!ihb", *data)
 
        packstyle=str(18+datlen)+'B'#B 0-255
        #req = struct.pack('14b',*sendBuf) 0-127
        req = struct.pack(packstyle, *sendBuf)
        #print(req)
        return req
    def senddata(self,dvcid,dat):
        #print(dat)
        #print(len(dat))
        #print(self.network,self.PORT)
        self.s.sendto(self.formatDMXdata(dvcid,dat), (self.network, self.PORT))
        #time.sleep(0.5)
 
class ArtNetDevices():
 
    def __init__(self, ips):
        datlen = len(ips)
        self.deviceList=[]
        for x in range(datlen):
            self.deviceList.append(ArtNetToDMX512(ips[x],port=6454))
    def splitData(self,data,sidx=0,eidx=0):
        b= eidx<=len(data) and sidx>=0 and eidx-sidx>0
        if(b):
            d= data[sidx:eidx]
            return b,d
        return False,[]
    def sendFrameData(self,data,pixstyle=4,width=45,height=15):
        datlen = len(self.deviceList)
        #一个设备有4个节点号
        c=0
        u=pixstyle*width
        #print(u)
        for x in range(datlen):#每个设备4个节点
 
            #获取切割的数据，发送到对应的节点
            b,d= self.splitData(data,c * u, (c + 1) * u)
            #print(c, c * u, (c + 1) * u,b,d)
            if b:
                self.deviceList[x].senddata(0,d)#节点接口1
            c+=1
 
            b, d = self.splitData(data, c * u, (c + 1) * u)
            #print(c, c * u, (c + 1) * u, b, d)
            if b:
                self.deviceList[x].senddata(1, d)#节点接口2
                pass
            c += 1
 
            b, d = self.splitData(data, c * u, (c + 1) * u)
            #print(c, c * u, (c + 1) * u, b, d)
            if b:
                self.deviceList[x].senddata(2, d)#节点接口3
                pass
            c += 1
 
            b, d = self.splitData(data, c * u, (c + 1) * u)
            #print(c, c * u, (c + 1) * u, b, d)
            if b:
                self.deviceList[x].senddata(3, d)#节点接口4
                pass
            c += 1
 
 
 
if __name__ == '__main__':
    c=0
    dvcs=ArtNetDevices(["192.168.1.8"])
    d = [200, 1, 2, 3, 4, 5, 6, 7,200]
    d = []
    #d = [0 for i in range(512)]
    for i in range(2700):
        d.append(i % 256)
    import time
 
    #dmx=ArtNetToDMX512("192.168.1.8")
    while True:
        c=c+1
        print(c)
        #dmx.senddata(0,[255,255,255])
        dvcs.sendFrameData(d,3,45)
        #s.sendto(pack(), (network, PORT))
        time.sleep(1)
