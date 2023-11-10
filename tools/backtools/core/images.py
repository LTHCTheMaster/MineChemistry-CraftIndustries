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

# Ingot
PALETTE_INGOT: tuple[tuple[int, int, int, int]] = (
	(0, 0, 0, 0), # Transparent
	makeColorTuple("6A"*3), # Border Top
	makeColorTuple("33"*3), # Border Bottom
	makeColorTuple("CF"*3),
	makeColorTuple("AE"*3),
	makeColorTuple("9A"*3),
	makeColorTuple("E4"*3),
	makeColorTuple("FA"*3), # Edges
	makeColorTuple("FF"*3), # Corner
)

INGOT: tuple[tuple[int]] = (
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

def colorEditionIngot(color: tuple[int, int, int, int], palette_index: int) -> tuple[int, int, int, int]:
	if i == 0: return (0, 0, 0, 0)
	return (round(color[0] * 0.651 + PALETTE_INGOT[palette_index][0] * 0.349), round(color[1] * 0.6509 + PALETTE_INGOT[palette_index][1] * 0.3491), round(color[2] * 0.649 + PALETTE_INGOT[palette_index][2] * 0.351), 255)

class IngotTextureImage(ItemTextureImage):
	def __init__(self, color: str):
		super().__init__(color)

	def draw(self):
		for y, line in enumerate(INGOT):
			for x, index in enumerate(line):
				if index == 0: continue
				self.image.putpixel((x, y), colorEditionIngot(self.color, index)) if index not in (7, 8) else self.image.putpixel((x, y), colorEditionIngot(colorEditionIngot(self.color, index), index))
# End of Ingot

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

# test = DustTextureImage("ffff00")
# test.show()

# test = DustTextureImage("4892d6")
# test.show()

# test = DustTextureImage("a82f2a")
# test.show()

# End of Test Area
