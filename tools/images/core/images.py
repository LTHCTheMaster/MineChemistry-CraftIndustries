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
STOPPER_LIGHT_BLUE = (23,84,135,255)
NATOCC_DECAY = (45, 236, 67, 255)
NATOCC_SYNTHETIC = (215, 159, 199, 255)
STOPPER_LIGHT_BLUE = (23,84,135,255)
STOPPER_LIGHT_BLUE_DECAY = colorMixer(STOPPER_LIGHT_BLUE, NATOCC_DECAY)
STOPPER_LIGHT_BLUE_SYNTHETIC = colorMixer(STOPPER_LIGHT_BLUE, NATOCC_SYNTHETIC)
STOPPER_DARK_BLUE = (10,38,62,255)
BLANK_IMAGE = (255, 255, 255, 0)
SIZE = (16, 16)

class BlankImage:
    def __init__(self, color: str, natural_occurence: str):
        self.image = Image.new("RGBA", SIZE, BLANK_IMAGE)
        self.color = makeColorTuple(color)
        self.natural_occurence = natural_occurence
    
    def drawBaseForm(self):
        pass
    def colorInside(self):
        pass
    def draw(self):
        self.drawBaseForm()
        self.colorInside()
    def show(self):
        tmp = self.image.resize((512,512),Image.Resampling.NEAREST)
        tmp.show()
    def getImage(self) -> Image.Image:
        return self.image

class solid_Image(BlankImage):
    def __init__(self, color: str, natural_occurence: str):
        super().__init__(color, natural_occurence)
        self.draw()
    
    def drawBaseForm(self):
        for i in range(12):
            self.image.putpixel((5,2+i),BLACK)
            self.image.putpixel((10,2+i),BLACK)
        for i in range(4):
            self.image.putpixel((6+i,1), STOPPER_LIGHT_BLUE_DECAY) if self.natural_occurence == "decay" else self.image.putpixel((6+i,1), STOPPER_LIGHT_BLUE_SYNTHETIC) if self.natural_occurence == "synthetic" else self.image.putpixel((6+i,1),STOPPER_LIGHT_BLUE)
            self.image.putpixel((6+i,2),STOPPER_DARK_BLUE)
            self.image.putpixel((6+i,3), STOPPER_LIGHT_BLUE_DECAY) if self.natural_occurence == "decay" else self.image.putpixel((6+i,3), STOPPER_LIGHT_BLUE_SYNTHETIC) if self.natural_occurence == "synthetic" else self.image.putpixel((6+i,3),STOPPER_LIGHT_BLUE)
        self.image.putpixel((6,14),BLACK)
        self.image.putpixel((9,14),BLACK)
        self.image.putpixel((7,15),BLACK)
        self.image.putpixel((8,15),BLACK)
    
    def colorInside(self):
        for i in range(4):
            for j in range(8):
                self.image.putpixel((6+i,6+j),self.color)
        self.image.putpixel((7,14),self.color)
        self.image.putpixel((8,14),self.color)

class liquid_Image(BlankImage):
    def __init__(self, color: str, natural_occurence: str):
        super().__init__(color, natural_occurence)
        self.draw()
    
    def drawBaseForm(self):
        for i in range(11):
            self.image.putpixel((5,4+i),BLACK)
            self.image.putpixel((10,4+i),BLACK)
        for i in range(4):
            self.image.putpixel((6+i,2), STOPPER_LIGHT_BLUE_DECAY) if self.natural_occurence == "decay" else self.image.putpixel((6+i,2), STOPPER_LIGHT_BLUE_SYNTHETIC) if self.natural_occurence == "synthetic" else self.image.putpixel((6+i,2),STOPPER_LIGHT_BLUE)
            self.image.putpixel((6+i,15),BLACK)
        for i in range(2):
            self.image.putpixel((7+i,3),STOPPER_DARK_BLUE)
            self.image.putpixel((7+i,4), STOPPER_LIGHT_BLUE_DECAY) if self.natural_occurence == "decay" else self.image.putpixel((7+i,4), STOPPER_LIGHT_BLUE_SYNTHETIC) if self.natural_occurence == "synthetic" else self.image.putpixel((7+i,4),STOPPER_LIGHT_BLUE)
            self.image.putpixel((6,3+i),BLACK)
            self.image.putpixel((9,3+i),BLACK)
        self.image.putpixel((6,14),BLACK)
        self.image.putpixel((9,14),BLACK)
    
    def colorInside(self):
        for i in range(4):
            for j in range(5):
                self.image.putpixel((6+i,9+j),self.color)
        self.image.putpixel((6,8),self.color)
        self.image.putpixel((8,8),self.color)
        self.image.putpixel((7,14),self.color)
        self.image.putpixel((8,14),self.color)

class gas_Image(BlankImage):
    def __init__(self, color: str, natural_occurence: str):
        super().__init__(color, natural_occurence)
        self.draw()
    
    def drawBaseForm(self):
        for i in range(5):
            self.image.putpixel((4,5+i),BLACK)
            self.image.putpixel((11,5+i),BLACK)
        for i in range(3):
            self.image.putpixel((5,3+i),BLACK)
            self.image.putpixel((5,9+i),BLACK)
            self.image.putpixel((10,3+i),BLACK)
            self.image.putpixel((10,9+i),BLACK)
        for i in range(4):
            self.image.putpixel((6+i,1),BLACK)
            self.image.putpixel((6+i,13), STOPPER_LIGHT_BLUE_DECAY) if self.natural_occurence == "decay" else self.image.putpixel((6+i,13), STOPPER_LIGHT_BLUE_SYNTHETIC) if self.natural_occurence == "synthetic" else self.image.putpixel((6+i,13),STOPPER_LIGHT_BLUE)
        for i in range(2):
            self.image.putpixel((7+i,11), STOPPER_LIGHT_BLUE_DECAY) if self.natural_occurence == "decay" else self.image.putpixel((7+i,11), STOPPER_LIGHT_BLUE_SYNTHETIC) if self.natural_occurence == "synthetic" else self.image.putpixel((7+i,11),STOPPER_LIGHT_BLUE)
            self.image.putpixel((7+i,12),STOPPER_DARK_BLUE)
            self.image.putpixel((6,2+i),BLACK)
            self.image.putpixel((9,2+i),BLACK)
            self.image.putpixel((6,11+i),BLACK)
            self.image.putpixel((9,11+i),BLACK)
    
    def colorInside(self):
        for i in range(6):
            for j in range(2):
                self.image.putpixel((5+i,6+j),self.color)
        for i in range(4):
            for j in range(2):
                self.image.putpixel((6+i,4+j),self.color)
        for i in range(2):
            for j in range(2):
                self.image.putpixel((7+i,2+j),self.color)
