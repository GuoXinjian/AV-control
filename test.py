#!/usr/bin/python
#-*-  coding:utf-8 -*-
from flask import Flask,request
import json
import time
import threading
import midi
import midi.sequencer as sequencer
import pygame
import os
from multiprocessing import Process, Queue

hardware = sequencer.SequencerHardware()
screen = sequencer.SequencerWrite(sequencer_resolution=220)
screen.subscribe_port(20, 0)
screen.start_sequencer()
light = sequencer.SequencerWrite(sequencer_resolution=220)
light.subscribe_port(24, 0)
light.start_sequencer()
app=Flask(__name__)



Qvolume=Queue()
Qmusicid=Queue()


t=0
nowmusic=0
nowvolume=1
def play(Qvolume,Qmusicid):
    global t,nowmusic,nowvolume
    pygame.mixer.init()
    while True:
        nextmusic=Qmusicid.get(True)       
        nextvolume=Qvolume.get(True)
        print(nextmusic,nextvolume)
        pygame.mixer.music.set_volume(nextvolume)
        if nextmusic==0:
            try:
                print('music pause')
                pygame.mixer.music.pause()
                print(nowmusic)
            except:
                continue
        elif nextmusic==-1:
            try:
                print('music resume')
                pygame.mixer.music.unpause()
                print(nowmusic)      
            except:
                continue  
        elif nextvolume!=nowvolume:
            pygame.mixer.music.set_volume(nextvolume)
            nowvolume=nextvolume
            print('volume ok')
        if nextmusic!=0 and nextmusic!=-1 and nextmusic!=nowmusic:
            try:
                pygame.mixer.music.load('%s.mp3'%nextmusic)
                print('load music ok')
            except:
                print('music stop')
                pygame.mixer.music.stop()
                continue
            nowmusic=nextmusic
        if pygame.mixer.music.get_busy()==False:
            print('music play')
            pygame.mixer.music.play()

        # pygame.mixer.music.load('1.mp3')

        
        if pygame.mixer.music.get_busy()==False:
            pygame.mixer.music.play()


@app.route('/',methods=['GET','POST'])
def index(): 
    if request.method   == 'GET':
        return '<p>Welcom VSPN AV-control System</p><p>By Guoxinjian</p>'
    elif request.method == 'POST':
        alldata=request.args.to_dict()#.encode(encoding='utf-8')
        
        datalist=json.loads(alldata['orderInfo'])
        print(datalist)
        for i in range(len(datalist)):
            print(i)
            typeid = datalist['%s'%i]['type']
            print(typeid)
            data=datalist['%s'%i]['data']
            sleep=data['time']
            time.sleep(sleep)
            if sleep:
                print(i,sleep)
                continue
            else:
                pitch=data['pitch']
                velocity=data['velocity']
                print(i,typeid,pitch,velocity)
                
                event=midi.NoteOnEvent(tick=0,pitch=pitch,velocity=velocity)
                print('ok')
                if typeid=='1':
                    screen.event_write(event, False, False, True)
                elif typeid=='3':
                    light.event_write(event, False, False, True)
                elif typeid=='5':
                    Qmusicid.put(pitch)
                    Qvolume.put(velocity/100)
                elif typeid=='6':
                    Qvolume.put(velocity/100)

        return 'ok'
def mainstart(app,Qvolume,Qmusicid):
    app.run('0.0.0.0',5000)



if __name__=='__main__':
    
    pm=Process(target=play,args=(Qvolume,Qmusicid,))
    # pf=Process(target=mainstart,args=(app,Qvolume,Qmusicid,))
    pm.start()
    app.run('0.0.0.0',5000)
    # pf.start()
    