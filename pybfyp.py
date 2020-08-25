# 使用playsound库
from playsound import playsound
playsound('xx.mp3')

# ②使用pygame库
from pygame import mixer 
import time
mixer.init()
mixer.music.load('xx.mp3')
mixer.music.play()
time.sleep(5)
mixer.music.stop()

# ③使用mp3play库（仅支持python2，对python3不支持）
import mp3play
import time
clip = mp3play.load('xx.mp3')
clip.play()
time.sleep(5) 
clip.stop()

# ④打开系统自带播放器，然后播放MP3，弹窗麻烦复杂
import os
os.system('xx.mp3')
