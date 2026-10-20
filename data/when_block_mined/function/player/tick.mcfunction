# Detect if player has mined block and run function function
execute if predicate bldp:mined_block run function when_block_mined:player/mined_block

# Mark the block the player is currently looking at
function iris:get_target

tag @s remove when_block_mined_face_up
tag @s remove when_block_mined_face_west
tag @s remove when_block_mined_face_east
tag @s remove when_block_mined_face_north
tag @s remove when_block_mined_face_south
tag @s remove when_block_mined_face_down

execute if data storage iris:output TargetedFace{Direction:UP} run tag @s add when_block_mined_face_up
execute if data storage iris:output TargetedFace{Direction:WEST} run tag @s add when_block_mined_face_west
execute if data storage iris:output TargetedFace{Direction:EAST} run tag @s add when_block_mined_face_east
execute if data storage iris:output TargetedFace{Direction:NORTH} run tag @s add when_block_mined_face_north
execute if data storage iris:output TargetedFace{Direction:SOUTH} run tag @s add when_block_mined_face_south
execute if data storage iris:output TargetedFace{Direction:DOWN} run tag @s add when_block_mined_face_down

# Store the coordinates of the block the player is looking at in a scoreboard
execute store result score @s when_block_mined_last_target_x run data get entity @n[type=marker,tag=iris.targeted_block] Pos[0]
execute store result score @s when_block_mined_last_target_y run data get entity @n[type=marker,tag=iris.targeted_block] Pos[1]
execute store result score @s when_block_mined_last_target_z run data get entity @n[type=marker,tag=iris.targeted_block] Pos[2]
