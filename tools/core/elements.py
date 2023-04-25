from datargsing import dGlobal_datafiles_manager as GDM
from .images import Coords, BlankImage, solid_Image, liquid_Image, gas_Image, Image

class Z:
    def __init__(self, z: str):
        self.Z_str = z
        self.Z_int = int(z)
    
    def __str__(self) -> str:
        return f"\t\tfixed size format: {self.Z_str}\n\t\tnumber format: {self.Z_int}"

class Element:
    def __init__(self, name: str, struct: dict):
        self.name: str = name
        self.z: Z = Z(struct["Z"])
        self.state: str = struct["state"]
        self.color: str = struct["color"]
        self.coords: Coords = Coords(struct["periodic_draw"])
        self.file_name: str = self.z.Z_str + "_" + self.name.lower()
        self.image: BlankImage = eval(f"{self.state}_Image('{self.color}')")
    
    def __str__(self) -> str:
        return f"{self.name.upper()}:\n\tAtomic Number:\n{self.z}\n\tState: {self.state}"

    def getDrawStruct(self) -> tuple[Image.Image, Coords]:
        return (self.image.getImage(), self.coords)
    def save(self, path: str):
        self.image.getImage().save(fp=path+"/"+self.file_name+'.png',format="png")

ELEMENT_PATH: str = "tools/data/struct.json"
elements: list[Element] = []

def loadElements():
    struct_full: dict = GDM().get_from_json(ELEMENT_PATH, True)
    for i in  struct_full:
        elements.append(Element(i, struct_full[i]))

def printElements():
    for i in elements:
        print(i)

def saveElements(path: str):
    for i in elements:
        i.save(path)
