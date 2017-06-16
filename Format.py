#encoding:utf-8
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#f = open('schedule.txt','r')
f = '周一第1-2节{第01-16周};周四第3-4节{第01-16单周};'
pattern = '(.*?){(.*?)};'
result = re.findall(pattern,f)
for turple in result:
	#print turple
	for item in turple:
		print item.decode('utf-8')