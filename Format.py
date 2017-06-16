#-*-coding:utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def appendtime(Courseinstance,str):
	time_list = filter(lambda i:i!='',str.split(';'))
	#num = len(time_list)
	pattern = '周(.*?)第(.*?)节{第(.*?)周}'
	pattern2 = '(.*?)周'
	returndata = []
	for i in time_list:
		try:
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
			returndata = [a,b,c]
		except AttributeError:
			result = re.match(pattern2,i)
			c = result.group(1).split('-')
			c = range(int(c[0]),int(c[1])+1)
			returndata = ['','',c]
		finally:
			Courseinstance.time.append(returndata)

def appendclassroom(Courseinstance,str):
	classroom_list = filter(lambda i:i!='',str.split(';'))
	#num = len(classroom_list)
	for i in classroom_list:
		Courseinstance.classroom.append(i)



'''
obj = Classify.Course()
str = '周一第5-6节{第17-17周};周一第7-8节{第13-15周};周一第7-8节{第16-17周};周三第5-6节{第03-17周};'
str2 = '18-20周'
appendtime(obj,str2)

for i in obj.time:
	print i
'''

