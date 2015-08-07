import os
import urllib #for urlretrieve 
import urllib2
from urlparse import urlparse, urlunparse
#will need to install pyopenssl ndg-httpsclient pyasn1 to local machine to avoid SSL error

#weblogo license.txt file share url
target_url = 'https://www.dropbox.com/s/qgfto1ipfnxh0pq/LICENSE.txt?dl=0'

def From_URL_fileopen(target_url):
	"""allows WebLogo to open files from URL locations"""

	#parsing url in component parts
	parsed_header = urlparse(target_url)
	scheme = parsed_header[0]
	net_location = parsed_header[1] 
	path = parsed_header[2]
	param = parsed_header[3]
	query = parsed_header[4]

	#checks if string is URL link
	
	if scheme == "http" or "https" or "ftp":
	try:
		print scheme

	except IOError:
        raise ValueError("Cannot open url: %s" % (options.upload) )

	#checks for dropbox link
	if net_location == 'www.dropbox.com':
		#changes dropbox http link into download link
		try:
			if query == "dl=0":
				query2 = "dl=1"

			#rebuild download URL, with new query2 variable
			dl_url = urlunparse((scheme, net_location, path, param, query2,""))
			target_url = dl_url #overwrites target_url with direct download url
		
		except IOError:
        	raise ValueError("Cannot open dropbox url: %s" % (options.upload) )

	#retrieves file from download link to local machine
	retrieved = urllib.urlretrieve(target_url)

	#urlretrieve returns a tuple: (local file location, HTTPMessage instance )
	file_path = retrieved[0] 
	
	# Splits file extension from the path and normalizes it to lowercase.
	file_ext = os.path.splitext(file_path)[-1].lower()
   
   # checks for usable file type
    file_types = [".txt", ".pir", ".msf", ".phy", ".fasta", \
    			".flat", ".aln", ".nx", ".nex"]

	if file_ext in file_types:
		try:
			#opens file to be read
			with open(file_path) as f:
				print f.read()

		except IOError:
        	raise ValueError("The URL supplies unsupported file format: %s" % (options.upload) )		
			
From_URL_fileopen(target_url)
#should return text of WebLogo's open source license



# Here's our "unit tests".
class FromURLfileopen_Tests(unittest.TestCase):

    def test_URLscheme(self):
    	"""test for http, https, or ftp scheme"""
    	target_url = "htp."

        self.assertEqual()

    def test_netlocation(self):
    	net_location = "wwww.dropbox.com"

    def URLfile_extension_test(self):
    	"""tests if file extension from URL is accepted format"""
        self.failIf(IsOdd(2))

def main():
    unittest.main()

if __name__ == '__main__':
    main()