with open("./data/frame/functions/fill1.mcfunction", "w") as f:
    for z in (-222, -221):
        for x in range(-220, 221):
            f.write(f"summon minecraft:item_frame {x} -59 {z}" + " {Facing:1b}\n")
with open("./data/frame/functions/fill2.mcfunction", "w") as f:
    for x in (-222, -221):
        for z in range(-220, 221):
            f.write(f"summon minecraft:item_frame {x} -59 {z}" + " {Facing:1b}\n")
with open("./data/frame/functions/fill3.mcfunction", "w") as f:
    for z in (222, 221):
        for x in range(-220, 221):
            f.write(f"summon minecraft:item_frame {x} -59 {z}" + " {Facing:1b}\n")
with open("./data/frame/functions/fill4.mcfunction", "w") as f:
    for x in (222, 221):
        for z in range(-220, 221):
            f.write(f"summon minecraft:item_frame {x} -59 {z}" + " {Facing:1b}\n")
