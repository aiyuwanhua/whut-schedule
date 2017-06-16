#-*-coding:utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def appendtime(Courseinstance,str):
	time_list = filter(lambda i:i!='',str.split(';'))
	num = len(time_list)
	pattern = '周(.*?)第(.*?)节{第(.*?)周}'
	for i in time_list:
		result = re.match(pattern,i)
		a = result.group(1)
		#print a
		b = result.group(2)
		#print b
		if '单' in result.group(3):
			l = re.match('(.*?)单',result.group(3)).group(1).split('-')
			c = range(int(l[0]),int(l[1])+1,2)
		#elif '双' in result.group(3):pass
		else:
			l = result.group(3).split('-')
			c = range(int(l[0]),int(l[1])+1)
		#print c
		Courseinstance.time.append([a,b,c])
		
'''
obj = Classify.Course()
str = '周一第5-6节{第17-17周};周一第7-8节{第13-15周};周一第7-8节{第16-17周};周三第5-6节{第03-17周};'
appendtime(obj,str)

print obj.time
for i in obj.time:
	print i
'''