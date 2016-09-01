# -*- coding: utf-8 -*-
#use othersites.txt as the text reporsitory
import collections
import math
import MySQLdb

def read(filename):
	arr = []
	of=open(filename,'r')
	linesarr=of.readlines()
	for line in linesarr:
		line=line.strip()
		pos=line.find(':')
		line=line[pos+1:]
		if(len(line)>100):
			#print len(line)
			line=line.split(',')
  			arr.append(line)
    		#print line[0:5]
    
	of.close()
	return arr

arr=read('othersites.txt')
wset=set([])
for page in arr:
	wset=set(page)|wset
#print wset
dic={}
for word in wset:
	dic[word]=0
for page in arr:
	page = set(page)
	for word in wset:
		if word in page:
			dic[word]+=1
			print word," : ",dic[word]
		
# sort the dic based on value
#dic  = collections.OrderedDict(sorted(dic.items(), key = lambda t: -t[1]))
# get IDF of each word
for key,value in dic.viewitems():
	dic[key]=math.log(len(arr)/(value+1))


# IDF-dic to Database
def idf2DB(dic,tablename):
	print "tablename :  ",tablename
	dic  = collections.OrderedDict(sorted(dic.items(), key = lambda t: -t[1]))	
		
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
			item = [i,key,value,"othersites"]
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

idf2DB(dic,"idftable")













'''
fo = open('out.txt','w')
for arri in arr:
	fo.write(arri+'\n')
fo.close()
'''
