"""
Tools
"""
from backtools import IMGRun, REGRun, buildupTranslations, runZip
from backtools.core import elements
from os import system, name

def work():
	"""
	Working method
	(main)
	"""
	img = IMGRun()
	reg = REGRun()
	while True:
		try:
			cmd = input("tools :\t").split(" ")
			match cmd[0]:
				case "quit" | "exit" | "stop":
					break
				case "image" | "img":
					img.run(cmd[1:])
				case "register" | "reg":
					reg.run(cmd[1:])
				case "export":
					elements.exportList(cmd[1])
				case "print":
					try:
						tmp = int(cmd[1])
						for i in elements.elements:
							if tmp == i.z.Z_int:
								print(i)
					except:
						for i in elements.elements:
							if cmd[1] == i.name.lower():
								print(i)
				case "cls" | "clear":
					if name == 'nt':
						system("cls")
					else:
						system("clear")
				case "zip":
					runZip()
				case "translation":
					buildupTranslations()
				case _:
					pass
		except:
			pass
	return

if __name__ == '__main__':
	work()
