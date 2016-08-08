# -*- coding: cp936 -*-
import csv
import codecs

def washData(filename):
	fr = open(filename,'rU')
	arrayoflines = fr.readlines()
	numoflines = len(arrayoflines)
	print "numoflines=",numoflines
	
	array = []
	for lineindex in range(numoflines):#len(numoflines)):
		line = arrayoflines[lineindex]
		line = line.strip().split(',')
		array.append(line)
		#array.append(list(line.strip().split(',')))
		#line = arrayoflines[lineindex].strip(',')
	
	fr.close()
	return array

def getURL(filename):
	urlArr = []
	rec2vec = washData(filename)
	for i in range(len(rec2vec)):
		urlArr.append(rec2vec[i][0])
	return urlArr
		
if __name__=="__main__":
	rec = getURL("browserHistory.csv")
	for i in range(len(rec)):
		print rec[i]
