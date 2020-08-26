#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import base64
import os
# import pymysql.cursors
# Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='admin@123',
#                              db='login',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=ornsT7TsKz305CHrgytwpMRh&client_secret=kbl7dczRGILTQdFLibjkSz8YdhgSxlD0'
respons = requests.get(host).json()
# print(type(respons))
# print(respons['access_token'])
'''
身份证识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# dir = 'C:/Users/admin/Desktop/fileimage/fileimg888/'
# 二进制方式打开图片文件
# aaa = []
path=input("请输入路径(例如D:\\\\picture)：")
# for f in os.listdir("C:\\Users\\admin\\Desktop\\fileimage\\fileimg888\\"):
for f in os.listdir(path):
	gg = path+'\\'+f
	dd = open(path+'\\'+f, 'rb')
	img = base64.b64encode(dd.read())

	params = {"id_card_side":"front","image":img}
	access_token = respons['access_token']
	request_url = request_url +"?access_token="+ access_token
	# print(request_url)
	headers = {'content-type': 'application/x-www-form-urlencoded'}
	response = requests.post(request_url, data=params, headers=headers)
	result = response.json()
	# print(result)
	for k,v in result.items():
		print(k,v)
	# if response:
	#     result = response.json()
	# #    print (response.json())
	# 	# print(type(result))
	#     for k in result:
	#     	# ss = result[k]
	#     	if k == 'words_result':
	#     		# print(type(result))
	#     		# print(result)
	#     		for j,i in result[k].items():
	#     			# print(j,i)
	#     			# aa = []
	#     			for m,n in i.items():
	#     				# print(type(i))
	#     				# print(i)
	#     				# print(i['民族'])
	#     				# print(type(i))
	#     				# print(i)
	#     				# del i['location']
	#     				# print(i)
	#     				# print(j,n)
	#     				# aa = []
	#     				if m == 'words' and j == '姓名':
	#     					print(j,n)
	#     					aa = n
	# 						# print(n)
	# 						# print(type(n))
	# 						# aa = n
	#     				if m == 'words' and j=='公民身份号码':
	#     					print(j,n)
	#     					bb = n
	#     				# elif bb == '':
	#     					# aaa.append[f]
	#     					# print(aaa)
	#     					# print(type(i))
	#     					# print(i)
	#     					# del i['民族']
	#     					# del i['住址']
	#     					# del i['出生']
	#     					# del i['性别']
	#     					# elif j == '姓名'：
	#     						# elif j== '公民身份号码'：
	#     					# aa.append(n)
	#     					# print(aa)
	#     					# aa.append([n])
	#     					# print(type(aa))
	#     					# print(aa)
	#     					connection = pymysql.connect(host='localhost',user='root',password='admin@123',
	#     						db='login',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	#     					try:
	#     						with connection.cursor() as cursor:
	#     							sql = "INSERT INTO `user` (`username`, `password`,`addr`) VALUES (%s, %s,%s)"
	#     							cursor.execute(sql, (aa,bb,gg))
	#     						connection.commit()
	#     					finally:
	#     						connection.close()
