#-*-encoding:utf-8-*-
import Classify
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def selectScheduleByWeek(week):
	for course in courselist:
		for time in course.time:
			if week in time[2]:
				c = Classify.Course()
				c.name = course.name
				c.teacher = course.teacher
				c.time = time
				index = course.time.index(time)
				if not course.classroom==[]:
					c.classroom = course.classroom[index]
				else:
					c.classroom = ''
				courseleft.append(c)
	flag = []
	for i in range(0,5):
		flag.append([])
		for j in range(0,7):
			flag[i].append('<td></td>')
	for course in courseleft:
		if course.time[0]!='' and course.time[1]!='':
			flag[time1[str(course.time[1])]][time0[str(course.time[0])]] = '<td>'+course.name+'<br/>'+course.teacher+'<br/>'+course.classroom+'<br/></td>'
	return flag
	
time0 = {
	'一':0,
	'二':1,
	'三':2,
	'四':3,
	'五':4,
	'六':5,
	'日':6
}
time1 = {
	'1-2':0,
	'3-4':1,
	'5-6':2,
	'7-8':3,
	'9-11':4
}

courselist = Classify.getCourselist()
courseleft = []
flag = selectScheduleByWeek(2)

str = '''
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>schedule</title>
</head>
<body>
<table border="1px" >
'''
for row in range(0,5):
	str += '<tr>\n'
	for column in range(0,7):
		str += flag[row][column]+'\n'
	str += '</tr>\n'
str += '''
</table>
</body>
</html>
'''

f = open('test.html','w')
f.write(str)
f.close
