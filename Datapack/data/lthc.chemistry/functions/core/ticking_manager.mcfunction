scoreboard players add #tick_2 lthc.chemistry.data 1
execute if score #tick_2 lthc.chemistry.data matches 2.. run function lthc.chemistry:core/tick_machine/tick_2

schedule function lthc.chemistry:core/ticking_manager 1t replace
