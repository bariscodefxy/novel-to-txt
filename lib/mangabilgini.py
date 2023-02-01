import baselib

class Mangabilgini(baselib.baselib):

	def get_text(
			self,
			url
		):
		return super().get_text(url, ('url', {'class':'text-left'}))