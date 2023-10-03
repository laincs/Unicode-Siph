import time

map = {}
combo = {}
numberCombo = {}

def BuildNumMap():
    i = 0
    aux = " 0123456789"
    for char1 in aux:
        for char2 in aux:
            c = char1 + char2
            numberCombo[c] = i
            i+=1

def BuildReadMap():
    i = 0
    aux = " abcdefghijklmnñopqrstuvwxyz,."
    for char1 in aux:
        for char2 in aux:
            c = char1 + char2
            combo[c] = i
            i+=1

def BuildMap():
    map_dict = {}

    with open('map.txt', 'r', encoding='utf-8') as file:
        i = 0
        for line in file:
            line = line.strip()

            parts = line.split()

            for c in parts:
                c = c.rstrip(',')
                if SearchValueToKey(map_dict, c) == "??":
                    map_dict[i] = c
                    i+=1

    return map_dict



def SynthWord(input_string):
    if len(input_string) % 2 == 1:
        input_string += " "

    separated_list = [input_string[i:i+2] for i in range(0, len(input_string), 2)]
    return NumSynth(separated_list)

def NumSynth(input_string):
    separated_list = []
    for c in input_string:
        if(c[0].isdigit() ^ c[1].isdigit()):
            separated_list.append(f"{c[0]} ")
            separated_list.append(f" {c[1]}")
        else:
            separated_list.append(c)
    return separated_list

def Encode(target):
    value = ""
    for c in target:
        value += map.get(combo.get(c))
    return value

def Decode(target):
    value = ""
    for c in target:
        p1 = SearchValueToKey(map, c)
        if(p1 != "??"):
            p2 = SearchValueToKey(combo, p1)
            value += p2
        else:
            value += "  "
    return value

def SearchValueToKey(dic, target):
    for key, value in dic.items():
        if value == target:
            return key
    return "??"

map = BuildMap()
BuildReadMap()
BuildNumMap()


vin = "aaaaa"
vout = "443"


""" for i in range(0,899):
    print(f"{SearchValueToKey(combinaciones, i)} : {map.get(i)}") """

print(f"Loaded ReadMap: {len(combo)} - Loaded Map: {len(map)} - Num Map {len(numberCombo)}")

print(Encode(SynthWord(vin.lower())))
print(Decode(Encode(SynthWord(vin.lower())))) 
print(Decode(vout))
