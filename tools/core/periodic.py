from .elements import elements, Image

BLANK_PERIOD = (181, 159, 119, 255)

class PeriodicTableBuilder:
    def __init__(self):
        self.image = Image.new("RGBA", (288, 148), BLANK_PERIOD)
        self.draw()
    
    def draw(self):
        for i in  elements:
            img, coords = i.getDrawStruct()
            self.image.paste(img, coords.pos(), img)
    
    def show(self):
        tmp = self.image.resize((1152,592), Image.Resampling.NEAREST)
        tmp.show()
    
    def save(self, path: str):
        self.image.save(fp=path+"/000_TableauPNG.png",format="png")
