import re

coordinate = re.compile("(pos_in_mm.*)")  # ((-)?\d+,(-)?\d+)
# mo=coordinate.search("<FD>pos_in_mm(-16,-1928)")

with open("3_22_15_08.txt", "r") as txt:
    text = txt.readlines()
    for tline in text:
        mo = coordinate.search(tline)
        if (mo != None):
            print(mo.groups()[0][9:])
