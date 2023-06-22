# Set the version of the datapack
scoreboard players set #lthc.chemistry load.status 010000

# Init multiple things
function lthc.chemistry:init/_intern/sub_parts/data

# Saves that the datapack was installed
scoreboard players set #lthc.chemistry.first_run lthc.chemistry.data 1
