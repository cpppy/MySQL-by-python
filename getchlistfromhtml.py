# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import re
import time
import jieba
import sys
import readCSV

def getChListFromHtml(url):
	#url="https://www.zhihu.com/question/49019162#answer-41274457"
	try:
		user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
		header = {"User-Agent":user_agent}
		req = urllib2.Request(url,headers=header)
		resp = urllib2.urlopen(req)
		html = resp.read()
	
		#html=urllib2.urlopen(url).read()
		html=unicode(html,'utf-8')
		word=re.findall(ur"[\u4e00-\u9fa5]+",html)

		s=""
		for w in word:
			s+=w
		
		seg_list=jieba.cut(s,cut_all=False)
		wdlist = list(seg_list)
		#print "read "+url[0:25]+" -------- OK ! "
		#fenci=",".join(wdlist)
		#print 'get web-->',s
		#print 'div result-》',fenci
		return wdlist
		#time.sleep(10)
	except:
		emptylist = []
		return emptylist
		
	
	
if __name__=="__main__":
	url = "http://blog.csdn.net/nevasun/article/details/7331644"
	#urlArr = readCSV.getUrl("browserHistory.csv")
	
	wdlist = getChListFromHtml(url)
	
	fenci=",".join(wdlist)
	
	#restore the string:fenci
	if(url.find('csdn')!=-1):
		filename = "CSDN.txt"
	elif(url.find('zhihu')!=-1):
		filename = "zhihu.txt"
	elif(url.find('bupt')!=-1):
		filename = "buptbbs.txt"
	elif(url.find('ustc')!=-1):
		filename = "ustcbbs.txt"
	elif(url.find('baidu')!=-1):
		filename = "baiduQA.txt"
	else:
		filename = "othersites.txt"
	
	fo = open(filename,'a')
	fo.write(fenci.encode('utf-8'))
	fo.close()
	
	
	
	
	
	
	
	
	
