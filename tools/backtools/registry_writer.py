"""
Data commands ?
"""
from .image_builder import elements, DustBlockTextureImage, CopperBlockTextureImage, IronBlockTextureImage, GoldenBlockTextureImage, Image
from datargsing import dGDM as GDM

FIXED_PATH: tuple[str] = ("Datapack/data/lthc.chemistry/functions/init/_intern/sub_parts/parts/registry/elements.mcfunction","Datapack/data/lthc.chemistry/loot_tables/i/elements/","Datapack/data/lthc.chemistry/functions/init/_intern/sub_parts/parts/registry/elements/solid.mcfunction","Datapack/data/lthc.chemistry/loot_tables/i/elements/solid/","Datapack/data/lthc.chemistry/functions/init/_intern/sub_parts/parts/registry/elements/block.mcfunction","Datapack/data/lthc.chemistry/loot_tables/i/elements/block/")

class Run:
	"""
	Command parser and runner for all data related things
	"""
	def __init__(self):
		"""
		Command parser and runner for all data related things
		"""
		self.gdm = GDM()

	def run(self, cmd: list[str]):
		"""
		Parse and Run commands
		"""
		match cmd[0]:
			case "elements":
				file_content = "## ELEMENTS\n"
				register_assembly: list[str] = []
				for numlowered, element in enumerate(elements.elements):
					calculated = 170000 + numlowered
					tmp = "# " + element.name.capitalize() + '\n'
					tmp += f"data modify storage lthc.chemistry:main REGISTRY.Items.{calculated} "
					tmp += 'set value {Slot:16b,id:"minecraft:repeating_command_block",Count:1b,tag:{ctc:{id:"'
					tmp += element.name.lower()
					tmp += '",from:"lthc.chemistry",traits:{element:1b}}'
					tmp += f",CustomModelData:{calculated},lthc_chemistry:"
					tmp += '{' + f"{element.state}:1b,{element.natural_occurence}:1b"
					tmp += '},display:{Lore:[\'{"translate":"lthcthemaster.lthc.chemistry.lore.tooltip","color":"blue","italic":true}\'],Name:\'[{"translate":"lthcthemaster.lthc.chemistry.items.elements.' + element.name.lower() + '","italic":false,"color":"#ffffff""}]\'}}}'
					register_assembly.append(tmp)
					self.gdm.set_to_json(FIXED_PATH[1] + element.name.lower() + '.json', {"pools": [{"rolls": 1,"bonus_rolls": 0,"entries": [{"type": "minecraft:item","name": "minecraft:repeating_command_block","functions": [{"function": "minecraft:copy_nbt","source": {"type": "minecraft:storage","source": "lthc.chemistry:main"},"ops": [{"source": "REGISTRY.Items."+ str(calculated) +".tag","target": "{}","op": "merge"}]}]}]}]}, False)
					print(f"\033[93m{element.z.Z_str}:\033[0m \033[32mDone\033[0m")
				file_content += '\n'.join(register_assembly)
				file = open(FIXED_PATH[0], "w", encoding='utf-8')
				file.write(file_content)
				file.close()
			case "solid":
				file_content = "## SOLID\n"
				register_assembly: list[str] = []
				toAdd = 0
				for numlowered, element in enumerate(elements.elements):
					if element.state == "solid" and not element.exclude:
						calculated = 170118 + toAdd
						tmp = "# " + element.name.capitalize() + '\n'
						tmp += f"data modify storage lthc.chemistry:main REGISTRY.Items.{calculated} "
						tmp += 'set value {Slot:16b,id:"minecraft:repeating_command_block",Count:1b,tag:{ctc:{id:"'
						tmp += element.name.lower()
						tmp += '_solid",from:"lthc.chemistry",traits:{solid:1b}}'
						tmp += f",CustomModelData:{calculated},lthc_chemistry:"
						tmp += '{' + f"{element.natural_occurence}:1b"
						tmp += '},display:{Lore:[\'{"translate":"lthcthemaster.lthc.chemistry.lore.tooltip","color":"blue","italic":true}\'],Name:\'[{"translate":"lthcthemaster.lthc.chemistry.items.elements_solid.' + element.name.lower() + '","italic":false,"color":"#ffffff""}]\'}}}'
						register_assembly.append(tmp)
						self.gdm.set_to_json(FIXED_PATH[3] + element.name.lower() + '.json', {"pools": [{"rolls": 1,"bonus_rolls": 0,"entries": [{"type": "minecraft:item","name": "minecraft:repeating_command_block","functions": [{"function": "minecraft:copy_nbt","source": {"type": "minecraft:storage","source": "lthc.chemistry:main"},"ops": [{"source": "REGISTRY.Items."+ str(calculated) +".tag","target": "{}","op": "merge"}]}]}]}]}, False)
						toAdd += 1
						print(f"\033[93m{element.z.Z_str}:\033[0m \033[32mDone\033[0m")

				file_content += '\n'.join(register_assembly)
				file = open(FIXED_PATH[2], "w", encoding='utf-8')
				file.write(file_content)
				file.close()
			case "block":
				file_content = "## BLOCKS\n"
				register_assembly: list[str] = []
				toAdd = 0
				for numlowered, element in enumerate(elements.elements):
					if element.state == "solid" and not element.exclude:
						if isinstance(element.block_image, (DustBlockTextureImage, CopperBlockTextureImage, IronBlockTextureImage, GoldenBlockTextureImage, Image.Image)):
							calculated = 172000 + toAdd
							tmp = "# " + element.name.capitalize() + '\n'
							tmp += f"data modify storage lthc.chemistry:main REGISTRY.Blocks.{calculated} "
							tmp += 'set value {Slot:16b,id:"minecraft:barrel",Count:1b,tag:{ctc:{id:"'
							tmp += element.name.lower()
							tmp += '_block",from:"lthc.chemistry",traits:{solid:1b,block:1b,packed:1b}}'
							tmp += f",CustomModelData:{calculated},lthc_chemistry:"
							tmp += '{' + f"{element.natural_occurence}:1b"
							tmp += '},display:{Lore:[\'{"translate":"lthcthemaster.lthc.chemistry.lore.tooltip","color":"blue","italic":true}\'],Name:\'[{"translate":"lthcthemaster.lthc.chemistry.items.block.' + element.name.lower() + '","italic":false,"color":"#ffffff""}]\'},BlockEntityTag:{Items:[{id:"minecraft:stone",Count:1b,Slot:0b,tag:{smithed:{block:{from:"lthc.chemistry",id:"lthc.chemistry:'
							tmp += element.name.lower()
							tmp += '_block"}}}}]}}}'
							register_assembly.append(tmp)
							self.gdm.set_to_json(FIXED_PATH[5] + element.name.lower() + '.json', {"pools": [{"rolls": 1,"bonus_rolls": 0,"entries": [{"type": "minecraft:item","name": "minecraft:barrel","functions": [{"function": "minecraft:copy_nbt","source": {"type": "minecraft:storage","source": "lthc.chemistry:main"},"ops": [{"source": "REGISTRY.Blocks."+ str(calculated) +".tag","target": "{}","op": "merge"}]}]}]}]}, False)
							toAdd += 1
							print(f"\033[93m{element.z.Z_str}:\033[0m \033[32mDone\033[0m")

				file_content += '\n'.join(register_assembly)
				file = open(FIXED_PATH[4], "w", encoding='utf-8')
				file.write(file_content)
				file.close()
			case _:
				pass
