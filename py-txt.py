import os
import re

import pandas as pd

coordinate = re.compile("(pos_in_mm.*)")  # ((-)?\d+,(-)?\d+)


def remove_brackets(str):
    ll = []
    index = str.find(",")
    ll.append(str[1:index])
    ll.append(str[index + 1:str.find(")")])
    return ll


# mo=coordinate.search("<FD>pos_in_mm(-16,-1928)")
# get the last third coordinate
def get_coordinate(file):
    coo = []
    with open(file, "r") as txt:
        text = txt.readlines()
        for tline in text:
            mo = coordinate.search(tline)
            if (mo != None):
                # print(mo.groups()[0][9:])
                coo.append(remove_brackets(mo.groups()[0][9:]))
    return coo[-3]


def get_txt_file(path1):
    files = []
    for (root, dirs, file) in os.walk(path1):
        for f in file:
            if '.txt' in f:
                real_path = root + '/' + f
                files.append(real_path)
    return files


if __name__ == "__main__":
    all_files = get_txt_file("D:/Files/A-Micro/Test Result/SC351/test0921/13m")
    scoo_all = []
    for file in all_files:
        scoo = get_coordinate(file)
        filename = os.path.splitext(os.path.split(file)[1])[0]
        # print(filename)
        scoo_all.append(scoo)
        print(scoo)
        data = pd.DataFrame(scoo_all, columns=['x', 'y'], index=None)
        data.to_csv("test.csv")
# remove_brackets("(-21,-1987)")
