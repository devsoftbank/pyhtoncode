#https://api.jisuapi.com/idcard/query?appkey=yourappkey&idcard=41272519800102067x
#https://api.jisuapi.com/idcard/query?appkey=fe3529619c1db286&idcard=421023198708286359
#{"status":0,"msg":"ok","result":{"province":"湖北","city":"荆州","town":"监利县","area":"湖北省 荆州市 监利县","lastflag":0,"sex":"男","birth":"1987年08月28日"}}
import pymysql
import requests
import time
conn = pymysql.connect(host="127.0.0.1",user="root",password="admin@123",database="juhedata",charset="utf8")
cursor = conn.cursor()
for i in range(3,100):
	sql = "select ucard from jh_Userinfo where uid=%s"
	cursor.execute(sql,str(i))
	ret = cursor.fetchone()	
	retresult= "".join(ret)
	http_start = 'https://api.jisuapi.com/idcard/query?appkey=fe3529619c1db286&idcard='
	http_end = http_start+retresult
	result = requests.get(http_end)
#	print(result)
	lists = result.json()['result']
#	print(lists['province'])
	uaddress = str(lists['province']+lists['city']+lists['town'])
	usex = lists['sex']
#	ucompany = lists['company']
	print(uaddress)
	sqll = "update jh_Userinfo set uaddress=%s, usex = %s where uid=%s;"
	cursor.execute(sqll,[uaddress,usex,str(i)])
	conn.commit()
	print("update %d sucess"%i)
	time.sleep(3)