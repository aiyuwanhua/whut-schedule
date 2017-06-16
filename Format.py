#encoding:utf-8
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#f = open('schedule.txt','r')
f = u'周一第1-2节{第01-16周};周四第3-4节{第01-16单周};'
f = filter(lambda i:i!='',f.split(';'))
num = len(f)
pattern = u'周(.*?)第(.*?)节{第(.*?)周}'
for i in f:
	result = re.match(pattern,i)
	print result.group(1)
	print result.group(2)
	if '单' in result.group(3):
		l = re.match(u'(.*?)单',result.group(3)).group(1).split('-')
		a = range(int(l[0]),int(l[1])+1,2)
	#elif '双' in result.group(3):
	#	l = re.match(u'(.*?)双',result.group(3)).group(1).split('-')
	#	a = range(int(l[0]),int(l[1])+1,2)
	else:
		l = result.group(3).split('-')
		a = range(int(l[0]),int(l[1])+1)
	print a

