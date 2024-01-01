"""
Elements toolbox
"""
from .images import *
from datargsing import dGDM as GDM
import os

# Simple (x, y) system
class Coords:
	"""
	Simple (x, y) system
	"""
	def __init__(self, struct: dict):
		"""
		Simple (x, y) system
		"""
		self.x = struct["x"]
		self.y = struct["y"]
	
	@property
	def pos(self) -> tuple[int, int]:
		"""
		Get x and y in a tuple form*
		it's a property so you don't need to use paranthesis when you call this method because it's a property ☺
		"""
		return (self.x, self.y)

	def __str__(self) -> str:
		"""
		Useful for display
		"""
		return f"x: {self.x}, y: {self.y}"

# Number of protons
class Z:
	"""
	A class that represent the Z number of an atom/element
	"""
	def __init__(self, z: str):
		"""
		A class that represent the Z number of an atom/element
		"""
		self.Z_str = z
		self.Z_int = int(z)
	
	def __str__(self) -> str:
		"""
		Useful for display
		"""
		return f"\t\tfixed size format: {self.Z_str}\n\t\tnumber format: {self.Z_int}"

# It's an element. Yes!
class Element:
	"""
	A class that represent an element and implements a lot of functions/methods related to drawings (textures), displaying textures and informations, manage saving and putting on a larger specific image
	"""
	def __init__(self, name: str, struct: dict):
		"""
		A class that represent an element and implements a lot of functions/methods related to drawings (textures), displaying textures and informations, manage saving and putting on a larger specific image
		"""
		self.name: str = name
		self.z: Z = Z(struct["Z"])
		self.state: str = struct["state"]
		self.color: str = struct["color"]
		self.coords: Coords = Coords(struct["periodic_draw"])
		self.natural_occurence: str = struct["natural_occurence"]
		self.file_name: str = self.z.Z_str + "_" + self.name.lower()
		self.image: BlankImage = eval(f"{self.state}_Image('{self.color}','{self.natural_occurence}')")
		self.ingot_image: GoldenIngotTextureImage | CopperIngotTextureImage | IronIngotTextureImage | DustTextureImage | Image.Image | None = None
		if self.state == "solid":
			if "shape" in struct:
				self.shape: str = struct["shape"]
			else:
				self.shape: str = "ingot"
			match self.shape:
				case "ingot":
					if "ingot_type" in struct:
						ingot_type: str = struct["ingot_type"]
						match ingot_type:
							case "gold":
								self.ingot_image = GoldenIngotTextureImage(self.color)
							case "iron":
								self.ingot_image = IronIngotTextureImage(self.color)
							case "copper":
								self.ingot_image = CopperIngotTextureImage(self.color)
							case _:
								self.ingot_image = GoldenIngotTextureImage(self.color)
					else:
						self.ingot_image = GoldenIngotTextureImage(self.color)
				case "dust":
					try:
						if "color_override" in struct:
							self.ingot_image = DustTextureImage(struct["color_override"])
						else: self.ingot_image = DustTextureImage(self.color)
					except:
						self.ingot_image = DustTextureImage(self.color)
				case "external":
					if "path" in struct:
						tmp_base_path: str = "tools/data/" + "/".join(struct["path"].split(":")) + "_"
						try:
							self.ingot_image = Image.open(tmp_base_path + "ingot.png")
							self.ingot_image.convert(mode="RGBA")
							self.ingot_image.load()
						except:
							self.fallback()
					else:
						self.fallback()
				case _:
					self.fallback()
		if "exclude_not_elements_from_export" in struct:
			self.exclude: bool = struct["exclude_not_elements_from_export"]
		else:
			self.exclude: bool = False
	
	def fallback(self):
		"""
		A fallback for "ingot texture" (solid shape texture)
		"""
		self.shape: str = "ingot"
		self.ingot_image = GoldenIngotTextureImage(self.color)

	def __str__(self) -> str:
		"""
		Useful for display
		"""
		return f"{self.name.upper()}:\n\tAtomic Number:\n{self.z}\n\tState: {self.state.capitalize()}\n\tNatural Occurence: {self.natural_occurence.capitalize()}"

	def getDrawStruct(self) -> tuple[Image.Image, Image.Image | None, Coords]:
		"""
		Related to a really specific image
		"""
		if self.state == "solid":
			if isinstance(self.ingot_image, (GoldenIngotTextureImage, IronIngotTextureImage, CopperIngotTextureImage, DustTextureImage)): return (self.image.getImage(), self.ingot_image.getImage(), self.coords)
			else: return (self.image.getImage(), self.ingot_image, self.coords)
		else: return (self.image.getImage(), None, self.coords)

	def save(self, path: str):
		"""
		manage saving
		"""
		self.image.save(path+"/"+self.file_name)
		if self.state == "solid":
			if not self.exclude:
				if isinstance(self.ingot_image, (GoldenIngotTextureImage, IronIngotTextureImage, CopperIngotTextureImage, DustTextureImage)):
					self.ingot_image.save(path+self.shape+"/"+self.file_name)
				else:
					self.ingot_image.save(fp=path+"imported/"+self.file_name+'.png',format="png")

# A constant here ?
ELEMENT_PATH: str = "tools/data/elements.struct"

# The name is transparent
# But i can explain a lttle bit more:
# you can (re)load elements from the data, print the whole list of elements,
# save (export a file) all image somewhere on your computer
# or just export the names of all elements
class Tool:
	"""
	Loading, reloading and some management of a lot of Element objects
	"""
	def __init__(self):
		"""
		Loading, reloading and some management of a lot of Element objects
		"""
		self.elements: list[Element] = []
		self.loadElements()

	def loadElements(self):
		"""
		Load all the elements
		"""
		struct_full: dict = GDM().get_from_json(ELEMENT_PATH, True)
		for i in  struct_full:
			self.elements.append(Element(i, struct_full[i]))
	
	def reloadElements(self):
		"""
		Allow you to reload all of your Elements
		"""
		self.elements: list[Element] = []
		self.loadElements()

	def printElements(self):
		"""
		Some display
		"""
		for i in self.elements:
			print(i)

	def saveElements(self, path: str):
		"""
		Manage saving
		"""
		if not os.path.exists(path):
			os.makedirs(path)
		if not os.path.exists(path+"ingot"):
			os.makedirs(path+"ingot")
		if not os.path.exists(path+"dust"):
			os.makedirs(path+"dust")
		if not os.path.exists(path+"imported"):
			os.makedirs(path+"imported")
		for i in self.elements:
			i.save(path)
	
	def exportList(self, path: str):
		"""
		Export some data
		"""
		if not os.path.exists(path):
			os.makedirs(path)
		tmp = open(path+"/names.txt", "w")
		for i in self.elements:
			tmp.write(f"{i.name.lower()}\n")
		tmp.close()

elements: Tool = Tool()
