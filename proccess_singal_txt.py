import os
import re
import sys

import pandas as pd

coordinate = re.compile("(pos_in_mm.*)")  # ((-)?\d+,(-)?\d+)


def remove_brackets(str):
    ll = []
    index = str.find(",")
    ll.append(str[1:index])
    ll.append(str[index + 1:str.find(")")])
    return ll


def get_path():
    if len(sys.argv) < 2:
        print("Please try again")
        sys.exit()
    path = sys.argv[1]
    rel_path = os.path.split(path)
    basepath = rel_path[0]
    filename = rel_path[1]
    exe_name = os.path.splitext(filename)
    rel_filename = exe_name[0]
    return path, basepath, rel_filename


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
    return coo


def main():
    # for file in all_files:
    filepath, basepath, real_filename = get_path()
    scoo = get_coordinate(filepath)
    # print(scoo)
    # convert array to dataframe
    data = pd.DataFrame(scoo, columns=['x', 'y'], index=None)
    data.to_csv(basepath + '/' + real_filename + ".csv", index=False)


if __name__ == "__main__":
    main()
