"""
Periodic Table(s?) toolbox
"""
from .elements import Tool, Image
import os

# Constants
BLANK_PERIOD = (181, 159, 119, 255) # RGBA Color
SIZE = (288, 148)           # Don't touch
RESCALED_SIZE = (1440, 740) # Don't touch

# Used to build a periodic table image
class PeriodicTableBuilder:
	"""
	Some tables
	"""
	def __init__(self, elements: Tool):
		"""
		Some tables
		"""
		self.image = Image.new("RGBA", SIZE, BLANK_PERIOD)
		self.ingot_image = Image.new("RGBA", SIZE, BLANK_PERIOD)
		self.block_image = Image.new("RGBA", SIZE, BLANK_PERIOD)
		self.elements = elements
		self.draw()
	
	def draw(self):
		"""
		Draw tables
		"""
		for i in  self.elements.elements:
			img, ingotimg, blockimg, coords = i.getDrawStruct()
			self.image.paste(img, coords.pos, img)
			if isinstance(ingotimg, Image.Image):
				self.ingot_image.paste(ingotimg, coords.pos, ingotimg)
			if isinstance(blockimg, Image.Image):
				self.block_image.paste(blockimg, coords.pos, blockimg)
	
	def show(self, cmd: list[str]):
		"""
		Show table(s)
		"""
		if cmd[0] == "ingot":
			tmp = self.ingot_image.resize(RESCALED_SIZE, Image.Resampling.NEAREST)
			tmp.show()
			return
		if cmd[0] == "block":
			tmp = self.block_image.resize(RESCALED_SIZE, Image.Resampling.NEAREST)
			tmp.show()
			return
		tmp = self.image.resize(RESCALED_SIZE, Image.Resampling.NEAREST)
		tmp.show()
	
	def save(self, path: str):
		"""
		Save Tables
		"""
		if not os.path.exists(path):
			os.makedirs(path)
		tmp = self.image.resize(RESCALED_SIZE, Image.Resampling.NEAREST)
		tmp.save(fp=path+"/000_TableauPNG.png",format="png")
		tmp = self.ingot_image.resize(RESCALED_SIZE, Image.Resampling.NEAREST)
		tmp.save(fp=path+"/000_TableauPNG_INGOT.png",format="png")
		tmp = self.block_image.resize(RESCALED_SIZE, Image.Resampling.NEAREST)
		tmp.save(fp=path+"/000_TableauPNG_BLOCK.png",format="png")
