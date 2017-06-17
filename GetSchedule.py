#encoding;utf-8
import re

def getSchedule(response):
	pattern = '<tr>.*?<td>(.*?)&nbsp;.*?<td>(.*?)&nbsp;.*?<td>\s*(.*?)\s*&nbsp;.*?<td>(.*?)&nbsp;</td>'
	result = re.findall(pattern,response.read(),re.S)
	f = open('schedule.txt','w')
	for cource in result:
		for item in cource:
			f.write(item+'\n')
		f.write('\n')
	f.close()

if __name__=="__main__":
	f = open('whut-schedule.txt','r')
	getSchedule(f)
	f.close()
	print 'done'
