# -*- coding: utf-8 -*-
import readCSV
import MySQLdb

# read table in database , restore the data into dictionary 
def table2list(tablename):
	print "now , deal with table: ",tablename
	print "try connecting the Database--'postana'--"
	conn = MySQLdb.connect(host='localhost',user='root',passwd='ene',db='postana',charset='utf8')  
	print  'DB is connected success !'
	cur = conn.cursor() 
	   
	freq_arr=[]  
	count = cur.execute('select frequency from '+tablename)	
	results=cur.fetchall()
	result=list(results)
	for freq in result:
		#print float(freq[0])
		freq_arr.append(float(freq[0]))
	cur.scroll(0,mode='absolute')  #index come to start point, default mode is "relative"
	
	word_arr=[]
	count=cur.execute('select word from '+tablename)
	results=cur.fetchall()
	result=list(results)
	for word in result:
		#print word[0].encode('utf-8')
		word_arr.append(word[0].encode('utf-8'))
	
	dic={}
	print "word quantity=",len(word_arr),'\t','frequency quantity=',len(freq_arr)
	for index in range(len(word_arr)):
		dic[word_arr[index]]=freq_arr[index]
		print word_arr[index],"   ",freq_arr[index]
	
	print "DATA in "+tablename+" have been written into Dictionary"
	conn.close()
	print 'DB --postana--   closed!'
	print '----------------------------------------'
	print '\n'
	return dic

if __name__ == '__main__':
	csdn_dic = table2list('csdntable')
	#zhihu_dic = table2list('zhihutable')
	#baiduQA_dic = table2list('baiduQAtable')
	
	
