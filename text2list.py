# -*- coding: utf-8 -*-
#read txt file

def readtxt(filename):
	listout = []
	of=open(filename,'r')
	lineArr = of.readlines()
	for index in range(len(lineArr)):
		print "-------------------------------"
		print "        line : ",index,"       "
		print "-------------------------------"
		line = lineArr[index]
		if(len(line)>40):
			pos=line.find(':')
			line = line[pos+1:]
			line = line.strip()
			#line = unicode(line,'utf-8')
			wordlist = list(line.split(','))
			if(len(wordlist)!=0):
				listout.extend(wordlist)
				del wordlist[:]
	return listout


	
listout = readtxt("CSDN.txt")



