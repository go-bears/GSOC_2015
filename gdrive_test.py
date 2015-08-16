import os
import urllib #for urlretrieve 
import urllib2
<<<<<<< HEAD
from urlparse import urlparse, urlunparse
# <code>https://drive.google.com/file/d/FILE_ID/edit?usp=sharing
import requests
# import pycurl
# import webapp2


target_url = "https://drive.google.com/file/d/0B_QbDSPaPwJzVVh2ZW1YZmVTOUU/view?usp=sharing"

from urlparse import urlparse, urlunparse, urlunsplit
# <code>https://drive.google.com/file/d/FILE_ID/edit?usp=sharing
import requests

new_target = "https://docs.google.com/document/d/FILE_ID/export?format=doc"


target_url = "https://drive.google.com/file/d/0B_QbDSPaPwJzeUUzU3ZJd0cyOUE/view?usp=sharing"

(scheme, net_location, path_raw, param, query, frag) = urlparse(target_url)
print path_raw
path = path_raw.split('/')
id_file = path[3]
print id_file


google_directdl_frag = "https://docs.google.com/uc?export=download&id="
direct_dl = google_directdl_frag + id_file
print direct_dl



# print requests.head(direct_dl)
# print requests.get(direct_dl)
# print requests.options(direct_dl)
# print requests.put(direct_dl)
# r = requests.head(direct_dl)

# x = urllib.urlretrieve(direct_dl)
# print "this is x:"
# print x

# print "this is for line in x:"
# for line in x:
#   print line.read()

# print headers





import shutil, tempfile

req = urllib2.Request(direct_dl)
res = urllib2.urlopen(req)
temp = tempfile.TemporaryFile()
shutil.copyfileobj(res, temp)
temp.seek(0)




print "blha"
print temp.read()

import sys; sys.exit()






print "i am res.read()"
print res.read()

finalurl = res.geturl()

print res.info()

print "i am finalurl"
print finalurl

print " i am urllib2.urlopen(finalurl)"
print urllib2.urlopen(finalurl)

print "i am urllib.urlretrieve(finalurl)"
print urllib.urlretrieve(finalurl)

import cgi

response = urllib2.urlopen(target_url)
print "i am response"
print response

# for line in response:
#   print line.read()

_, params = cgi.parse_header(response.headers.get('Content-Disposition', ''))

print "i am cgi.parse.header"
print cgi.parse_header(response.headers.get('Content-Disposition', ''))

print "i am params"
print params

# 

# import posixpath
# import urlparse 

# path = urlparse.urlsplit(URL).path
# filename = posixpath.basename(path)




g = urllib2.urlopen(direct_dl, 'r')
i = g.info()
print "this is i"
print i

print g.read()


# print "this is for item in g:"
# for item in i:
#   print "me is here"
  
#   print item



=======
print requests.head(direct_dl)
print requests.get(direct_dl)
print requests.options(direct_dl)
print requests.put(direct_dl)
r = requests.head(direct_dl)

x = urllib.urlretrieve(direct_dl)
print "this is x:"
print x

print "this is for line in x:"
for line in x:
  print line

g = urllib.urlopen(direct_dl, 'r')


print "this is for item in g:"
for item in g:
  print "me is here"
  
  print item


print "this is item[1] ",  item[1]
  

# (scheme2, net_location2, path2, param2, query2, frag2) = urlparse(new_target)

# local_file =urllib.urlretrieve(direct_dl)
# files = local_file[0]

# with open(f1) as x:
#   print x.read()
