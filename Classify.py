#encoding:utf-8
import Format

class Course(object):
	def __init__(self):
		self.name = ''
		self.teacher = ''
		self.time = []
		self.classroom = []

def filldata(Courseinstance,args):
	Courseinstance.name = args[0]
	Courseinstance.teacher = args[1]
	Format.appendtime(Courseinstance,args[2].rstrip())
	Format.appendclassroom(Courseinstance,args[3].rstrip())

def getCourselist():
	f = open('schedule.txt','r')
	courselist = []
	itemlist = []
	flag = 1
	for line in f.readlines():
		if not flag==5:
			itemlist.append(line)
			flag += 1
		else:
			a = Course()
			filldata(a,itemlist)
			courselist.append(a)
			itemlist = []
			flag = 1
	return courselist
'''
for i in getCourselist():
	print i.name
	print i.teacher
	print i.time
	print i.classroom
'''
