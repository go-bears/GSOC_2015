import os
import urllib #for urlretrieve 
import urllib2
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
