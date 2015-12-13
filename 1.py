import urllib.request
import os
import re

def open_url(page_url):
	req = urllib.request.Request(page_url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36')
	page = urllib.request.urlopen(req)
	html = page.read().decode('utf-8')
	return html

def get_img(html):
	q = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
	imglist = re.findall(q,html)
	for each in imglist:
		filename = each.split("/")[-1]
		urllib.request.urlretrieve(each,filename,None)

def download():
	os.chdir(r'D:\\A')
	url = 'http://tieba.baidu.com/p/2848748716?pn='
	for i in range(1,10):
		page_num = i
		page_url = url + str(page_num)
		folder=(str(page_num))
		os.mkdir(folder)
		os.chdir(folder)
		get_img(open_url(page_url))
		os.chdir(r'D:\\A')


if __name__ == '__main__':
	download()


