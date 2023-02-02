import requests
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

class baselib:

	def get_all(
			self,
			url,
			element
		):
		episodes = {}
		try:
			html = requests.get(url).text
		except:
			print( "An exception occured" )

		elem, attr = element
		ep = BeautifulSoup(html).body.find(elem, attrs=attr).text
		print(ep)
		return ep

	def get_text(
			self,
			url,
			element
		):
		try:
			html = requests.get(url).text
		except:
			print( "An exception occurred" )


		elem, attr = element
		text = BeautifulSoup(html).body.find(elem, attrs=attr).text

		return text