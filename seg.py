import urllib,urllib2
import json

base_url = 'http://segmenttest.sinaapp.com/'

def segment(content):
	payload = urllib.urlencode({'content':content})
	url = base_url+'?'+payload
	return json.loads(urllib2.urlopen(url).read())
	
if __name__=="__main__":
	while 1:
		content = raw_input("Enter the content")
		print `content`
		print segment(content.decode('gbk').encode('UTF8'))
