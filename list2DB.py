# -*- coding: utf-8 -*-
# list2DB.py

import text2list
import ratesAndDB
import collections
import MySQLdb

'''
# build dictionary for the whole words
csdn = {}
zhihu = {}
buptbbs = {}
ustcbbs = {}
baiduQA = {}
othersites = {}
'''

#get rates of every word from each txt file
def getRatesFromList(filename):
	dic = {}
	wordlist = text2list.readtxt(filename)
	for word in wordlist:
		if word not in dic:
			dic[word] = 0
		dic[word] += 1
	return dic


csdn = getRatesFromList("CSDN.txt")
zhihu = getRatesFromList("zhihu.txt")
buptbbs = getRatesFromList("buptbbs.txt")
ustcbbs = getRatesFromList("ustcbbs.txt")
baiduQA = getRatesFromList("baiduQA.txt")
othersites = getRatesFromList("othersites.txt")


#write dictionary to each table in database:postana
ratesAndDB.in2db(csdn,"csdntable")	
ratesAndDB.in2db(zhihu,"zhihutable")	
ratesAndDB.in2db(buptbbs,"buptbbstable")	
ratesAndDB.in2db(ustcbbs,"ustcbbstable")	
ratesAndDB.in2db(baiduQA,"baiduQAtable")	
ratesAndDB.in2db(othersites,"othersitestable")	

















