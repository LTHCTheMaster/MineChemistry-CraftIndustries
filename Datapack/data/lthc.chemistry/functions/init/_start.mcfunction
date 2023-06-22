tag LTHCTheMaster add convention.debug

function lthc.chemistry:utils/_defs
function lthc.chemistry:utils/checkers/check_minecraft_version

execute if score _defs.checked_version lthc.chemistry._defs matches 1 run function lthc.chemistry:init/_loading_sequence_step_2
execute if score _defs.checked_version lthc.chemistry._defs matches 2 run schedule function lthc.chemistry:init/_start 5t replace
execute if score _defs.checked_version lthc.chemistry._defs matches 0 run tellraw @a[tag=convention.debug] ["",{"text": "MineChemistry CraftIndustries Error: ERROR] MC 1.19.4 is Required","color": "red","bold": true}]
