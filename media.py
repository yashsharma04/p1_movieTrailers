import webbrowser
class Movie():
	""" Summary of Movie class
		class containing the movie details as its parameters
		Attributes:
			title: stores the title of the movie
			storyline: stores the storyline of the movie 
			poster_image_url : stores the image url
			trailer_youtube_url : stores the url of the youtube video
""" 
	def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
		# Inits Movie class with title ,storyline ,poster_image_url,trailer_youtube_url 
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)