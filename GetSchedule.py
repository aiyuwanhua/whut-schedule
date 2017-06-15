#encoding;utf-8
import re

pattern = '<tr>.*?<td>(.*?)&nbsp;.*?<td>(.*?)&nbsp;.*?<td>\s*(.*?)\s*&nbsp;.*?<td>(.*?)&nbsp;</td>'

f = open('whut-schedule.txt','r')

result = re.findall(pattern,f.read(),re.S)

f.close()
f = open('schedule.txt','w')

for cource in result:
	for item in cource:
		f.write(item+'\n')
	f.write('\n')

f.close()
print 'done'
