from .elements import Tool, Image
import os

BLANK_PERIOD = (181, 159, 119, 255)
SIZE = (288, 148)
RESCALED_SIZE = (1440, 740)

class PeriodicTableBuilder:
	def __init__(self, elements: Tool):
		self.image = Image.new("RGBA", SIZE, BLANK_PERIOD)
		self.ingot_image = Image.new("RGBA", SIZE, BLANK_PERIOD)
		self.elements = elements
		self.draw()
	
	def draw(self):
		for i in  self.elements.elements:
			img, ingotimg, coords = i.getDrawStruct()
			self.image.paste(img, coords.pos, img)
			if isinstance(ingotimg, Image.Image):
				self.ingot_image.paste(ingotimg, coords.pos, ingotimg)
	
	def show(self):
		tmp = self.image.resize(RESCALED_SIZE, Image.Resampling.NEAREST)
		tmp.show()
	
	def save(self, path: str):
		if not os.path.exists(path):
			os.makedirs(path)
		tmp = self.image.resize(RESCALED_SIZE, Image.Resampling.NEAREST)
		tmp.save(fp=path+"/000_TableauPNG.png",format="png")
		tmp = self.ingot_image.resize(RESCALED_SIZE, Image.Resampling.NEAREST)
		tmp.save(fp=path+"/000_TableauPNG_INGOT.png",format="png")
