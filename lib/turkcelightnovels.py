import baselib

class turkcelightnovels(baselib.baselib):

	def get_all(
			self,
			url
		):
		return super().get_all(url, ('div', {'class':'select-view'}))

	def get_text(
			self,
			url
		):
		return super().get_text(url, ('div', {'class':'reading-content'}))