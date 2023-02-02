import baselib

class mangabilgini(baselib.baselib):

	def get_text(
			self,
			url
		):
		return super().get_text(url, ('div', {'class':'text-left'}))