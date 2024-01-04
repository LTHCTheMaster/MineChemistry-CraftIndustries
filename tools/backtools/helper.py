"""
Help Message
"""

def formatHelpLine(head: str, desc: str, tabs: int, argslist: str | None = None, state: bool = False) -> str:
	"""
	Format help line
	"""
	if state:
		return '\t'*tabs + f" \033[93m{desc}"
	return f"\033[95m{head} \033[0m\033[92m{argslist}\033[0m:" + '\t'*tabs + f"\033[93m{desc}" if type(argslist) is str else f"\033[95m{head}\033[0m:" + '\t'*tabs + f"\033[93m{desc}"

def formatHelpMultiLine(place: int, cmd: str, lines: tuple[tuple[str | int | tuple[tuple[str | int]]]], state: bool = False) -> str:
	tmp: str = formatHelpLine(cmd, "", 1, None, state) + '\n' if place == 0 else '\t' * (place-1) + formatHelpLine("", "", 1, cmd, state)
	for i in lines:
		tmp += '\t' * (place+1)
		if type(i[1]) is str:
			tmp += formatHelpLine("", i[1], i[2], i[0])
		else:
			has = False
			for j in i[1]:
				tmp += formatHelpMultiLine(place + 1, i[0], j, has)
				has = True
				tmp += "\n"
			tmp = tmp[:-1]
		tmp += '\n'
	return tmp[:-1]


def printHelpMessage():
	"""
	Print the help message
	"""
	print(formatHelpLine("quit, exit, stop", "stop tools", 3))
	print(formatHelpLine("print", "print details about an element", 2, "<number|element name>"))
	print(formatHelpLine("cls, clear", "clear screen", 4))
	print(formatHelpLine("zip", "zip the DP and the RP", 5))
	print(formatHelpLine("translation, translate", "build translations files", 3))
	print(formatHelpLine("help", "show this message", 5))
	print(formatHelpLine("export", "export all elements names in a file", 4, "<path>"))
	print(formatHelpMultiLine(0, "registry, register, reg", (
		("elements", "build basic elements related items registry", 3),
		("solid", "build basic solid state elements related items (dusts, ingots) registry", 4),
		("block", "build block registry", 4)
	)))
	print(formatHelpMultiLine(0, "image, img", (
		("build", (
			(("elements <path>", "save all elements images at a specified location", 2),),
			(("\t periodic <path>", "save all periodic tables images at a specified location", 2),),
			(("\t templates <path>", "save all templates images at a specified location", 2),)
		)),
		("show", (
			(("element <number|element name>", "show the specified elements", 1),),
			(("\t periodic [\033[4mingot\033[0m\033[92m|\033[4mblock\033[0m\033[92m]", "show periodic table", 2),)
		)),
		("reload", " reload data for textures (and also data)", 2),
		("rp", " build the RP", 3)
	)))
