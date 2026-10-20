For Minecraft 26.4

When a block is broken, it spreads itself to nearby blocks. So if you break a Diamond Ore, all of the Stone blocks touching the Diamond Ore get converted into a Diamond Ore. And if you break a Dandelion, the Grass block beneath the Dandelion becomes a Dandelion.

## How does it work?
This pack uses my mini data pack `when_block_mined` in order to run any command whenever and wherever the player mined a block. `when_block_mined` uses the data pack library [Iris by Aeldrion](https://github.com/Aeldrion/Iris) in order to get the mined block's location, and the `mined_block` module from my personal data pack library [bldp](https://github.com/blockerlocker/bldp) to detect when the block is actually mined.