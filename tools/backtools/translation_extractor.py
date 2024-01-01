"""
Translations ?
"""
from datargsing import dGDM as GDM

FIXED_PATH: str = "Resourcepack/assets/lthc.chemistry/lang/"
TRANSLATION_SOURCE: str = "tools/data/translate.trslt"

def buildupTranslations() -> None:
	"""
	Generate translations files
	"""
	langs: list[str] = []
	contents: list[dict] = []
	sub_contents: list[str] = []
	sources: list[str] = open(TRANSLATION_SOURCE, 'r', encoding="utf-8").read().replace('\n','').replace('\t', '').split('#')[1:]
	for source in sources:
		sub_contents: list[str] = source.split(' {', 1)
		langs.append(sub_contents[0])
		contents.append(eval('{' + sub_contents[1]).copy())

	core: dict = dict()
	gdm = GDM()
	for i in range(len(langs)):
		core = dict()
		for j in contents[i]:
			for k in contents[i][j]:
				if type(contents[i][j][k]) is str:
					core["lthcthemaster.lthc.chemistry." + j + '.' + k] = contents[i][j][k]
				else:
					for l in contents[i][j][k]:
						core["lthcthemaster.lthc.chemistry." + j + '.' + k + '.' + l] = contents[i][j][k][l]
		gdm.set_to_json(FIXED_PATH + langs[i] + '.json', core, False)
