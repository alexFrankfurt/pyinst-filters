from instagram_filters.filter import Filter
from instagram_filters.decorations.vignette import Vignette

class Lomo(Vignette):
	
	def apply(self):
		self.execute("convert {filename} -channel R -level 33% -channel G -level 33% {filename}")
		self.vignette()