#encoding:utf-8

class Course(object):
	def __init__(self):
		self.name = ''
		self.teacher = ''
		self.time = []
		self.classroom = []

def filldata(Courseinstance,args):
	Courseinstance.name = args[0]
	Courseinstance.teacher = args[1]
	Courseinstance.time.append(args[2])
	Courseinstance.classroom.append(args[3])


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

for i in courselist:
	print i.name
	print i.teacher
	for j in i.time:
		print j
	for j in i.classroom:
		print j


