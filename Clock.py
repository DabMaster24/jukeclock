import datetime
import time
import RPi.GPIO as GPIO
import vlc
import pafy
from pygame import mixer

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)
mixer.init()
url = "https://www.youtube.com/playlist?list=PLK3jctReHIcET3Vy9TfZ6I-i5v0LH5seL"
playlist = pafy.get_playlist(url)
items = playlist["items"]
song_index=0
Instance = vlc.Instance()
player = Instance.media_player_new()
sounds=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sounds[0]=mixer.Sound("piano2.wav")
sounds[1]=mixer.Sound("/home/pi/Clock Project Audio/1.wav")
sounds[2]=mixer.Sound("/home/pi/Clock Project Audio/2.wav")
sounds[3]=mixer.Sound("/home/pi/Clock Project Audio/3.wav")
sounds[4]=mixer.Sound("/home/pi/Clock Project Audio/4.wav")
sounds[5]=mixer.Sound("/home/pi/Clock Project Audio/5.wav")
sounds[6]=mixer.Sound("/home/pi/Clock Project Audio/6.wav")
sounds[7]=mixer.Sound("/home/pi/Clock Project Audio/7.wav")
sounds[8]=mixer.Sound("/home/pi/Clock Project Audio/8.wav")
sounds[9]=mixer.Sound("/home/pi/Clock Project Audio/9.wav")
sounds[10]=mixer.Sound("/home/pi/Clock Project Audio/10.wav")
sounds[11]=mixer.Sound("/home/pi/Clock Project Audio/lam.wav")
sounds[12]=mixer.Sound("/home/pi/Clock Project Audio/muoi.wav")
sounds[13]=mixer.Sound("/home/pi/Clock Project Audio/mot.wav")
sounds[14]=mixer.Sound("/home/pi/Clock Project Audio/sang.wav")
sounds[15]=mixer.Sound("/home/pi/Clock Project Audio/trua.wav")
sounds[16]=mixer.Sound("/home/pi/Clock Project Audio/chieu.wav")
sounds[17]=mixer.Sound("/home/pi/Clock Project Audio/toi.wav")
sounds[18]=mixer.Sound("/home/pi/Clock Project Audio/khuya.wav")
sounds[19]=mixer.Sound("/home/pi/Clock Project Audio/gio.wav")
sounds[20]=mixer.Sound("/home/pi/Clock Project Audio/phut.wav")
mixer.music.set_volume(10)


def get_time():
    x = datetime.datetime.now()
    hour=int(x.strftime("%I"))
    minute=int(x.strftime("%M"))
#    second=int(x.strftime("%S"))
    ampm=x.strftime("%p")
    
    play_hour(hour)
    time.sleep(1)
    play_minute(minute)
#    time.sleep(1)
#    play_second(second)
    time.sleep(1)
    play_am_pm(ampm, hour)

def play_hour(h):
#    print(h)
    if h>10:
        mixer.Sound.play(sounds[10])
        time.sleep(delay)
        mixer.Sound.play(sounds[h%10])
        time.sleep(delay)
        mixer.Sound.play(sounds[19])
    else:
        mixer.Sound.play(sounds[h])
        time.sleep(delay)
        mixer.Sound.play(sounds[19])
        
def play_minute(m):
#    print(m)
    if m>=20:
        m=str(m)
        mixer.Sound.play(sounds[int(m[0])])
        time.sleep(delay)
        mixer.Sound.play(sounds[12])
        time.sleep(delay)
        m=int(m)
        if m%10==5:
            mixer.Sound.play(sounds[11])
        elif m%10==1:
            mixer.Sound.play(sounds[13])
        elif not m%10==0:
            mixer.Sound.play(sounds[m%10])
        time.sleep(delay)
        mixer.Sound.play(sounds[20])
    elif m>10 and m<20:
        mixer.Sound.play(sounds[10])
        time.sleep(delay)
        if m%10==5:
            mixer.Sound.play(sounds[11])
        else:
            mixer.Sound.play(sounds[m%10])
        time.sleep(delay)
        mixer.Sound.play(sounds[20])
    else:
        mixer.Sound.play(sounds[m])
        time.sleep(delay)
        mixer.Sound.play(sounds[20])

#def play_second(s):
#    print(s)

def play_am_pm(ap, hr):
#    print(ap)
    if (hr>=4 and hr<12) and ap=='AM':
       mixer.Sound.play(sounds[14])
    elif (hr==12 or hr<4) and ap=='PM':
       mixer.Sound.play(sounds[15])
    elif (hr>=4 and hr<7) and ap=='PM':
       mixer.Sound.play(sounds[16])
    elif (hr>=7 and hr<11) and ap=='PM':
       mixer.Sound.play(sounds[17])
    elif (hr>=11 and ap=='PM') or ((hr==12 or hr<4) and ap=='AM'):
       mixer.Sound.play(sounds[18])
       
def play_song(url):
    global player
    
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    return video.length


def test_clock(channel):
#     while True:
#        if not GPIO.input(25):
    global current_state, song_index, player

    if current_state==state_idle:   
        print("idle")
        get_time()
        current_state=state_time
    elif current_state==state_time:
        print("time")
        
        item = items[song_index]
        i_pafy = item['pafy'] 
        y_url = i_pafy.watchv_url
        length = play_song(y_url)
        
        if song_index==len(items)-1:
            song_index=0
        else:
            song_index+=1
            
        current_state=state_song
    elif current_state==state_song:
        print("song")        
        player.stop()
        current_state=state_idle
            
delay=0.6
state_idle=0
state_time=1
state_song=2
current_state=state_idle
mixer.Sound.play(sounds[0])
time.sleep(delay)
GPIO.add_event_detect(25, GPIO.FALLING, callback=test_clock, bouncetime=5000)

while True: 
#     try:
#     GPIO.wait_for_edge(25, GPIO.FALLING)
    time.sleep(delay)
# 
#     except KeyboardInterrupt:
#         GPIO.cleanup()
#     
