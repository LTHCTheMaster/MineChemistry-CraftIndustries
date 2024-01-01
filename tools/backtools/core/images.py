from os import listdir

# A lot of strange things to automatically define class and drawings usable for state value of elements,
# Usefull to quickly edit a state "representation", you just need to restart the program
POS_FILE_PATH = "tools/data/elements"
AFCIMGPATH = "tools/backtools/core/autofilecontainer/"

def filecutter(content: str) -> list[str]:
	lcontent = content.split('\t-\n')
	lcontent[0] = lcontent[0].replace('BLACK:','').replace('\t','')
	lcontent[1] = lcontent[1].replace('STOPPER_LIGHT_BLUE:','').replace('\t','')
	lcontent[2] = lcontent[2].replace('STOPPER_DARK_BLUE:','').replace('\t','')
	return lcontent.copy()

def define_drawBaseForm(desc: list[str]) -> str:
	return '\tdef drawBaseForm(self):\n\t\t' + '\n\t\t'.join([f"self.image.putpixel({i},BLACK)" for i in desc[0].split('\n')[1:-1]]) + '\n\t\tif self.natural_occurence == "decay":\n\t\t\t' + '\n\t\t\t'.join([f"self.image.putpixel({i},STOPPER_LIGHT_BLUE_DECAY)" for i in desc[1].split('\n')[1:-1]]) + '\n\t\telif self.natural_occurence == "synthetic":\n\t\t\t' + '\n\t\t\t'.join([f"self.image.putpixel({i},STOPPER_LIGHT_BLUE_SYNTHETIC)" for i in desc[1].split('\n')[1:-1]]) + '\n\t\telse:\n\t\t\t' + '\n\t\t\t'.join([f"self.image.putpixel({i},STOPPER_LIGHT_BLUE)" for i in desc[1].split('\n')[1:-1]]) + '\n\t\t' + '\n\t\t'.join([f"self.image.putpixel({i},STOPPER_DARK_BLUE)" for i in desc[2].split('\n')[1:]])

def define_colorInside(desc: list[str]) -> str:
	return '\tdef colorInside(self):\n\t\t' + '\n\t\t'.join([f"self.image.putpixel({i},self.color)" for i in desc])

def define_imageClass(prefix: str, descDrawBaseForm: list[str], descColorInside: list[str]) -> str:
	return f"class {prefix}_Image(BlankImage):\n\tdef __init__(self, color: str, natural_occurence: str):\n\t\tsuper().__init__(color, natural_occurence)\n"+define_drawBaseForm(descDrawBaseForm)+'\n'+define_colorInside(descColorInside)

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

class ItemTextureImage(PureBaseImage):
	def __init__(self, color: str):
		super().__init__(color)
		self.draw()

def colorEditionIngot(color: tuple[int, int, int, int], palette_index: int, palette: tuple[tuple[int, int, int, int]]) -> tuple[int, int, int, int]:
	if i == 0: return (0, 0, 0, 0)
	return (round(color[0] * 0.651 + palette[palette_index][0] * 0.349), round(color[1] * 0.6509 + palette[palette_index][1] * 0.3491), round(color[2] * 0.649 + palette[palette_index][2] * 0.351), 255)

class IngotTextureImage(ItemTextureImage):
	def __init__(self, color: str):
		super().__init__(color)

	def draw(self):
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
	(0, 0, 0, 1, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)

class CopperIngotTextureImage(IngotTextureImage):
	def __init__(self, color: str):
		super().__init__(color)
	
	def draw(self):
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
	(0, 0, 0, 1, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)

class IronIngotTextureImage(IngotTextureImage):
	def __init__(self, color: str):
		super().__init__(color)
	
	def draw(self):
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
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)

class GoldenIngotTextureImage(IngotTextureImage):
	def __init__(self, color: str):
		super().__init__(color)
	
	def draw(self):
		for y, line in enumerate(GOLDEN_INGOT):
			for x, index in enumerate(line):
				if index == 0: continue
				self.image.putpixel((x, y), colorEditionIngot(self.color, index, PALETTE_GOLDEN_INGOT)) if index not in (7, 8) else self.image.putpixel((x, y), colorEditionIngot(colorEditionIngot(self.color, index, PALETTE_GOLDEN_INGOT), index, PALETTE_GOLDEN_INGOT))
# End of Gold Based Ingot

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
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
	(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)

def colorEditionDust(color: tuple[int, int, int, int], palette_index: int) -> tuple[int, int, int, int]:
	if i == 0: return (0, 0, 0, 0)
	return (round(color[0] * 0.652 + PALETTE_DUST[palette_index][0] * 0.348), round(color[1] * 0.6509 + PALETTE_DUST[palette_index][1] * 0.3491), round(color[2] * 0.65 + PALETTE_DUST[palette_index][2] * 0.35), 255)

class DustTextureImage(ItemTextureImage):
	def __init__(self, color: str):
		super().__init__(color)

	def draw(self):
		for y, line in enumerate(DUST):
			for x, index in enumerate(line):
				if index == 0: continue
				self.image.putpixel((x, y), colorEditionDust(self.color, index)) if index not in (1, 2) else self.image.putpixel((x, y), colorEditionDust(colorEditionDust(self.color, index), index))
# End of Dust

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
