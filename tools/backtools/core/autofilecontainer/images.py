from PIL import Image

def makeColorTuple(color: str) -> tuple[int, int, int, int]:
	r, g, b = color[:2], color[2:4], color[4:]
	red = int(r, 16)
	green = int(g, 16)
	blue = int(b, 16)
	return (red, green, blue, 255)

def colorMixer(maincolor: tuple[int, int, int, int], secondarycolor: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
	return makeColorDarker((int((maincolor[0]+secondarycolor[0])/2.1), int((maincolor[1]+secondarycolor[1])/2.4), int((maincolor[2]+secondarycolor[2])/2.2), 255))

def makeColorDarker(color: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
	return (int(color[0]*0.88), int(color[1]*0.85), int(color[2]*0.75), 255)


BLACK = (0,0,0,255)
NATOCC_DECAY = (45, 236, 67, 255)
NATOCC_SYNTHETIC = (215, 159, 199, 255)
STOPPER_LIGHT_BLUE = (23,84,135,255)
STOPPER_LIGHT_BLUE_DECAY = colorMixer(STOPPER_LIGHT_BLUE, NATOCC_DECAY)
STOPPER_LIGHT_BLUE_SYNTHETIC = colorMixer(STOPPER_LIGHT_BLUE, NATOCC_SYNTHETIC)
STOPPER_DARK_BLUE = (10,38,62,255)
BLANK_IMAGE = (255, 255, 255, 0)
SIZE = (16, 16)

class PureBaseImage:
	def __init__(self, color: str):
		self.image:Image.Image = Image.new("RGBA", SIZE, BLANK_IMAGE)
		self.color: tuple[int, int, int, int] = makeColorTuple(color)
	
	def show(self):
		tmp = self.image.resize((512,512),Image.Resampling.NEAREST)
		tmp.show()
	def getImage(self) -> Image.Image:
		return self.image
	def save(self, path: str):
		self.image.save(fp=path+'.png',format="png")
	
	def draw(self):
		pass

class BlankImage(PureBaseImage):
	def __init__(self, color: str, natural_occurence: str):
		super().__init__(color)
		self.natural_occurence = natural_occurence
		self.draw()
	
	def drawBaseForm(self):
		pass
	def colorInside(self):
		pass
	def draw(self):
		self.drawBaseForm()
		self.colorInside()
class gas_Image(BlankImage):
	def __init__(self, color: str, natural_occurence: str):
		super().__init__(color, natural_occurence)
	def drawBaseForm(self):
		self.image.putpixel((4, 5),BLACK)
		self.image.putpixel((4, 6),BLACK)
		self.image.putpixel((4, 7),BLACK)
		self.image.putpixel((4, 8),BLACK)
		self.image.putpixel((4, 9),BLACK)
		self.image.putpixel((11, 5),BLACK)
		self.image.putpixel((11, 6),BLACK)
		self.image.putpixel((11, 7),BLACK)
		self.image.putpixel((11, 8),BLACK)
		self.image.putpixel((11, 9),BLACK)
		self.image.putpixel((5, 3),BLACK)
		self.image.putpixel((5, 4),BLACK)
		self.image.putpixel((5, 5),BLACK)
		self.image.putpixel((5, 9),BLACK)
		self.image.putpixel((5, 10),BLACK)
		self.image.putpixel((5, 11),BLACK)
		self.image.putpixel((10, 3),BLACK)
		self.image.putpixel((10, 4),BLACK)
		self.image.putpixel((10, 5),BLACK)
		self.image.putpixel((10, 9),BLACK)
		self.image.putpixel((10, 10),BLACK)
		self.image.putpixel((10, 11),BLACK)
		self.image.putpixel((6, 1),BLACK)
		self.image.putpixel((7, 1),BLACK)
		self.image.putpixel((8, 1),BLACK)
		self.image.putpixel((9, 1),BLACK)
		self.image.putpixel((6, 2),BLACK)
		self.image.putpixel((6, 3),BLACK)
		self.image.putpixel((9, 2),BLACK)
		self.image.putpixel((9, 3),BLACK)
		self.image.putpixel((6, 11),BLACK)
		self.image.putpixel((6, 12),BLACK)
		self.image.putpixel((9, 11),BLACK)
		self.image.putpixel((9, 12),BLACK)
		if self.natural_occurence == "decay":
			self.image.putpixel((6, 13),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((7, 13),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((8, 13),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((9, 13),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((7, 11),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((8, 11),STOPPER_LIGHT_BLUE_DECAY)
		elif self.natural_occurence == "synthetic":
			self.image.putpixel((6, 13),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((7, 13),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((8, 13),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((9, 13),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((7, 11),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((8, 11),STOPPER_LIGHT_BLUE_SYNTHETIC)
		else:
			self.image.putpixel((6, 13),STOPPER_LIGHT_BLUE)
			self.image.putpixel((7, 13),STOPPER_LIGHT_BLUE)
			self.image.putpixel((8, 13),STOPPER_LIGHT_BLUE)
			self.image.putpixel((9, 13),STOPPER_LIGHT_BLUE)
			self.image.putpixel((7, 11),STOPPER_LIGHT_BLUE)
			self.image.putpixel((8, 11),STOPPER_LIGHT_BLUE)
		self.image.putpixel((7, 12),STOPPER_DARK_BLUE)
		self.image.putpixel((8, 12),STOPPER_DARK_BLUE)
	def colorInside(self):
		self.image.putpixel((5, 6),self.color)
		self.image.putpixel((5, 7),self.color)
		self.image.putpixel((6, 6),self.color)
		self.image.putpixel((6, 7),self.color)
		self.image.putpixel((7, 6),self.color)
		self.image.putpixel((7, 7),self.color)
		self.image.putpixel((8, 6),self.color)
		self.image.putpixel((8, 7),self.color)
		self.image.putpixel((9, 6),self.color)
		self.image.putpixel((9, 7),self.color)
		self.image.putpixel((10, 6),self.color)
		self.image.putpixel((10, 7),self.color)
		self.image.putpixel((6, 4),self.color)
		self.image.putpixel((6, 5),self.color)
		self.image.putpixel((7, 4),self.color)
		self.image.putpixel((7, 5),self.color)
		self.image.putpixel((8, 4),self.color)
		self.image.putpixel((8, 5),self.color)
		self.image.putpixel((9, 4),self.color)
		self.image.putpixel((9, 5),self.color)
		self.image.putpixel((7, 2),self.color)
		self.image.putpixel((7, 3),self.color)
		self.image.putpixel((8, 2),self.color)
		self.image.putpixel((8, 3),self.color)
class liquid_Image(BlankImage):
	def __init__(self, color: str, natural_occurence: str):
		super().__init__(color, natural_occurence)
	def drawBaseForm(self):
		self.image.putpixel((5, 4),BLACK)
		self.image.putpixel((5, 5),BLACK)
		self.image.putpixel((5, 6),BLACK)
		self.image.putpixel((5, 7),BLACK)
		self.image.putpixel((5, 8),BLACK)
		self.image.putpixel((5, 9),BLACK)
		self.image.putpixel((5, 10),BLACK)
		self.image.putpixel((5, 11),BLACK)
		self.image.putpixel((5, 12),BLACK)
		self.image.putpixel((5, 13),BLACK)
		self.image.putpixel((5, 14),BLACK)
		self.image.putpixel((10, 4),BLACK)
		self.image.putpixel((10, 5),BLACK)
		self.image.putpixel((10, 6),BLACK)
		self.image.putpixel((10, 7),BLACK)
		self.image.putpixel((10, 8),BLACK)
		self.image.putpixel((10, 9),BLACK)
		self.image.putpixel((10, 10),BLACK)
		self.image.putpixel((10, 11),BLACK)
		self.image.putpixel((10, 12),BLACK)
		self.image.putpixel((10, 13),BLACK)
		self.image.putpixel((10, 14),BLACK)
		self.image.putpixel((6, 15),BLACK)
		self.image.putpixel((7, 15),BLACK)
		self.image.putpixel((8, 15),BLACK)
		self.image.putpixel((9, 15),BLACK)
		self.image.putpixel((6, 3),BLACK)
		self.image.putpixel((6, 4),BLACK)
		self.image.putpixel((9, 3),BLACK)
		self.image.putpixel((9, 4),BLACK)
		self.image.putpixel((6, 14),BLACK)
		self.image.putpixel((9, 14),BLACK)
		if self.natural_occurence == "decay":
			self.image.putpixel((6, 2),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((7, 2),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((8, 2),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((9, 2),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((7, 4),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((8, 4),STOPPER_LIGHT_BLUE_DECAY)
		elif self.natural_occurence == "synthetic":
			self.image.putpixel((6, 2),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((7, 2),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((8, 2),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((9, 2),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((7, 4),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((8, 4),STOPPER_LIGHT_BLUE_SYNTHETIC)
		else:
			self.image.putpixel((6, 2),STOPPER_LIGHT_BLUE)
			self.image.putpixel((7, 2),STOPPER_LIGHT_BLUE)
			self.image.putpixel((8, 2),STOPPER_LIGHT_BLUE)
			self.image.putpixel((9, 2),STOPPER_LIGHT_BLUE)
			self.image.putpixel((7, 4),STOPPER_LIGHT_BLUE)
			self.image.putpixel((8, 4),STOPPER_LIGHT_BLUE)
		self.image.putpixel((7, 3),STOPPER_DARK_BLUE)
		self.image.putpixel((8, 3),STOPPER_DARK_BLUE)
	def colorInside(self):
		self.image.putpixel((6, 9),self.color)
		self.image.putpixel((6, 10),self.color)
		self.image.putpixel((6, 11),self.color)
		self.image.putpixel((6, 12),self.color)
		self.image.putpixel((6, 13),self.color)
		self.image.putpixel((7, 9),self.color)
		self.image.putpixel((7, 10),self.color)
		self.image.putpixel((7, 11),self.color)
		self.image.putpixel((7, 12),self.color)
		self.image.putpixel((7, 13),self.color)
		self.image.putpixel((8, 9),self.color)
		self.image.putpixel((8, 10),self.color)
		self.image.putpixel((8, 11),self.color)
		self.image.putpixel((8, 12),self.color)
		self.image.putpixel((8, 13),self.color)
		self.image.putpixel((9, 9),self.color)
		self.image.putpixel((9, 10),self.color)
		self.image.putpixel((9, 11),self.color)
		self.image.putpixel((9, 12),self.color)
		self.image.putpixel((9, 13),self.color)
		self.image.putpixel((6, 8),self.color)
		self.image.putpixel((8, 8),self.color)
		self.image.putpixel((7, 14),self.color)
		self.image.putpixel((8, 14),self.color)
class solid_Image(BlankImage):
	def __init__(self, color: str, natural_occurence: str):
		super().__init__(color, natural_occurence)
	def drawBaseForm(self):
		self.image.putpixel((5, 2),BLACK)
		self.image.putpixel((5, 3),BLACK)
		self.image.putpixel((5, 4),BLACK)
		self.image.putpixel((5, 5),BLACK)
		self.image.putpixel((5, 6),BLACK)
		self.image.putpixel((5, 7),BLACK)
		self.image.putpixel((5, 8),BLACK)
		self.image.putpixel((5, 9),BLACK)
		self.image.putpixel((5, 10),BLACK)
		self.image.putpixel((5, 11),BLACK)
		self.image.putpixel((5, 12),BLACK)
		self.image.putpixel((5, 13),BLACK)
		self.image.putpixel((10, 2),BLACK)
		self.image.putpixel((10, 3),BLACK)
		self.image.putpixel((10, 4),BLACK)
		self.image.putpixel((10, 5),BLACK)
		self.image.putpixel((10, 6),BLACK)
		self.image.putpixel((10, 7),BLACK)
		self.image.putpixel((10, 8),BLACK)
		self.image.putpixel((10, 9),BLACK)
		self.image.putpixel((10, 10),BLACK)
		self.image.putpixel((10, 11),BLACK)
		self.image.putpixel((10, 12),BLACK)
		self.image.putpixel((10, 13),BLACK)
		self.image.putpixel((6, 14),BLACK)
		self.image.putpixel((9, 14),BLACK)
		self.image.putpixel((7, 15),BLACK)
		self.image.putpixel((8, 15),BLACK)
		if self.natural_occurence == "decay":
			self.image.putpixel((6, 1),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((7, 1),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((8, 1),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((9, 1),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((6, 3),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((7, 3),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((8, 3),STOPPER_LIGHT_BLUE_DECAY)
			self.image.putpixel((9, 3),STOPPER_LIGHT_BLUE_DECAY)
		elif self.natural_occurence == "synthetic":
			self.image.putpixel((6, 1),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((7, 1),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((8, 1),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((9, 1),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((6, 3),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((7, 3),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((8, 3),STOPPER_LIGHT_BLUE_SYNTHETIC)
			self.image.putpixel((9, 3),STOPPER_LIGHT_BLUE_SYNTHETIC)
		else:
			self.image.putpixel((6, 1),STOPPER_LIGHT_BLUE)
			self.image.putpixel((7, 1),STOPPER_LIGHT_BLUE)
			self.image.putpixel((8, 1),STOPPER_LIGHT_BLUE)
			self.image.putpixel((9, 1),STOPPER_LIGHT_BLUE)
			self.image.putpixel((6, 3),STOPPER_LIGHT_BLUE)
			self.image.putpixel((7, 3),STOPPER_LIGHT_BLUE)
			self.image.putpixel((8, 3),STOPPER_LIGHT_BLUE)
			self.image.putpixel((9, 3),STOPPER_LIGHT_BLUE)
		self.image.putpixel((6, 2),STOPPER_DARK_BLUE)
		self.image.putpixel((7, 2),STOPPER_DARK_BLUE)
		self.image.putpixel((8, 2),STOPPER_DARK_BLUE)
		self.image.putpixel((9, 2),STOPPER_DARK_BLUE)
	def colorInside(self):
		self.image.putpixel((6, 6),self.color)
		self.image.putpixel((6, 7),self.color)
		self.image.putpixel((6, 8),self.color)
		self.image.putpixel((6, 9),self.color)
		self.image.putpixel((6, 10),self.color)
		self.image.putpixel((6, 11),self.color)
		self.image.putpixel((6, 12),self.color)
		self.image.putpixel((6, 13),self.color)
		self.image.putpixel((7, 6),self.color)
		self.image.putpixel((7, 7),self.color)
		self.image.putpixel((7, 8),self.color)
		self.image.putpixel((7, 9),self.color)
		self.image.putpixel((7, 10),self.color)
		self.image.putpixel((7, 11),self.color)
		self.image.putpixel((7, 12),self.color)
		self.image.putpixel((7, 13),self.color)
		self.image.putpixel((8, 6),self.color)
		self.image.putpixel((8, 7),self.color)
		self.image.putpixel((8, 8),self.color)
		self.image.putpixel((8, 9),self.color)
		self.image.putpixel((8, 10),self.color)
		self.image.putpixel((8, 11),self.color)
		self.image.putpixel((8, 12),self.color)
		self.image.putpixel((8, 13),self.color)
		self.image.putpixel((9, 6),self.color)
		self.image.putpixel((9, 7),self.color)
		self.image.putpixel((9, 8),self.color)
		self.image.putpixel((9, 9),self.color)
		self.image.putpixel((9, 10),self.color)
		self.image.putpixel((9, 11),self.color)
		self.image.putpixel((9, 12),self.color)
		self.image.putpixel((9, 13),self.color)
		self.image.putpixel((7, 14),self.color)
		self.image.putpixel((8, 14),self.color)
