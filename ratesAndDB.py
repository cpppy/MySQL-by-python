# -*- coding: utf-8 -*-
import readCSV
import getchlistfromhtml
import collections
import MySQLdb

#urlArr = readCSV.getUrl("browserHistory.csv")
urlArr = ["http://blog.csdn.net/nevasun/article/details/7331644"]

# build dictionary for the whole words
csdn = {}
zhihu = {}
buptbbs = {}
ustcbbs = {}
baiduQA = {}
othersites = {}


# get rates of every word in each table(classify)
for url in urlArr:
	# from url get the dic_name & get rates of every word
	if(url.find('csdn')!=-1):
		wdlist = getchlistfromhtml.getChListFromHtml(url)
		for word in wdlist:
			if word not in csdn:
				csdn[word] = 0
			csdn[word] += 1
			
	elif(url.find('zhihu')!=-1):
		wdlist = getchlistfromhtml.getChListFromHtml(url)
		for word in wdlist:
			if word not in zhihu:
				zhihu[word] = 0
			zhihu[word] += 1
			
	elif(url.find('bupt')!=-1):
		wdlist = getchlistfromhtml.getChListFromHtml(url)
		for word in wdlist:
			if word not in csdn:
				buptbbs[word] = 0
			buptbbs[word] += 1
			
	elif(url.find('ustc')!=-1):
		filename = "ustcbbs.txt"
		wdlist = getchlistfromhtml.getChListFromHtml(url)
		for word in wdlist:
			if word not in csdn:
				ustcbbs[word] = 0
			ustcbbs[word] += 1
			
	elif(url.find('baidu')!=-1):
		filename = "baiduQA.txt"
		wdlist = getchlistfromhtml.getChListFromHtml(url)
		for word in wdlist:
			if word not in csdn:
				baiduQA[word] = 0
			baiduQA[word] += 1
			
	else:
		filename = "othersites.txt"
		wdlist = getchlistfromhtml.getChListFromHtml(url)
		for word in wdlist:
			if word not in csdn:
				othersites[word] = 0
			othersites[word] += 1
			

#restore data into database
#database: postana
#tables:csdntable,zhihutable......

#   in2db(csdn,csdntable)
def in2db(dic,tablename):
	print "tablename :  ",tablename
	dic  = collections.OrderedDict(sorted(dic.items(), key = lambda t: -t[1]))
	
	''' //tansfer count to rate
	sum = 0
	for value in dic.values():
		sum += value
	for key,value in dic.viewitems():
		value = float(value)/sum
		print "dic---- ",key," : ",value
		'''
		
	try:
		conn = MySQLdb.connect(host="localhost",user="root",passwd="ene",db="postana",use_unicode=True,charset="utf8",port=0)
		print " database connected success !"
		cur = conn.cursor()
		#delete data restored in this table before
		cur.execute("delete from "+tablename)
		conn.commit()
		#prepare data and write into this table
		insertvalues=[]
		i=1
		for key,value in dic.viewitems():
			item = [i,key,value,tablename[0:-5]]
			insertvalues.append(item)
			item = []
			i += 1
			
		cur.executemany("insert into "+tablename+" values(%s,%s,%s,%s)",insertvalues)
		conn.commit()
		
		cur.close()
		conn.close()
		print "---Data have been written into ",tablename,"  ! ---"
	except MySQLdb.Error,e:
		print "MySQL Error %d: %s" % (e.args[0], e.args[1])
	






	
			
		
		
		
		
