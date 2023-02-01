import requests
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

class baselib:

	def get_text(
			self,
			url,
			element
		):
		try:
			html = requests.get(url).text
		except:
			print( __name__ + ".api_request(): An exception occurred" )


		text = BeautifulSoup(html).body.find('div', {'class':'text-left'}).text

		return text