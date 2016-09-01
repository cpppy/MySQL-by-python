# -*- coding: utf-8 -*-

import readDB2dic
import getNew
import getchlistfromhtml
import collections

# refresh the frequency of each word using idf_rates
def multiIDF(dic,idf_dic):
	for key,value in dic.items():
		if key in idf_dic.keys():
			if(idf_dic[key]<2.2):
				idf_dic[key]=0
			dic[key]=value*idf_dic[key]
		else:
			dic[key]=value*10
	return dic

#get new url resource from csdn bolg website
def getWordFromNewUrl():
	url_arr,urlname_dic = getNew.getCsdnUrlArr()    # !!! CSDN
	wordsc = []
	for url in url_arr:
		wdlist = getchlistfromhtml.getChListFromHtml(url)
		wordsc.append(wdlist)
	return wordsc,url_arr,urlname_dic

def wlist2ratesDic(wlist):
	dic = {}
	for word in wlist:
		word = word.encode('utf-8')
		if word not in dic.keys():
			dic[word] = 0
		dic[word] += 1
	sum=len(wlist)
	for key,value in dic.viewitems():
		dic[key] = float(value)/sum
	return dic

# cosine similarity
def calcScore(source_dic,new_dic):
	score = 0
	for key,value in new_dic.items():
		if key in source_dic.keys():
			score += value*source_dic[key]
	return score



if __name__ == '__main__':
	
	csdn_dic = readDB2dic.table2list('csdntable')
	#zhihu_dic = readDB2dic.table2list('zhihutable')
	#baiduQA_dic = readDB2dic.table2list('baiduQAtable')
	idf_dic = readDB2dic.table2list('idftable')

	csdn_dic = multiIDF(csdn_dic,idf_dic)
	csdn_dic = collections.OrderedDict(sorted(csdn_dic.items(), key = lambda t: -t[1]))
	print "csdn_dic------------****"
	for key,value in csdn_dic.items():
		print key,'\t',value
		
	
	#get new word_bag from new url each day
	wordsc,url_arr,urlname_dic = getWordFromNewUrl()
	score_arr = []
	for wlist in wordsc:
		print 'get one wlist of a fresh url !'
		new_dic = wlist2ratesDic(wlist)
		new_dic = multiIDF(new_dic,idf_dic)
		print 'get rates dic after multipuls the idf_frequency !' 
		new_dic = collections.OrderedDict(sorted(new_dic.items(), key = lambda t: -t[1]))
		print 'sort the new url wdlist dic after deal with by IDF algorithm !'
		'''
		print "new_dic------------****"
		for key,value in new_dic.items():
			print key,'\t',value
		'''
		score = calcScore(csdn_dic,new_dic)
		score_arr.append(score)
	
	# restore score to dic with url
	score_dic = {}
	for i in range(len(score_arr)):
		score_dic[url_arr[i]] = score_arr[i]
		
	score_dic = collections.OrderedDict(sorted(score_dic.items(), key = lambda t: -t[1]))
	
	# print results
	for key,value in score_dic.items():
		print 'Score = ',value
		print 'URL   = ',key
		print 'Title : ',urlname_dic[key]
		print "----------------------------"
		

	
