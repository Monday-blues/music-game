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
button1 = Button(text="▶", color=color.pink, x=-0.6, scale=0.2)      
button2 = Button(text="⬤", color=color.pink, scale=0.2)
button3 = Button(text="⟳", color=color.pink, x=0.6, scale=0.2)
button4 = Button(text="?", color=color.blue, x=0.6, y=0.3, scale=0.2)

choose1 = 0

def button_click_next():
    print("button_clicked")
    rps()

def button_click_open_answer():
    print("show answer")
    rpsupdate()
    
def button_click_replay():
    print("replay")
    rpl()
    
def button_click_resume():
    print("resume music")
    button1.scale = 0.2
    button2.scale = 0.2
    button3.scale = 0.2
    
    

button1.on_click = button_click_next
button2.on_click = button_click_open_answer
button3.on_click = button_click_replay
button4.on_click = button_click_resume


def rps():
    global choose
    global choose1
    global music
    choose = int(random.randrange(1,3))
    if choose == 1:
        if choose1 != 1:
            winsound.PlaySound("1-01.ogg", winsound.SND_ASYNC)
            choose1 = 1
            music = "come back home"
            print("choose number 1's music")
        else:
            print("error:choose value is already choosed")
            rps()
    else:
        print("it can not make!")

def rpsupdate():
    global music
    
    music_text.text = str(music)
    button1.scale = 0
    button2.scale = 0
    button3.scale = 0
        
def rpl():
    global choose
    
    if choose == 1:
        winsound.PlaySound("1-01.ogg", winsound.SND_ASYNC)
        print("replay number 1's music")

app.run()