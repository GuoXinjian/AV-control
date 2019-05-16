import time
from multiprocessing import Process,Queue
import pygame

pygame.mixer.init()
now=0
def play(q):
    global now
    while 1:
        
        print(now)
        nextmusic = q.get(True)
        print(nextmusic)
        if nextmusic!=now:
            print(nextmusic)
            try:
                print('load')
                pygame.mixer.music.load('%s.mp3'%nextmusic)
            except:
                pygame.mixer.music.stop()
                continue
            now=nextmusic
        if pygame.mixer.music.get_busy()==False:
            print('play')
            pygame.mixer.music.play()


if __name__=='__main__':
    q=Queue()
    # pw=Process(target=get,args=(q,))
    pr=Process(target=play,args=(q,))
    # pw.start()
    pr.start()
    while 1:
        nextmusic=input('输入歌曲编号')
        q.put(nextmusic)
    # pw.join()
    pr.terminate()