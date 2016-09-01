# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import re
import time
import jieba
import getchlistfromhtml

def getCsdnUrlArr():
	url_arr=[]
	urlname_dic = {}
	for i in range(1,6):
		print 'page : ',i
		URL = 'http://blog.csdn.net/?&page='+str(i)
		user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
		header = {"User-Agent":user_agent}
		req = urllib2.Request(URL,headers=header)
		urlop = urllib2.urlopen(req,timeout=10)
		cont = urlop.read()
		#print cont

		findhead = '<h3  class'
		findtail = 'target='
		poshead = 0
		while(poshead!=-1):
			poshead = cont.find(findhead,poshead+1)
			postail = cont.find(findtail,poshead+1)
			blogURL = cont[poshead+54:postail-3]
			if(postail-poshead<200):
				print blogURL
				url_arr.append(blogURL)
				posnameh = postail+16
				findnamet = '</a></h3>'
				posnamet = cont.find(findnamet,poshead+1)
				blogname = cont[posnameh:posnamet]
				print blogname
				urlname_dic[blogURL]=blogname
				print "-----------*********************-------------"
	return url_arr,urlname_dic

if __name__ == '__main__':
	url_arr,urlname_dic = getCsdnUrlArr()
	'''
	wordsc = []
	for url in url_arr:
		wdlist = getchlistfromhtml.getChListFromHtml(url)
		wordsc.append(wdlist)
	'''





