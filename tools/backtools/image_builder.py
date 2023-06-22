from .core import PeriodicTableBuilder, elements
from datargsing import dGDM as GDM

FIXED_PATH_RP = ["Resourcepack/assets/lthc.chemistry/models/elements/", "Resourcepack/assets/lthc.chemistry/textures/block/elements/"]

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
				elements.saveElements(FIXED_PATH_RP[1])
				for i in elements.elements:
					self.gdm.set_to_json(FIXED_PATH_RP[0] + i.file_name + '.json', {"parent": "item/generated","textures": {"layer0": f"lthc.chemistry:block/elements/{i.file_name}"}}, True)
			case _:
				pass
	
	def reload(self):
		elements.reloadElements()
		self.period = PeriodicTableBuilder(elements)
