execute if data storage when_block_mined:config {identify:true} run function bldp:mined_block/identify
execute if data storage when_block_mined:config {identify:true} run data modify storage when_block_mined:temp all.id set from storage bldp:mined_block out
function bldp:mined_block/reset

execute store result storage when_block_mined:temp all.x int 1 run scoreboard players get @s when_block_mined_last_target_x
execute store result storage when_block_mined:temp all.y int 1 run scoreboard players get @s when_block_mined_last_target_y
execute store result storage when_block_mined:temp all.z int 1 run scoreboard players get @s when_block_mined_last_target_z

function when_block_mined:player/at_block_location with storage when_block_mined:temp all