import pymysql
import time
import requests
#{"status":0,"msg":"ok","result":{"shouji":"13871303832","province":"湖北","city":"武汉","company":"中国移动","cardtype":"GSM","areacode":"027"}}
conn = pymysql.connect(host="127.0.0.1",user="root",password="admin@123",database="juhedata",charset="utf8")
cursor = conn.cursor()
for i in range(900,930):
	sql = "select utel from jh_Userinfo where uid=%s"
	cursor.execute(sql,str(i))
	ret = cursor.fetchone()	
	retresult= "".join(ret)
	http_start = 'https://api.jisuapi.com/shouji/query?appkey=fe3529619c1db286&shouji='
	http_end = http_start+retresult
	result = requests.get(http_end)
#	print(result)
	lists = result.json()['result']
#	print(lists['province'])
	strresult = str(lists['province']+lists['city'])
	ucompany = lists['company']
	print(strresult)
	sqll = "update jh_Userinfo set uarea=%s, ucompany = %s where uid=%s;"
	cursor.execute(sqll,[strresult,ucompany,str(i)])
	conn.commit()
	print("update %d sucess"%i)
	time.sleep(3)
#	for j in result.json()['result'].values():
#		lists.append(j)
#		print(index)

#		strresult = str(results[1]+results[2])
#		print(strresult)
cursor.close()
conn.close()
#for i in range(1,500):
#	sql = "select * from jh_Userinfo where uid=1"
#	ret = cursor.execute(sql)
#	print(ret)
	

"""
http_end = 'https://api.jisuapi.com/shouji/query?appkey=fe3529619c1db286&shouji=13871303832'
result = requests.get(http_end)
print(result)
print(result.json()['result'])
for i in result.json()['result'].values():
	results.append(i)
#	return results
#print('城市：%s'%rep.json()['']
print(results[1])
print(results[2])
strresult = str(results[1]+results[2])
print(strresult)
"""
