"""
Images (big?) toolbox
"""
from os import listdir, path as pt, mkdir

# A lot of strange things to automatically define class and drawings usable for state value of elements,
# Usefull to quickly edit a state "representation", you just need to restart the program
POS_FILE_PATH = "tools/data/elements"
AFCIMGPATH = "tools/backtools/core/autofilecontainer/"

def filecutter(content: str) -> list[str]:
	"""
	Cut specific files in multiple parts
	"""
	lcontent = content.split('\t-\n')
	lcontent[0] = lcontent[0].replace('BLACK:','').replace('\t','')
	lcontent[1] = lcontent[1].replace('STOPPER_LIGHT_BLUE:','').replace('\t','')
	lcontent[2] = lcontent[2].replace('STOPPER_DARK_BLUE:','').replace('\t','')
	return lcontent.copy()

def define_drawBaseForm(desc: list[str]) -> str:
	"""
	Dynamically define the code for outline drawings of elements
	"""
	return '\tdef drawBaseForm(self):\n\t\t' + '\n\t\t'.join([f"self.image.putpixel({i},BLACK)" for i in desc[0].split('\n')[1:-1]]) + '\n\t\tif self.natural_occurence == "decay":\n\t\t\t' + '\n\t\t\t'.join([f"self.image.putpixel({i},STOPPER_LIGHT_BLUE_DECAY)" for i in desc[1].split('\n')[1:-1]]) + '\n\t\telif self.natural_occurence == "synthetic":\n\t\t\t' + '\n\t\t\t'.join([f"self.image.putpixel({i},STOPPER_LIGHT_BLUE_SYNTHETIC)" for i in desc[1].split('\n')[1:-1]]) + '\n\t\telse:\n\t\t\t' + '\n\t\t\t'.join([f"self.image.putpixel({i},STOPPER_LIGHT_BLUE)" for i in desc[1].split('\n')[1:-1]]) + '\n\t\t' + '\n\t\t'.join([f"self.image.putpixel({i},STOPPER_DARK_BLUE)" for i in desc[2].split('\n')[1:]])

def define_colorInside(desc: list[str]) -> str:
	"""
	Dynamically define the code for colour filling of elements
	"""
	return '\tdef colorInside(self):\n\t\t' + '\n\t\t'.join([f"self.image.putpixel({i},self.color)" for i in desc])

def define_imageClass(prefix: str, descDrawBaseForm: list[str], descColorInside: list[str]) -> str:
	"""
	"Dynamically" define new "Image" Class for elements
	"""
	return f"class {prefix}_Image(BlankImage):\n\tdef __init__(self, color: str, natural_occurence: str):\n\t\tsuper().__init__(color, natural_occurence)\n"+define_drawBaseForm(descDrawBaseForm)+'\n'+define_colorInside(descColorInside)

# do some file edition
tmp = ""
for i in listdir(POS_FILE_PATH):
	local_path = POS_FILE_PATH+'/'+i+'/'+i+'_'
	name = i
	empty_pos_file = open(local_path+'empty.pos','r')
	empty_desc = filecutter(empty_pos_file.read())
	empty_pos_file.close()
	color_pos_file = open(local_path+'color.pos','r')
	color_desc = color_pos_file.read().split('\n')
	color_pos_file.close()
	tmp += define_imageClass(i, empty_desc.copy(), color_desc.copy())+'\n'
file = open(AFCIMGPATH + "images.py",'w')
tmpfile = open(AFCIMGPATH + "base.txt", 'r')
file.write(tmpfile.read() + tmp)
tmpfile.close()
file.close()

from .autofilecontainer.images import *
# End of a lot of strange things

##############################################################################

# Other Textures

##################################
class ItemTextureImage(PureBaseImage):
	"""
	The base image for all "solid shaped" elements
	"""
	def __init__(self, color: str):
		"""
		The base image for all "solid shaped" elements
		"""
		super().__init__(color)
		self.draw()

def colorEditionIngot(color: tuple[int, int, int, int], palette_index: int, palette: tuple[tuple[int, int, int, int]]) -> tuple[int, int, int, int]:
	"""
	Too many strange code lines
	"""
	return (round(color[0] * 0.651 + palette[palette_index][0] * 0.349), round(color[1] * 0.6509 + palette[palette_index][1] * 0.3491), round(color[2] * 0.649 + palette[palette_index][2] * 0.351), 255)

class IngotTextureImage(ItemTextureImage):
	"""
	Base class for all ingot shape
	"""
	def __init__(self, color: str):
		"""
		Base class for all ingot shape
		"""
		super().__init__(color)

	def draw(self):
		"""
		Drawing method
		To Implement
		"""
		pass

# Copper Based Ingot
PALETTE_COPPER_INGOT: tuple[tuple[int, int, int, int]] = (
	(0, 0, 0, 0), # Transparent
	makeColorTuple("65"*3), # Border Top
	makeColorTuple("5D"*3), # Border Bottom
	makeColorTuple("4C"*3),
	makeColorTuple("95"*3),
	makeColorTuple("81"*3),
	makeColorTuple("72"*3),
	makeColorTuple("84"*3),
	makeColorTuple("CC"*3), # Edges
	makeColorTuple("E7"*3), # Corner
)

COPPER_INGOT: tuple[tuple[int]] = (
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 4, 2, 0, 0, 0),
	(0, 0, 0, 0, 1, 1, 1, 7, 4, 5, 5, 4, 7, 2, 0, 0),
	(0, 1, 1, 1, 4, 7, 7, 4, 5, 5, 4, 7, 7, 4, 2, 0),
	(1, 8, 4, 7, 7, 7, 4, 5, 5, 4, 7, 7, 8, 8, 7, 2),
	(1, 7, 8, 7, 7, 4, 4, 4, 7, 8, 8, 8, 4, 5, 5, 3),
	(1, 7, 4, 8, 7, 7, 8, 8, 8, 7, 4, 4, 5, 6, 5, 3),
	(1, 7, 5, 4, 9, 8, 4, 5, 5, 4, 4, 5, 6, 6, 4, 3),
	(1, 7, 5, 5, 8, 4, 5, 5, 4, 4, 5, 6, 5, 3, 3, 0),
	(0, 1, 4, 5, 8, 5, 5, 4, 4, 5, 3, 3, 3, 0, 0, 0),
	(0, 0, 1, 5, 7, 5, 4, 3, 3, 3, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 1, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0),
)

class CopperIngotTextureImage(IngotTextureImage):
	"""
	Copper ingot based image
	"""
	def __init__(self, color: str):
		"""
		Copper ingot based image
		"""
		super().__init__(color)
	
	def draw(self):
		"""
		Drawings
		"""
		for y, line in enumerate(COPPER_INGOT):
			for x, index in enumerate(line):
				if index == 0: continue
				self.image.putpixel((x, y), colorEditionIngot(self.color, index, PALETTE_COPPER_INGOT)) if index not in (8, 9) else self.image.putpixel((x, y), colorEditionIngot(colorEditionIngot(self.color, index, PALETTE_COPPER_INGOT), index, PALETTE_COPPER_INGOT))
# End of Copper Based Ingot

# Iron Based Ingot
PALETTE_IRON_INGOT: tuple[tuple[int, int, int, int]] = (
	(0, 0, 0, 0), # Transparent
	makeColorTuple("5E"*3), # Border Top
	makeColorTuple("35"*3), # Border Bottom
	makeColorTuple("72"*3), # Border Right and one "face" of the ingot
	makeColorTuple("82"*3),
	makeColorTuple("A8"*3),
	makeColorTuple("58"*3),
	makeColorTuple("FF"*3),
	makeColorTuple("D8"*3),
)

IRON_INGOT: tuple[tuple[int]] = (
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 5, 5, 3, 0, 0, 0),
	(0, 0, 0, 0, 1, 1, 1, 5, 8, 8, 8, 8, 5, 3, 0, 0),
	(0, 1, 1, 1, 5, 8, 8, 8, 8, 8, 8, 8, 8, 5, 3, 0),
	(1, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 8, 3),
	(1, 5, 7, 8, 8, 8, 8, 8, 8, 7, 7, 7, 8, 3, 5, 2),
	(1, 5, 5, 7, 8, 8, 7, 7, 7, 8, 4, 3, 3, 4, 5, 2),
	(1, 5, 5, 5, 7, 7, 8, 4, 3, 3, 3, 3, 5, 5, 5, 2),
	(1, 4, 5, 5, 8, 4, 3, 3, 3, 3, 5, 5, 4, 2, 2, 0),
	(0, 1, 4, 5, 8, 4, 3, 3, 4, 4, 2, 2, 2, 0, 0, 0),
	(0, 0, 1, 4, 5, 4, 6, 2, 2, 2, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0),
)

class IronIngotTextureImage(IngotTextureImage):
	"""
	Iron ingot based image
	"""
	def __init__(self, color: str):
		"""
		Iron ingot based image
		"""
		super().__init__(color)
	
	def draw(self):
		"""
		Drawings
		"""
		for y, line in enumerate(IRON_INGOT):
			for x, index in enumerate(line):
				if index == 0: continue
				self.image.putpixel((x, y), colorEditionIngot(self.color, index, PALETTE_IRON_INGOT)) if index not in (7, 8) else self.image.putpixel((x, y), colorEditionIngot(colorEditionIngot(self.color, index, PALETTE_IRON_INGOT), index, PALETTE_IRON_INGOT))
# End of Iron Based Ingot

# Gold Based Ingot
PALETTE_GOLDEN_INGOT: tuple[tuple[int, int, int, int]] = (
	(0, 0, 0, 0), # Transparent
	makeColorTuple("6A"*3), # Border Top
	makeColorTuple("33"*3), # Border Bottom
	makeColorTuple("CC"*3),
	makeColorTuple("AB"*3),
	makeColorTuple("97"*3),
	makeColorTuple("E1"*3),
	makeColorTuple("FA"*3), # Edges
	makeColorTuple("FF"*3), # Corner
)

GOLDEN_INGOT: tuple[tuple[int]] = (
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 3, 3, 1, 0, 0, 0),
	(0, 0, 0, 0, 1, 1, 1, 6, 6, 6, 6, 6, 6, 1, 0, 0),
	(0, 1, 1, 1, 3, 6, 6, 6, 6, 6, 6, 6, 6, 3, 2, 0),
	(1, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 6, 2),
	(1, 3, 7, 6, 6, 6, 6, 6, 6, 7, 7, 7, 6, 5, 3, 2),
	(1, 3, 6, 7, 6, 6, 7, 7, 7, 6, 4, 5, 5, 5, 3, 2),
	(1, 3, 6, 3, 8, 7, 6, 4, 5, 5, 5, 5, 4, 3, 3, 2),
	(1, 4, 6, 3, 6, 4, 5, 5, 5, 5, 4, 3, 3, 2, 2, 0),
	(0, 1, 4, 3, 6, 4, 5, 5, 4, 4, 2, 2, 2, 0, 0, 0),
	(0, 0, 1, 4, 3, 4, 4, 2, 2, 2, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0),
)

class GoldenIngotTextureImage(IngotTextureImage):
	"""
	Gold ingot based image
	"""
	def __init__(self, color: str):
		"""
		Gold ingot based image
		"""
		super().__init__(color)
	
	def draw(self):
		for y, line in enumerate(GOLDEN_INGOT):
			"""
		Drawings
		"""
			for x, index in enumerate(line):
				if index == 0: continue
				self.image.putpixel((x, y), colorEditionIngot(self.color, index, PALETTE_GOLDEN_INGOT)) if index not in (7, 8) else self.image.putpixel((x, y), colorEditionIngot(colorEditionIngot(self.color, index, PALETTE_GOLDEN_INGOT), index, PALETTE_GOLDEN_INGOT))
# End of Gold Based Ingot

# Special Ingot
PALETTE_SPECIAL_INGOT: tuple[tuple[int, int, int, int]] = (
	(0, 0, 0, 0), # Transparent
	makeColorTuple("15"*3), # Border
	makeColorTuple("69"*3),
	makeColorTuple("3F"*3), # Edges
	makeColorTuple("20"*3),
	makeColorTuple("2A"*3),
)

SPECIAL_INGOT: tuple[tuple[int]] = (
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 1, 0, 0, 0),
	(0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0),
	(0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0),
	(1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 1),
	(1, 5, 3, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 1),
	(1, 5, 5, 3, 2, 2, 2, 3, 5, 5, 4, 4, 4, 4, 4, 1),
	(1, 5, 5, 5, 3, 3, 3, 5, 5, 4, 4, 4, 4, 4, 3, 1),
	(1, 3, 5, 5, 3, 5, 5, 5, 5, 5, 5, 3, 1, 1, 1, 0),
	(0, 1, 3, 5, 3, 5, 3, 5, 5, 1, 1, 1, 0, 0, 0, 0),
	(0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
)

class SpecialIngotTextureImage(IngotTextureImage):
	"""
	Special ingot image
	"""
	def __init__(self, color: str):
		"""
		Special ingot image
		"""
		super().__init__(color)
	
	def draw(self):
		"""
		Drawings
		"""
		for y, line in enumerate(SPECIAL_INGOT):
			for x, index in enumerate(line):
				if index == 0: continue
				self.image.putpixel((x, y), colorEditionIngot(self.color, index, PALETTE_SPECIAL_INGOT))
# End of Special Ingot

# Speciall Ingot
PALETTE_SPECIALL_INGOT: tuple[tuple[int, int, int, int]] = (
	(0, 0, 0, 0),
	(76, 76, 76, 255),
	(112, 112, 112, 255),
	(61, 61, 61, 255)
)

SPECIALL_INGOT: tuple[tuple[int]] = (
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 1, 0, 0, 0),
	(0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 0, 0),
	(0, 1, 1, 1, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 3, 0),
	(1, 1, 2, 2, 3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 1, 1),
	(1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 3, 3, 2, 2, 2, 1),
	(1, 1, 1, 1, 2, 1, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1),
	(1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1),
	(1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 0),
	(0, 1, 1, 1, 1, 1, 2, 2, 2, 1, 3, 3, 0, 0, 0, 0),
	(0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)

class SpeciallIngotTextureImage(IngotTextureImage):
	"""
	Speciall ingot image
	"""
	def __init__(self, color: str):
		"""
		Speciall ingot image
		"""
		super().__init__(color)
	
	def draw(self):
		"""
		Drawings
		"""
		for y, line in enumerate(SPECIALL_INGOT):
			for x, index in enumerate(line):
				if index == 0: continue
				self.image.putpixel((x, y), colorEditionIngot(self.color, index, PALETTE_SPECIALL_INGOT))
# End of Speciall Ingot

# Dust
PALETTE_DUST: tuple[tuple[int, int, int, int]] = (
	(0, 0, 0, 0), # Transparent
	makeColorTuple("1E"*3), # Border Top
	makeColorTuple("0C"*3), # Border Bottom
	makeColorTuple("61"*3),
	makeColorTuple("70"*3),
	makeColorTuple("3C"*3),
	makeColorTuple("2D"*3),
	makeColorTuple("23"*3),
	makeColorTuple("30"*3)
)

DUST: tuple[tuple[int]] = (
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 1, 5, 3, 1, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 1, 3, 4, 3, 6, 2, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 1, 3, 4, 3, 5, 4, 6, 2, 0, 0, 0, 0),
	(0, 0, 0, 1, 3, 3, 3, 4, 3, 6, 8, 6, 2, 0, 0, 0),
	(0, 0, 1, 5, 4, 3, 5, 6, 4, 5, 6, 3, 7, 2, 0, 0),
	(0, 0, 1, 3, 5, 3, 4, 3, 5, 6, 6, 8, 6, 2, 0, 0),
	(0, 0, 2, 6, 3, 4, 3, 5, 6, 3, 6, 6, 7, 2, 0, 0),
	(0, 0, 0, 2, 6, 3, 5, 6, 8, 6, 6, 7, 2, 0, 0, 0),
	(0, 0, 0, 0, 2, 2, 7, 6, 6, 7, 2, 2, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0),
)

def colorEditionDust(color: tuple[int, int, int, int], palette_index: int, palette: tuple[tuple[int, int, int, int]]) -> tuple[int, int, int, int]:
	"""
	Too many strange code lines
	"""
	return (round(color[0] * 0.652 + palette[palette_index][0] * 0.348), round(color[1] * 0.6509 + palette[palette_index][1] * 0.3491), round(color[2] * 0.65 + palette[palette_index][2] * 0.35), 255)

class DustTextureImage(ItemTextureImage):
	"""
	Dust image
	"""
	def __init__(self, color: str):
		"""
		Dust image
		"""
		super().__init__(color)

	def draw(self):
		"""
		Drawings
		"""
		for y, line in enumerate(DUST):
			for x, index in enumerate(line):
				if index == 0: continue
				self.image.putpixel((x, y), colorEditionDust(self.color, index, PALETTE_DUST)) if index not in (1, 2) else self.image.putpixel((x, y), colorEditionDust(colorEditionDust(self.color, index, PALETTE_DUST), index, PALETTE_DUST))
# End of Dust

class TemplateImg(PureBaseImage):
	"""
	Template Image
	"""
	def __init__(self, color: str, model: tuple[tuple[int]], palette: tuple[tuple[int, int, int, int]]):
		"""
		Template Image
		"""
		super().__init__(color)
		self.model = model
		self.palette = palette
		self.draw()
	
	def draw(self):
		"""
		Drawings
		"""
		for y, line in enumerate(self.model):
			for x, index in enumerate(line):
				if index == 0: continue
				self.image.putpixel((x, y), self.palette[index])

class TemplateImageExporter:
	"""
	used to export template images
	"""
	def __init__(self):
		"""
		used to export template images
		"""
		self.ingot0Template: TemplateImg = TemplateImg("000000", COPPER_INGOT, PALETTE_COPPER_INGOT)
		self.ingot1Template: TemplateImg = TemplateImg("000000", IRON_INGOT, PALETTE_IRON_INGOT)
		self.ingot2Template: TemplateImg = TemplateImg("000000", GOLDEN_INGOT, PALETTE_GOLDEN_INGOT)
		self.ingot3Template: TemplateImg = TemplateImg("000000", SPECIAL_INGOT, PALETTE_SPECIAL_INGOT)
		self.dustTemplate: TemplateImg = TemplateImg("000000", DUST, PALETTE_DUST)
	
	def export(self, path: str):
		"""
		export templates images
		"""
		if not pt.exists(path):
			mkdir(path)
		self.ingot0Template.save(path+'/ingot0_template')
		self.ingot1Template.save(path+'/ingot1_template')
		self.ingot2Template.save(path+'/ingot2_template')
		self.ingot3Template.save(path+'/ingot3_template')
		self.dustTemplate.save(path+'/dust_template')
##################################

##################################
class BlockTextureImage(PureBaseImage):
	"""
	The base image for all blocks for "solid shaped" elements
	"""
	def __init__(self, color: str):
		"""
		The base image for all blocks for "solid shaped" elements
		"""
		super().__init__(color)
		self.draw()

class IngotBlockTextureImage(BlockTextureImage):
	"""
	Base class for all blocks from ingot shape
	"""
	def __init__(self, color: str):
		"""
		Base class for all blocks from ingot shape
		"""
		super().__init__(color)

	def draw(self):
		"""
		Drawing method
		To Implement
		"""
		pass

# Dust
PALETTE_DUST_BLOCK: tuple[tuple[int, int, int, int]] = (
	makeColorTuple("58"*3),
	makeColorTuple("4C"*3),
	makeColorTuple("40"*3),
	makeColorTuple("38"*3),
	makeColorTuple("29"*3)
)

DUST_BLOCK: tuple[tuple[int]] = (
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 1, 1, 0, 1, 1, 2, 2, 2, 1, 1, 0, 1, 1, 1, 0),
	(0, 1, 1, 0, 2, 2, 4, 2, 2, 2, 2, 2, 1, 2, 1, 0),
	(0, 1, 1, 2, 1, 3, 3, 4, 4, 3, 3, 2, 4, 2, 1, 0),
	(0, 0, 1, 2, 3, 3, 4, 3, 2, 4, 3, 3, 2, 0, 0, 0),
	(0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 0, 2, 1, 0),
	(0, 1, 4, 2, 3, 4, 4, 4, 4, 4, 4, 3, 3, 3, 1, 0),
	(0, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 2, 0),
	(0, 2, 2, 1, 3, 4, 4, 4, 4, 4, 4, 3, 3, 3, 1, 0),
	(0, 1, 2, 0, 3, 3, 4, 2, 3, 4, 3, 3, 3, 2, 1, 0),
	(0, 1, 2, 3, 3, 4, 4, 4, 0, 4, 4, 3, 2, 2, 0, 0),
	(0, 1, 1, 2, 3, 3, 4, 3, 4, 4, 3, 3, 3, 4, 1, 0),
	(0, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 0),
	(0, 0, 1, 4, 2, 0, 2, 3, 3, 4, 2, 2, 1, 2, 1, 0),
	(0, 1, 1, 1, 0, 0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)

class DustBlockTextureImage(BlockTextureImage):
	"""
	"Dust" block textures
	"""
	def __init__(self, color: str):
		"""
		"Dust" block textures
		"""
		super().__init__(color)
	
	def draw(self):
		"""
		Drawings
		"""
		for y, line in enumerate(DUST_BLOCK):
			for x, index in enumerate(line):
				self.image.putpixel((x, y), colorEditionDust(self.color, index, PALETTE_DUST_BLOCK))
# End of Dust

# Copper Based Block
PALETTE_COPPER_BLOCK: tuple[tuple[int, int, int, int]] = (
	(149, 149, 149, 255),
	(140, 140, 140, 255),
	(131, 131, 131, 255),
	(122, 122, 122, 255),
	(103, 103, 103, 255),
	(112, 112, 112, 255),
	(92, 92, 92, 255),
	(84, 84, 84, 255)
)

COPPER_BLOCK: tuple[tuple[int]] = (
	(0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 2, 3, 4),
	(0, 2, 2, 3, 3, 2, 2, 1, 0, 1, 1, 1, 3, 3, 5, 6),
	(0, 2, 0, 5, 2, 2, 1, 0, 1, 1, 1, 3, 0, 5, 5, 6),
	(0, 3, 5, 6, 2, 1, 0, 1, 2, 1, 3, 3, 5, 6, 5, 7),
	(0, 3, 2, 2, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 3, 7),
	(0, 2, 2, 1, 1, 1, 2, 2, 3, 3, 4, 6, 4, 3, 5, 7),
	(0, 2, 1, 0, 1, 2, 2, 3, 3, 4, 6, 4, 3, 5, 5, 7),
	(0, 1, 0, 1, 2, 2, 3, 3, 4, 6, 4, 3, 3, 5, 2, 7),
	(0, 0, 1, 2, 2, 3, 5, 4, 6, 4, 3, 3, 5, 2, 2, 7),
	(0, 1, 2, 2, 3, 5, 5, 4, 4, 3, 3, 3, 2, 2, 1, 6),
	(0, 2, 2, 3, 5, 5, 4, 5, 3, 3, 3, 2, 2, 1, 0, 6),
	(0, 2, 3, 5, 5, 5, 5, 3, 3, 5, 2, 2, 1, 0, 1, 6),
	(0, 3, 0, 5, 4, 5, 3, 3, 5, 2, 2, 1, 0, 5, 2, 7),
	(0, 5, 5, 6, 5, 3, 5, 5, 2, 2, 1, 1, 5, 6, 3, 7),
	(0, 4, 6, 5, 3, 5, 5, 2, 2, 1, 1, 1, 2, 3, 3, 6),
	(1, 6, 4, 6, 6, 7, 6, 7, 4, 4, 4, 6, 6, 7, 6, 6)
)

class CopperBlockTextureImage(IngotBlockTextureImage):
	"""
	"Copper" block textures
	"""
	def __init__(self, color: str):
		"""
		"Copper" block textures
		"""
		super().__init__(color)
	
	def draw(self):
		"""
		Drawings
		"""
		for y, line in enumerate(COPPER_BLOCK):
			for x, index in enumerate(line):
				self.image.putpixel((x, y), colorEditionIngot(self.color, index, PALETTE_COPPER_BLOCK))
# End of Copper Based Block

# Iron Based Block
PALETTE_IRON_BLOCK: tuple[tuple[int, int, int, int]] = (
	(183, 183, 183, 255),
	(168, 168, 168, 255),
	(217, 217, 217, 255),
	(211, 211, 211, 255),
	(209, 209, 209, 255),
	(205, 205, 205, 255),
	(160, 160, 160, 255),
	(151, 151, 151, 255),
	(195, 195, 195, 255),
	(199, 199, 199, 255),
	(189, 189, 189, 255)
)

IRON_BLOCK: tuple[tuple[int]] = (
	(0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0),
	(1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5, 1),
	(1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6),
	(7, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 7),
	(1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 6),
	(1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6),
	(7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 7),
	(1, 2, 2, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 6),
	(1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6),
	(7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 7),
	(1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 5, 5, 5, 5, 6),
	(1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6),
	(7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 7),
	(1, 2, 2, 2, 2, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 6),
	(1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6),
	(1, 1, 1, 1, 1, 1, 1, 6, 6, 1, 6, 6, 6, 6, 6, 6)
)

class IronBlockTextureImage(IngotBlockTextureImage):
	"""
	"Iron" block textures
	"""
	def __init__(self, color: str):
		"""
		"Iron" block textures
		"""
		super().__init__(color)
	
	def draw(self):
		"""
		Drawings
		"""
		for y, line in enumerate(IRON_BLOCK):
			for x, index in enumerate(line):
				self.image.putpixel((x, y), colorEditionIngot(self.color, index, PALETTE_IRON_BLOCK))
# End of Iron Based Block

# Gold Based Block
PALETTE_GOLDEN_BLOCK: tuple[tuple[int, int, int, int]] = (
	(195, 195, 195, 255),
	(188, 188, 188, 255),
	(159, 159, 159, 255),
	(235, 235, 235, 255),
	(243, 243, 243, 255),
	(216, 216, 216, 255),
	(205, 205, 205, 255),
	(209, 209, 209, 255),
	(151, 151, 151, 255)
)

GOLDEN_BLOCK: tuple[tuple[int]] = (
	(0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 2),
	(0, 3, 4, 4, 5, 5, 3, 3, 3, 5, 5, 6, 6, 3, 3, 2),
	(0, 4, 6, 6, 7, 3, 5, 5, 6, 0, 1, 1, 0, 7, 3, 2),
	(0, 4, 6, 7, 3, 5, 5, 7, 6, 0, 0, 0, 7, 7, 5, 2),
	(1, 5, 7, 5, 5, 5, 7, 6, 0, 0, 6, 7, 7, 6, 5, 2),
	(1, 5, 5, 5, 5, 7, 6, 0, 0, 6, 5, 5, 6, 0, 1, 8),
	(0, 3, 5, 5, 7, 7, 7, 6, 6, 5, 5, 6, 0, 1, 1, 8),
	(0, 3, 5, 7, 7, 7, 6, 6, 7, 7, 6, 0, 0, 1, 0, 8),
	(1, 5, 7, 7, 7, 6, 6, 7, 7, 6, 6, 0, 0, 0, 6, 2),
	(1, 5, 7, 7, 6, 6, 7, 7, 6, 6, 6, 6, 0, 7, 6, 2),
	(1, 6, 7, 6, 6, 5, 5, 6, 6, 6, 6, 6, 5, 7, 0, 8),
	(1, 0, 6, 6, 5, 5, 6, 0, 0, 6, 0, 5, 5, 6, 0, 8),
	(1, 0, 6, 5, 5, 6, 0, 1, 1, 0, 7, 7, 6, 0, 6, 2),
	(1, 1, 7, 7, 6, 0, 1, 1, 0, 6, 6, 6, 0, 0, 7, 2),
	(1, 0, 1, 0, 0, 1, 1, 0, 6, 6, 0, 0, 6, 7, 5, 8),
	(2, 2, 8, 2, 2, 8, 8, 8, 2, 2, 8, 8, 2, 2, 8, 8)
)

class GoldenBlockTextureImage(IngotBlockTextureImage):
	"""
	"Gold" block textures
	"""
	def __init__(self, color: str):
		"""
		"Gold" block textures
		"""
		super().__init__(color)
	
	def draw(self):
		"""
		Drawings
		"""
		for y, line in enumerate(GOLDEN_BLOCK):
			for x, index in enumerate(line):
				self.image.putpixel((x, y), colorEditionIngot(self.color, index, PALETTE_GOLDEN_BLOCK))
# End of Gold Based Block
##################################

# End of Other Textures

##############################################################################

# Test Area

# test = CopperIngotTextureImage("ffff00")
# test.show()

# test = CopperIngotTextureImage("4892d6")
# test.show()

# test = CopperIngotTextureImage("a82f2a")
# test.show()

# End of Test Area
