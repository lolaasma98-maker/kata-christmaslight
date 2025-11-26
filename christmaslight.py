# kata-christmaslight
resolution de l'exercise christmas lights
from collections import namedtuple
from functools import reduce
#j'ai utilisé dans cet exercise fonctional programming
#je veux definir mes instructions au debut

Instruction = namedtuple("Instruction", ["action", "x1", "y1", "x2", "y2"])

# List des instructions
instructions = [
    Instruction("on", 887, 9, 959, 629),
    Instruction("on", 454, 398, 844, 448),
    Instruction("off", 539, 243, 559, 965),
    Instruction("off", 370, 819, 676, 868),
    Instruction("off", 145, 40, 370, 997),
    Instruction("off", 301, 3, 808, 453),
    Instruction("on", 351, 678, 951, 908),
    Instruction("toggle", 720, 196, 897, 994),
    Instruction("toggle", 831, 394, 904, 860)]

# je declare ma matrix pour les lumieres
grid_onoff = [[False]*1000 for _ in range(1000)]    # partie 1
grid_brightness = [[0]*1000 for _ in range(1000)]   # partie 2

# appliquer l'action on off pour la matrix pour partie 1
def apply_onoff(acc, instr):
    for x in range(instr.x1, instr.x2+1):
        for y in range(instr.y1, instr.y2+1):
            if instr.action == "on":
                acc[x][y] = True
            elif instr.action == "off":
                acc[x][y] = False
            elif instr.action == "toggle":
                acc[x][y] = not acc[x][y]
    return acc

# appliquer laction brightness pour partie 2
def apply_brightness(acc, instr):
    for x in range(instr.x1, instr.x2+1):
        for y in range(instr.y1, instr.y2+1):
            if instr.action == "on":
                acc[x][y] += 1
            elif instr.action == "off":
                acc[x][y] = max(0, acc[x][y]-1)
            elif instr.action == "toggle":
                acc[x][y] += 2
    return acc

# appliquer les instruction pour les 2 parties
grid_onoff = reduce(apply_onoff, instructions, grid_onoff)
grid_brightness = reduce(apply_brightness, instructions, grid_brightness)

# le nombre total des lumiére allumés
total_lights_on = sum(light for row in grid_onoff for light in row)

# le nombre  total de brightness (Part Two)
total_brightness = sum(brightness for row in grid_brightness for brightness in row)

print("Part one: Total lights on(le nombre total des lumieres on) =", total_lights_on,"light")
print("Part two: Total brightness (Luminosité totale)=", total_brightness,"bright")
