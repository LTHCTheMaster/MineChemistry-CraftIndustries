from .core import PeriodicTableBuilder, elements

class Run:
	def __init__(self):
		self.period = PeriodicTableBuilder(elements)

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
	
	def reload(self):
		elements.reloadElements()
		self.period = PeriodicTableBuilder(elements)
