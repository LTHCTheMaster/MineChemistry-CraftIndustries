from .image_builder import elements

FIXED_PATH: tuple[str] = ("Datapack/data/lthc.chemistry/functions/init/_intern/sub_parts/parts/registry/elements.mcfunction",)

class Run:
	def __init__(self):
		pass

	def run(self, cmd: list[str]):
		match cmd[0]:
			case "elements":
				file_content = "## ELEMENTS\n"
				register_assembly: list[str] = []
				for numlowered, element in enumerate(elements.elements):
					tmp = "# " + element.name.capitalize() + '\n'
					tmp += f"data modify storage lthc.chemistry:main REGISTRY.Items.{170000 + numlowered} "
					tmp += 'set value {Slot:16b,id:"minecraft:repeating_command_block",Count:1b,tag:{ctc:{id:"'
					tmp += element.name
					tmp += '",from:"lthc.chemistry",traits:{element:1b}}'
					tmp += f",CustomModelData:{170000 + numlowered},lthc_chemistry:"
					tmp += '{' + f"{element.state}:1b,{element.natural_occurence}:1b"
					tmp += '},display:{Lore:[\'{"translate":"lthcthemaster.lthc.chemistry.lore.tooltip","color":"blue","italic":true}\'],Name:\'[{"translate":"lthcthemaster.lthc.chemistry.items.elements.' + element.name + '","italic":false,"color":"#ffffff""}]\'}}}'
					register_assembly.append(tmp)
				file_content += '\n'.join(register_assembly)
				file = open(FIXED_PATH[0], "w", encoding='utf-8')
				file.write(file_content)
				file.close()
