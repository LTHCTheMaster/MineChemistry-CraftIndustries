"""
Tools
"""
from backtools import IMGRun, REGRun, buildupTranslations, runZip, printHelpMessage
from backtools.core import elements
from os import system, name
from sys import argv

class ToolsRunner:
	"""
	Tools
	"""
	def __init__(self):
		"""
		Tools
		"""
		self.img = IMGRun()
		self.reg = REGRun()
	
	def runCMD(self, cmd: list[str]) -> bool:
		"""
		Working method
		(main/run command)
		"""
		try:
			match cmd[0]:
				case "quit" | "exit" | "stop":
					return True
				case "image" | "img":
					self.img.run(cmd[1:])
				case "registry" | "register" | "reg":
					self.reg.run(cmd[1:])
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
					system("cls") if name == 'nt' else system("clear")
				case "zip":
					runZip()
				case "translation" | "translate":
					buildupTranslations()
				case "help":
					printHelpMessage()
				case _:
					pass
		except:
			print("\033[31mAn error occured\033[0m")
		return False
	
	def shellLoop(self) -> None:
		"""
		Working method
		(main/shell loop)
		"""
		while True:
			cmd = input("\033[36mtools :\033[0m\t").split(" ")
			if self.runCMD(cmd): break
		return
	
	def argExec(self, cmdlist: list[str]) -> None:
		"""
		Working method
		(main/from args)
		"""
		for cmd in cmdlist:
			self.runCMD(cmd.split(" "))

def work():
	"""
	Working method
	(main)
	"""
	_tools = ToolsRunner()
	_tools.argExec(argv[1:]) if len(argv) > 1 else _tools.shellLoop()

if __name__ == '__main__':
	work()
