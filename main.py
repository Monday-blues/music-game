from playsound import playsound
import random
from ursina import *
import time
import wave
import winsound

app = Ursina()


window.borderless = False
window.color = color._20


#Text.default_font = "c:/Windows/Fonts/malgunbd.ttf"


music = "none"
choose = 0

music_text = Text(text=str(music), x=-0, y=0.3, scale=2, background=False)
button1 = Button(text="Next", color=color.pink, x=-0.6, scale=0.2)      
button2 = Button(text="Answer", color=color.pink, scale=0.2)
button3 = Button(text="Replay", color=color.pink, x=0.6, scale=0.2)
button4 = Button(text="Resume", color=color.blue, x=0.6, y=0.3, scale=0.2)

sky = Entity(
    parent=scene,
    model='sphere',
    texture=load_texture('sky.jpg'),
    scale=100,
    double_sided=True
)

loop = 0
choose1 = 0
choose2 = 0
choose3 = 0
choose4 = 0
choose5 = 0
choose6 = 0
choose7 = 0
choose8 = 0
choose9 = 0
choose10 = 0
choose11 = 0
choose12 = 0
choose13 = 0
choose14 = 0
choose = 0

def button_click_next():
    print("button_clicked")
    rps()

def button_click_open_answer():
    print("show answer")
    rpsupdate()
    button1.scale = 0
    button2.scale = 0
    button3.scale = 0
    music = ""
    
    
    global choose
    
    if choose == 1:
        winsound.PlaySound(m1, winsound.SND_ASYNC)
        print("replay number 1's music")
    if choose == 2:
        winsound.PlaySound(m2, winsound.SND_ASYNC)
        print("replay number 2's music")
    if choose == 3:
        winsound.PlaySound(m3, winsound.SND_ASYNC)
        print("replay number 3's music")
    if choose == 4:
        winsound.PlaySound(m4, winsound.SND_ASYNC)
        print("replay number 4's music")
    if choose == 5:
        winsound.PlaySound(m5, winsound.SND_ASYNC)
        print("replay number 5's music")
    if choose == 6:
        winsound.PlaySound(m6, winsound.SND_ASYNC)
        print("replay number 6's music")
    if choose == 7:
        winsound.PlaySound(m7, winsound.SND_ASYNC)
        print("replay number 7's music")
    if choose == 8:
        winsound.PlaySound(m8, winsound.SND_ASYNC)
        print("replay number 8's music")
    if choose == 9:
        winsound.PlaySound(m9, winsound.SND_ASYNC)
        print("replay number 9's music")
    if choose == 10:
        winsound.PlaySound(m10, winsound.SND_ASYNC)
        print("replay number 10's music")
    if choose == 11:
        winsound.PlaySound(m11, winsound.SND_ASYNC)
        print("replay number 11's music")
    if choose == 12:
        winsound.PlaySound(m12, winsound.SND_ASYNC)
        print("replay number 12's music")
    if choose == 13:
        winsound.PlaySound(m13, winsound.SND_ASYNC)
        print("replay number 13's music")
    if choose == 14:
        winsound.PlaySound(m14, winsound.SND_ASYNC)
        print("replay number 14's music")
    
def button_click_replay():
    print("replay")
    rpl()
    
def button_click_resume():
    print("resume music")
    button1.scale = 0.2
    button2.scale = 0.2
    button3.scale = 0.2
    winsound.PlaySound(None, winsound.SND_PURGE)
    global music
    music = ""
    rpsupdate()
    
m1=('resource/1-01.wav')
m2=('resource/1-02.wav')
m3=('resource/1-03.wav')
m4=('resource/1-04.wav')
m5=('resource/1-05.wav')
m6=('resource/1-06.wav')
m7=('resource/1-07.wav')
m8=('resource/1-08.wav')
m9=('resource/1-09.wav')
m10=('resource/1-10.wav')
m11=('resource/1-11.wav')
m12=('resource/1-12.wav')
m13=('resource/1-13.wav')
m14=('resource/1-14.wav')



m1s=('resource/1-01s.wav')
m2s=('resource/1-02s.wav')
m3s=('resource/1-03s.wav')
m4s=('resource/1-04s.wav')
m5s=('resource/1-05s.wav')
m6s=('resource/1-06s.wav')
m7s=('resource/1-07s.wav')
m8s=('resource/1-08s.wav')
m9s=('resource/1-09s.wav')
m10s=('resource/1-10s.wav')
m11s=('resource/1-11s.wav')
m12s=('resource/1-12s.wav')
m13s=('resource/1-13s.wav')
m14s=('resource/1-14s.wav')

button1.on_click = button_click_next
button2.on_click = button_click_open_answer
button3.on_click = button_click_replay
button4.on_click = button_click_resume


def rps():
    global choose
    global choose1
    global choose2
    global choose3
    global choose4
    global choose5
    global choose6
    global choose7
    global choose8
    global choose9
    global choose10
    global choose11
    global choose12
    global choose13
    global choose14
    global music
    choose = choose + 1
#    choose = int(random.randrange(1,15))
    print(choose)
    
    if choose == 1:
        if choose1 != 1:
            winsound.PlaySound(m1s, winsound.SND_ASYNC)
            choose1 = 1
            music = "next level"
            print("choose number 1's music")
        elif choose1 == 1:
            print("error:choose value is already choosed")
            rps()
    if choose == 2:
        if choose2 != 2:
            winsound.PlaySound(m2s, winsound.SND_ASYNC)
            choose2 = 2
            music = "chum cu nun zagun catalena"
            print("choose number 2's music")
        elif choose2 == 2:
            print("error:choose value is already choosed")
            rps()
    if choose == 3:
        if choose3 != 3:
            winsound.PlaySound(m3s, winsound.SND_ASYNC)
            choose3 = 3
            music = "superman"
            print("choose number 3's music")
        elif choose3 == 3:
            print("error:choose value is already choosed")
            rps()
    if choose == 4:
        if choose4 != 4:
            winsound.PlaySound(m4s, winsound.SND_ASYNC)
            choose4 = 4
            music = "ururung"
            print("choose number 4's music")
        elif choose4 == 4:
            print("error:choose value is already choosed")
            rps()
    if choose == 5:
        if choose5 != 5:
            winsound.PlaySound(m5s, winsound.SND_ASYNC)
            choose5 = 5
            music = "why tory"
            print("choose number 5's music")
        elif choose5 == 5:
            print("error:choose value is already choosed")
            rps()
    if choose == 6:
        if choose6 != 6:
            winsound.PlaySound(m6s, winsound.SND_ASYNC)
            choose6 = 6
            music = "mr.simple"
            print("choose number 6's music")
        elif choose6 == 6:
            print("error:choose value is already choosed")
            rps()
    if choose == 7:
        if choose7 != 7:
            winsound.PlaySound(m7s, winsound.SND_ASYNC)
            choose7 = 7
            music = "iu sin-gok"
            print("choose number 7's music")
        elif choose7 == 7:
            print("error:choose value is already choosed")
            rps()
    else:
        print("it can not make!")
    if choose == 8:
        if choose8 != 8:
            winsound.PlaySound(m8s, winsound.SND_ASYNC)
            choose8 = 8
            music = "200 pro"
            print("choose number 8's music")
        elif choose8 == 8:
            print("error:choose value is already choosed")
            rps()
    if choose == 9:
        if choose9 != 9:
            winsound.PlaySound(m9s, winsound.SND_ASYNC)
            choose9 = 9
            music = "ring-ding-dong"
            print("choose number 9's music")
        elif choose9 == 9:
            print("error:choose value is already choosed")
            rps()
    if choose == 10:
        if choose10 != 10:
            winsound.PlaySound(m10s, winsound.SND_ASYNC)
            choose10 = 10
            music = "asap"
            print("choose number 10's music")
        elif choose10 == 10:
            print("error:choose value is already choosed")
            rps()
    if choose == 11:
        if choose11 != 11:
            winsound.PlaySound(m11s, winsound.SND_ASYNC)
            choose11 = 11
            music = "pok-tan"
            print("choose number 11's music")
        elif choose11 == 11:
            print("error:choose value is already choosed")
            rps()
    if choose == 12:
        if choose12 != 12:
            winsound.PlaySound(m12s, winsound.SND_ASYNC)
            choose12 = 12
            music = "hit"
            print("choose number 12's music")
        elif choose12 == 12:
            print("error:choose value is already choosed")
            rps()
    if choose == 13:
        if choose13 != 13:
            winsound.PlaySound(m13s, winsound.SND_ASYNC)
            choose13 = 13
            music = "heart shaker"
            print("choose number 13's music")
        elif choose13 == 13:
            print("error:choose value is already choosed")
            rps()
    if choose == 14:
        if choose14 != 14:
            winsound.PlaySound(m14s, winsound.SND_ASYNC)
            choose14 = 14
            music = "her"
            print("choose number 14's music")
        elif choose14 == 14:
            print("error:choose value is already choosed")
            rps()
    else:
        print("it can not make!")
        if choose == 15:
            music = "End"
            rpsupdate()

#        if choose1 == 1:
#            if choose2 == 2:
#                if choose3 == 3:
#                    if choose4 == 4:
#                        if choose5 == 5:
#                            if choose6 == 6:
#                                if choose7 == 7:
#                                    if choose8 == 8:
#                                        if choose9 == 9:
#                                            if choose10 == 10:
#                                                if choose11 == 11:
#                                                    if choose12 == 12:
#                                                        if choose13 == 13:
#                                                            if choose14 == 14:
#                                                                music = "End"
#                                                                rpsupdate()
                                
        


def rpsupdate():
    global music
    
    music_text.text = str(music)
        
def rpl():
    global choose
    
    if choose == 1:
        winsound.PlaySound(m1s, winsound.SND_ASYNC)
        print("replay number 1's music")
    if choose == 2:
        winsound.PlaySound(m2s, winsound.SND_ASYNC)
        print("replay number 2's music")
    if choose == 3:
        winsound.PlaySound(m3s, winsound.SND_ASYNC)
        print("replay number 3's music")
    if choose == 4:
        winsound.PlaySound(m4s, winsound.SND_ASYNC)
        print("replay number 4's music")
    if choose == 5:
        winsound.PlaySound(m5s, winsound.SND_ASYNC)
        print("replay number 5's music")
    if choose == 6:
        winsound.PlaySound(m6s, winsound.SND_ASYNC)
        print("replay number 6's music")
    if choose == 7:
        winsound.PlaySound(m7s, winsound.SND_ASYNC)
        print("replay number 7's music")
    if choose == 8:
        winsound.PlaySound(m8s, winsound.SND_ASYNC)
        print("replay number 8's music")
    if choose == 9:
        winsound.PlaySound(m9s, winsound.SND_ASYNC)
        print("replay number 9's music")
    if choose == 10:
        winsound.PlaySound(m10s, winsound.SND_ASYNC)
        print("replay number 10's music")
    if choose == 11:
        winsound.PlaySound(m11s, winsound.SND_ASYNC)
        print("replay number 11's music")
    if choose == 12:
        winsound.PlaySound(m12s, winsound.SND_ASYNC)
        print("replay number 12's music")
    if choose == 13:
        winsound.PlaySound(m13s, winsound.SND_ASYNC)
        print("replay number 13's music")
    if choose == 14:
        winsound.PlaySound(m14s, winsound.SND_ASYNC)
        print("replay number 14's music")

app.run()