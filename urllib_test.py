import os
import urllib #for urlretrieve 
import urllib2
from urlparse import urlparse, urlunparse
import unittest
import weblogolib
#will need to install pyopenssl ndg-httpsclient pyasn1 to local machine to avoid SSL error

#weblogo license.txt file share url
target_url = 'https://www.dropbox.com/s/qgfto1ipfnxh0pq/LICENSE.txt?dl=0'

def From_URL_fileopen(target_url):
    """allows WebLogo to open files from URL locations"""

    #parsing url in component parts
    (scheme, net_location, path, param, query, frag) = urlparse(target_url)

    #checks if string is URL link
    
    if scheme != "http" and scheme !="https" and scheme != "ftp":
    	print "me is here"
    	raise ValueError("Cannot open url: %s" , target_url)
    #checks for dropbox link
    if net_location == 'www.dropbox.com':
	    #changes dropbox http link into download link
	    if query == "dl=0": query2 = "dl=1"

	    #rebuild download URL, with new query2 variable
	    target_url = urlunparse((scheme, net_location, path, param, query2,""))

    print path
    


   
    # checks for usable file type
    file_types = weblogolib._seq_extensions() 

        #retrieves file from download link to local machine
    retrieved = urllib.urlretrieve(target_url)

    #urlretrieve returns a tuple: (local file location, HTTPMessage instance )
    file_path = retrieved[0] 
    
    # Splits file extension from the path and normalizes it to lowercase.
    file_ext = os.path.splitext(file_path)[-1].lower()
#should return text of WebLogo's open source license

    if file_ext in file_types:
    	try:
    	#opens file to be read
    		with open(file_path) as f:
	    		print f.read()
    	except IOError:
            raise ValueError("The URL supplies unsupported file format: %s", 
            	From_URL_fileopen(target_url))




#pseudo unit test
class From_URL_fileopen_Tests(unittest.TestCase):

    def test_URLscheme(self):
        """test for http, https, or ftp scheme"""
        broken_url = "file://foo.txt"
        print "i am here"
        self.assertRaises(ValueError, From_URL_fileopen, (broken_url))
                         
    def test_URLfile_extension(self):
        """tests if file extension from URL is accepted format"""
        broken_text_ext = "http://foo.pdf"
        self.assertRaises(ValueError, From_URL_fileopen, (broken_text_ext))
                         


if __name__ == '__main__':
    unittest.main()