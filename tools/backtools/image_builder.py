from .core import PeriodicTableBuilder, elements
from datargsing import dGDM as GDM

FIXED_PATH: tuple[str] = ["Resourcepack/assets/lthc.chemistry/models/elements/", "Resourcepack/assets/lthc.chemistry/textures/block/elements/", "Resourcepack/assets/minecraft/models/item/repeating_command_block.json"]

class Run:
	def __init__(self):
		self.period = PeriodicTableBuilder(elements)
		self.gdm = GDM()

	def run(self, cmd: list[str]):
		match cmd[0]:
			case "build":
				match cmd[1]:
					case "elements":
						elements.saveElements(cmd[2])
					case "periodic":
						self.period.save(cmd[2])
					case _:
						pass
			case "show":
				match cmd[1]:
					case "periodic":
						self.period.show()
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
				elements.saveElements(FIXED_PATH[1])
				for j, i in enumerate(elements.elements):
					self.gdm.set_to_json(FIXED_PATH[0] + i.file_name + '.json', {"parent": "item/generated","textures": {"layer0": f"lthc.chemistry:block/elements/{i.file_name}"}}, False)
					pred.append({"predicate": {"custom_model_data": 170000 + j},"model": "lthc.chemistry:elements/" + i.file_name})
				self.gdm.set_to_json(FIXED_PATH[2], {"parent": "minecraft:block/repeating_command_block","overrides": [i for i in pred]}, False)
			case _:
				pass
	
	def reload(self):
		elements.reloadElements()
		self.period = PeriodicTableBuilder(elements)
