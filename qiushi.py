#! /usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import copy
from bs4 import BeautifulSoup  


page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    soup =  BeautifulSoup(content)
    authuser = []
    textuser = []
    for a in soup.find_all("h2"):
	for i in a.stripped_strings:
		authuser.append(i)
	
    for b in soup.find_all("div" ,class_="content"):
	pattern = re.compile(r'<div.*>|</div>|<br/>|<!.*>')
	c = str(b).decode("utf-8")
	d = re.split(pattern,c)
	s = ""
	for i in range(len(d)):
		s = s+d[i]


    	

	textuser.append(s)
	
		
#    for dd in range(len(textuser)):
#	print "---------------------"
#	print textuser[dd]
#	print "---------------------"
    dectuser = {}
    for i in range(len(authuser)):
	dectuser[authuser[i]] = textuser[i]

    for t in dectuser:
	print "%s : \n %s" % (t,dectuser[t])        
   	print "-----------------------------" 
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason  
