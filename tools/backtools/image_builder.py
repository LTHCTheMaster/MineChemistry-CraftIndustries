"""
Image commands ?
"""
from .core import PeriodicTableBuilder, elements, TemplateImageExporter, DustBlockTextureImage, IronBlockTextureImage, CopperBlockTextureImage, GoldenBlockTextureImage
from datargsing import dGDM as GDM
from PIL import Image

FIXED_PATH: tuple[str] = ("Resourcepack/assets/lthc.chemistry/models/elements/", "Resourcepack/assets/lthc.chemistry/textures/block/elements/", "Resourcepack/assets/minecraft/models/item/repeating_command_block.json")
FIXED_PATH2: tuple[str] = ("Resourcepack/assets/lthc.chemistry/models/block/", "Resourcepack/assets/minecraft/models/item/cobblestone.json", "Resourcepack/assets/minecraft/models/item/barrel.json")

class Run:
	"""
	Command parser and runner for all images related things
	"""
	def __init__(self):
		"""
		Command parser and runner for all images related things
		"""
		self.period = PeriodicTableBuilder(elements)
		self.gdm = GDM()
		self.templates = TemplateImageExporter()

	def run(self, cmd: list[str]):
		"""
		Parse and Run commands
		"""
		match cmd[0]:
			case "build":
				match cmd[1]:
					case "elements":
						elements.saveElements(cmd[2])
						print("\033[32mDone\033[0m")
					case "periodic":
						self.period.save(cmd[2])
						print("\033[32mDone\033[0m")
					case "templates":
						self.templates.export(cmd[2])
						print("\033[32mDone\033[0m")
					case _:
						pass
			case "show":
				match cmd[1]:
					case "periodic":
						try:
							self.period.show(cmd[2:])
						except:
							self.period.show(["base_table"])
					case "element":
						try:
							tmp = int(cmd[2])
							for i in elements.elements:
								if tmp == i.z.Z_int:
									i.image.show()
									return
						except:
							for i in elements.elements:
								if cmd[2] == i.name.lower():
									i.image.show()
									return
						return
					case _:
						pass
			case "reload":
				self.reload()
			case "rp":
				pred = []
				pred2 = []
				pred3 = []
				pred4 = []
				to_add = 0
				to_add2 = 0
				elements.saveElements(FIXED_PATH[1])
				print("\033[35mTextures:\033[0m \033[32mDone\033[0m")
				for j, i in enumerate(elements.elements):
					self.gdm.set_to_json(FIXED_PATH[0] + i.file_name + '.json', {"parent": "item/generated","textures": {"layer0": f"lthc.chemistry:block/elements/{i.file_name}"}}, False)
					pred.append({"predicate": {"custom_model_data": 170000 + j},"model": "lthc.chemistry:elements/" + i.file_name})
					if i.state == "solid" and not i.exclude:
						if i.shape in ("ingot", "dust"):
							self.gdm.set_to_json(FIXED_PATH[0] + i.shape + '/' + i.file_name + '.json', {"parent": "item/generated","textures": {"layer0": f"lthc.chemistry:block/elements/{i.shape}/{i.file_name}"}}, False)
							pred2.append({"predicate": {"custom_model_data": 170118 + to_add},"model": "lthc.chemistry:elements/" + i.shape + "/" + i.file_name})
							if isinstance(i.block_image, (DustBlockTextureImage, IronBlockTextureImage, CopperBlockTextureImage, GoldenBlockTextureImage)):
								pred3.append({"predicate": {"custom_model_data": 172000 + to_add2},"model": "lthc.chemistry:block/" + i.file_name})
								pred4.append({"predicate": {"custom_model_data": 172000 + to_add2},"model": "lthc.chemistry:block/barrel/" + i.file_name})
								self.gdm.set_to_json(FIXED_PATH2[0] + i.file_name + '.json', {"parent": "lthc.chemistry:block_renderer", "textures": {"all": f"lthc.chemistry:block/elements/{i.shape}_block/{i.file_name}"}})
								self.gdm.set_to_json(FIXED_PATH2[0] + 'barrel/' + i.file_name + '.json', {"parent": "minecraft:block/cube_all", "textures": {"all": f"lthc.chemistry:block/elements/{i.shape}_block/{i.file_name}"}})
						else:
							self.gdm.set_to_json(FIXED_PATH[0] + 'imported/' + i.file_name + '.json', {"parent": "item/generated","textures": {"layer0": f"lthc.chemistry:block/elements/imported/{i.file_name}"}}, False)
							pred2.append({"predicate": {"custom_model_data": 170118 + to_add},"model": "lthc.chemistry:elements/imported/" + i.file_name})
							if isinstance(i.block_image, Image.Image):
								pred3.append({"predicate": {"custom_model_data": 172000 + to_add2},"model": "lthc.chemistry:block/" + i.file_name})
								pred4.append({"predicate": {"custom_model_data": 172000 + to_add2},"model": "lthc.chemistry:block/barrel/" + i.file_name})
								self.gdm.set_to_json(FIXED_PATH2[0] + i.file_name + '.json', {"parent": "lthc.chemistry:block_renderer", "textures": {"all": f"lthc.chemistry:block/elements/imported_block/{i.file_name}"}})
								self.gdm.set_to_json(FIXED_PATH2[0] + 'barrel/' + i.file_name + '.json', {"parent": "minecraft:block/cube_all", "textures": {"all": f"lthc.chemistry:block/elements/imported_block/{i.file_name}"}})
						to_add += 1
						to_add2 += 1
				pred.extend(pred2)
				self.gdm.set_to_json(FIXED_PATH[2], {"parent": "minecraft:block/repeating_command_block","overrides": [i for i in pred]}, False)
				self.gdm.set_to_json(FIXED_PATH2[1], {"parent": "block/cobblestone","overrides": [i for i in pred3]}, False)
				self.gdm.set_to_json(FIXED_PATH2[2], {"parent": "block/barrel","overrides": [i for i in pred4]}, False)
				print("\033[35mModels:\033[0m \033[32mDone\033[0m")
			case _:
				pass
	
	def reload(self):
		"""
		Call elements reloading
		"""
		elements.reloadElements()
		self.period = PeriodicTableBuilder(elements)
