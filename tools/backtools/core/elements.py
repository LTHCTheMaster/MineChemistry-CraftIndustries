from .images import *
from datargsing import dGDM as GDM
import os

class Coords:
	def __init__(self, struct: dict):
		self.x = struct["x"]
		self.y = struct["y"]
	
	@property
	def pos(self) -> tuple[int, int]:
		return (self.x, self.y)

	def __str__(self) -> str:
		return f"x: {self.x}, y: {self.y}"

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
		self.natural_occurence: str = struct["natural_occurence"]
		self.file_name: str = self.z.Z_str + "_" + self.name.lower()
		self.image: BlankImage = eval(f"{self.state}_Image('{self.color}','{self.natural_occurence}')")
		self.ingot_image: IngotTextureImage | None = None
		if self.state == "solid" and self.name not in ("Iron", "Copper", "Gold"):
			self.ingot_image = IngotTextureImage(self.color)
	
	def __str__(self) -> str:
		return f"{self.name.upper()}:\n\tAtomic Number:\n{self.z}\n\tState: {self.state.capitalize()}\n\tNatural Occurence: {self.natural_occurence.capitalize()}"

	def getDrawStruct(self) -> tuple[Image.Image, Image.Image | None, Coords]:
		return (self.image.getImage(), self.ingot_image.getImage() if isinstance(self.ingot_image, IngotTextureImage) else None, self.coords)
	def save(self, path: str):
		self.image.save(path+"/"+self.file_name)
		if isinstance(self.ingot_image, IngotTextureImage):
			self.image.save(path+"ingot/"+self.file_name)

ELEMENT_PATH: str = "tools/data/elements.struct"

class Tool:
	def __init__(self):
		self.elements: list[Element] = []
		self.loadElements()

	def loadElements(self):
		struct_full: dict = GDM().get_from_json(ELEMENT_PATH, True)
		for i in  struct_full:
			self.elements.append(Element(i, struct_full[i]))
	
	def reloadElements(self):
		self.elements: list[Element] = []
		self.loadElements()

	def printElements(self):
		for i in self.elements:
			print(i)

	def saveElements(self, path: str):
		if not os.path.exists(path):
			os.makedirs(path)
		if not os.path.exists(path+"ingot"):
			os.makedirs(path+"ingot")
		for i in self.elements:
			i.save(path)
	
	def exportList(self, path: str):
		if not os.path.exists(path):
			os.makedirs(path)
		tmp = open(path+"/names.txt", "w")
		for i in self.elements:
			tmp.write(f"{i.name.lower()}\n")
		tmp.close()

elements: Tool = Tool()
