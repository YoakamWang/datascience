import pandas as pd

with open("D:/PDMLink/56414e19 scrub system.xlsx", 'rb') as f:
    data = pd.read_excel(f, dtype=str)
    # print(data["Name"][0])
    for i in range(1, len(data['Level'])):
        # print(i, data['Level'][i])
        if int(data['Level'][i]) == int(data['Level'][i - 1]) + 1:
            print(i, "tttt")
        elif int(data['Level'][i]) == int(data['Level'][i - 1]):
            print(i, "dddd")
            for j in range(len(data['Level'][1:i]), -1, -1):
                if int(data['Level'][j]) == int(data['Level'][i]) - 1:
                    print(j)
                    break
        elif int(data['Level'][i]) < int(data['Level'][i - 1]):
            print(i, "aaaa")
            for jj in range(len(data['Level'][1:i]), -1, -1):
                if int(data['Level'][jj]) == int(data['Level'][i]) - 1:
                    print(data['Level'][jj], data['Level'][i])
                    break
