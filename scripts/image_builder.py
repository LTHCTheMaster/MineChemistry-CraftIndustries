from PIL import Image

BLACK = (0,0,0,255)
STOPPER_LIGHT_BLUE = (23,84,135,255)
STOPPER_DARK_BLUE = (10,38,62,255)

def getDec(v: str) -> int:
    if v == "0": return 0
    if v == "1": return 1
    if v == "2": return 2
    if v == "3": return 3
    if v == "4": return 4
    if v == "5": return 5
    if v == "6": return 6
    if v == "7": return 7
    if v == "8": return 8
    if v == "9": return 9
    if v == "a": return 10
    if v == "b": return 11
    if v == "c": return 12
    if v == "d": return 13
    if v == "e": return 14
    if v == "f": return 15

def makeColorTuple(color: str) -> tuple[int, int, int, int]:
    r, g, b = color[:2], color[2:4], color[4:]
    red = getDec(r[0]) * 16 + getDec(r[1])
    green = getDec(g[0]) * 16 + getDec(g[1])
    blue = getDec(b[0]) * 16 + getDec(b[1])
    return (red, green, blue, 255)

class BlankImage:
    def __init__(self, color: str):
        self.image = Image.new("RGBA", (16, 16), (255, 255, 255, 0))
        self.color = makeColorTuple(color)
    
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

class solid_Image(BlankImage):
    def __init__(self, color: str):
        super().__init__(color)
        self.draw()
    
    def drawBaseForm(self):
        for i in range(12):
            self.image.putpixel((5,2+i),BLACK)
            self.image.putpixel((10,2+i),BLACK)
        for i in range(4):
            self.image.putpixel((6+i,1),STOPPER_LIGHT_BLUE)
            self.image.putpixel((6+i,2),STOPPER_DARK_BLUE)
            self.image.putpixel((6+i,3),STOPPER_LIGHT_BLUE)
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
    def __init__(self, color: str):
        super().__init__(color)
        self.draw()
    
    def drawBaseForm(self):
        for i in range(11):
            self.image.putpixel((5,4+i),BLACK)
            self.image.putpixel((10,4+i),BLACK)
        for i in range(4):
            self.image.putpixel((6+i,2),STOPPER_LIGHT_BLUE)
            self.image.putpixel((6+i,15),BLACK)
        for i in range(2):
            self.image.putpixel((7+i,3),STOPPER_DARK_BLUE)
            self.image.putpixel((7+i,4),STOPPER_LIGHT_BLUE)
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
    def __init__(self, color: str):
        super().__init__(color)
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
            self.image.putpixel((6+i,13),STOPPER_LIGHT_BLUE)
        for i in range(2):
            self.image.putpixel((7+i,11),STOPPER_LIGHT_BLUE)
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

test = gas_Image("ffffff")
test.show()
