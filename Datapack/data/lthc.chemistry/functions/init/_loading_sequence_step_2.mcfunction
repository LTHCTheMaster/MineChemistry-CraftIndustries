# Basic Scoreboard
scoreboard objectives add lthc.chemistry.data dummy

# Check if it is the datapack first run or an update of the datapack
execute unless score #lthc.chemistry.first_run lthc.chemistry.data matches 1 run function lthc.chemistry:init/_intern/main
execute if score #lthc.first_run lthc.chemistry.data matches 1 unless score #lthc.chemistry load.status matches 010000 run function lthc.chemistry:init/_intern/update

# Summon a marker at the worldspawn for something
execute as @e[type=marker,tag=lthc.chemistry.loading_marker] run function lthc.chemistry:utils/conventions/try_unload
kill @e[type=marker,tag=lthc.chemistry.loading_marker]
summon marker ~ ~1 ~ {Tags:["lthc.chemistry.loading_marker","global.ignore","global.ignore.kill","global.forceload","smithed.entity","smithed.strict"]}
execute as @e[type=marker,tag=lthc.chemistry.loading_marker] at @s run forceload add ~ ~ ~ ~

# Chunkload convention chunk
execute in overworld run forceload add -30000000 1600

# Init the gamerules
gamerule maxCommandChainLength 2147483647

# Start loops
schedule function lthc.chemistry:init/_intern/sub_parts/schedule 1t replace

# Saves that the datapack was started/loaded
scoreboard players set #lthc.chemistry.loaded lthc.chemistry.data 1

tellraw @a[tag=convention.debug] {"text":"[Loaded MineChemistry CraftIndustries v1.0.0]","italic":false,"color":"green"}
