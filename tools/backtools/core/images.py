from os import listdir

POS_FILE_PATH = "tools/data/elements"
AFCIMGPATH = "tools/backtools/core/autofilecontainer/"

def filecutter(content: str) -> list[str]:
	lcontent = content.split('\t-\n')
	lcontent[0] = lcontent[0].replace('BLACK:','').replace('\t','')
	lcontent[1] = lcontent[1].replace('STOPPER_LIGHT_BLUE:','').replace('\t','')
	lcontent[2] = lcontent[2].replace('STOPPER_DARK_BLUE:','').replace('\t','')
	return lcontent.copy()

def define_drawBaseForm(desc: list[str]) -> str:
	return '\tdef drawBaseForm(self):\n\t\t' + '\n\t\t'.join([f"self.image.putpixel({i},BLACK)" for i in desc[0].split('\n')[1:-1]]) + '\n\t\tif self.natural_occurence == "decay":\n\t\t\t' + '\n\t\t\t'.join([f"self.image.putpixel({i},STOPPER_LIGHT_BLUE_DECAY)" for i in desc[1].split('\n')[1:-1]]) + '\n\t\telif self.natural_occurence == "synthetic":\n\t\t\t' + '\n\t\t\t'.join([f"self.image.putpixel({i},STOPPER_LIGHT_BLUE_SYNTHETIC)" for i in desc[1].split('\n')[1:-1]]) + '\n\t\telse:\n\t\t\t' + '\n\t\t\t'.join([f"self.image.putpixel({i},STOPPER_LIGHT_BLUE)" for i in desc[1].split('\n')[1:-1]]) + '\n\t\t' + '\n\t\t'.join([f"self.image.putpixel({i},STOPPER_DARK_BLUE)" for i in desc[2].split('\n')[1:]])

def define_colorInside(desc: list[str]) -> str:
	return '\tdef colorInside(self):\n\t\t' + '\n\t\t'.join([f"self.image.putpixel({i},self.color)" for i in desc])

def define_imageClass(prefix: str, descDrawBaseForm: list[str], descColorInside: list[str]) -> str:
	return f"class {prefix}_Image(BlankImage):\n\tdef __init__(self, color: str, natural_occurence: str):\n\t\tsuper().__init__(color, natural_occurence)\n"+define_drawBaseForm(descDrawBaseForm)+'\n'+define_colorInside(descColorInside)

tmp = ""
for i in listdir(POS_FILE_PATH):
	local_path = POS_FILE_PATH+'/'+i+'/'+i+'_'
	name = i
	empty_pos_file = open(local_path+'empty.pos','r')
	empty_desc = filecutter(empty_pos_file.read())
	empty_pos_file.close()
	color_pos_file = open(local_path+'color.pos','r')
	color_desc = color_pos_file.read().split('\n')
	color_pos_file.close()
	tmp += define_imageClass(i, empty_desc.copy(), color_desc.copy())+'\n'
file = open(AFCIMGPATH + "images.py",'w')
tmpfile = open(AFCIMGPATH + "base.txt", 'r')
file.write(tmpfile.read() + tmp)
tmpfile.close()
file.close()

from .autofilecontainer.images import *
