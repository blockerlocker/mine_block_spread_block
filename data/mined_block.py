import os, json, sys, urllib.request, re
from pathlib import Path


if len(sys.argv) > 1:
    MCVERSION = sys.argv[1]
else:
#### SET MINECRAFT VERSION MANUALLY HERE ####
    MCVERSION = "latest-snapshot"


os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not Path.cwd().name == "data":
    print(f"Working directory not named 'data'! Instead got '{Path.cwd().name}'. bldp generation scripts must be stored within the 'data' folder of your pack to generate correctly!")
    input("Press Enter to exit program...")
    sys.exit()

if not Path("bldp.py").is_file():
    with open("bldp.py", "w", encoding="utf-8") as bldp_main:
        bldp_main.write(urllib.request.urlopen("https://raw.githubusercontent.com/blockerlocker/bldp/main/data/bldp.py").read().decode('utf-8'))

import bldp

MCVERSION = bldp.get_version(MCVERSION)

bldp.remove_path("bldp/function/mined_block")
bldp.remove_path("bldp/predicate/mined_block.json")

block_list = bldp.get_registry_data(MCVERSION,"block")

predicate_template = {
        "type": "minecraft:any_of",
        "terms": []
    }

for block in block_list:
    term_template = {
            "type": "minecraft:entity_scores",
            "entity": "this",
            "scores": {}
        }
    
    term_template["scores"]["bldp.mined."+block] = {"min": 1}

    predicate_template["terms"].append(term_template)

bldp.json_to_file(predicate_template,"bldp/predicate","mined_block")

load_commands = [re.sub("(^.*$)",r"scoreboard objectives add bldp.mined.\1 minecraft.mined:\1",block) for block in block_list]
load_commands.insert(0,"scoreboard objectives add bldp.blocks_mined dummy")
load_function = "\n".join(load_commands)
bldp.string_to_file(load_function,"bldp/function/mined_block","load.mcfunction")

reset_function = "\n".join([re.sub("(^.*$)",r"scoreboard players reset @s bldp.mined.\1",block) for block in block_list])
bldp.string_to_file(reset_function,"bldp/function/mined_block","reset.mcfunction")

identify_function = "\n".join([re.sub("(^.*$)",r"execute if score @s bldp.mined.\1 matches 1.. run data modify storage bldp:mined_block out set value \1",block) for block in block_list])
bldp.string_to_file(identify_function,"bldp/function/mined_block","identify.mcfunction")

add_function = "\n".join([re.sub("(^.*$)",r"execute if score @s bldp.mined.\1 matches 1.. run scoreboard players operation @s bldp.blocks_mined += @s bldp.mined.\1",block) for block in block_list])
bldp.string_to_file(add_function,"bldp/function/mined_block","add.mcfunction")

bldp.tag_append("bldp/tags/function","load","bldp:mined_block/load")
bldp.tag_append("minecraft/tags/function","load","#bldp:load")