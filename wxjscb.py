from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
 
bot = Bot()
#bot.join()             #不注释此代码时，不执行bot后面代码
 
 
def get_news():
 
    """获取金山词霸每日一句，英文和翻译"""
	
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']      #英文
    note = r.json()['note']            #中文
    misue = r.json()['tts']            #语音
    return content, note ,misue
 
def send_news():
    try:
        contents = get_news()
 
        # 你朋友的微信名称，不是备注，也不是微信帐号。
 
        my_friend = bot.friends().search(u'朋友微信名词')[0]
        my_friend.send(contents[0])
        my_friend.send(contents[1])
        my_friend.send(contents[2])
        my_friend.send(u"Have a good day, love you baby!")
        # 每86400秒（1天），发送1次，通过线程方式控制发送时间，不用登录
        t = Timer(86400, send_news)
        t.start()
    except:
 
        # 你的微信名称，不是备注，也不是微信帐号。
        my_friend = bot.friends().search('自己微信名词')[0]
        my_friend.send(u"Failure to send message!")
 
 
if __name__ == "__main__":
    send_news()