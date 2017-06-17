#encoding:utf-8
import urllib2
import urllib

def getHtml(userName,password,type):
	url = 'http://sso.jwc.whut.edu.cn/Certification/login.do'
	data = {}
	data['userName'] = userName
	data['password'] = password
	data['type'] = type
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
	}
	formData = urllib.urlencode(data)
	req = urllib2.Request(url,data=formData,headers=headers)
	response = urllib2.urlopen(req)
	return response

if __name__=="__main__":
	file = open('whut-schedule.txt','w')
	response = getHtml(username,password,'xs')
	file.write(response.read())
	file.close()
	print 'done'
