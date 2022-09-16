# import openpyxl
#
# wb = openpyxl.load_workbook("Rev deck replacement and options.xlsx")
# ws = wb["Sheet1"]
# for row in ws.iter_rows():
#     for cell in row:
#         if "B" in cell.coordinate :
#             print(cell.coordinate, cell.value)
import pandas as pd

df = pd.read_excel("Rev deck replacement and options.xlsx")
df1 = pd.read_excel("20220721 Item Data Dump from LN.xlsx")
# print(df1.head())
for num in range(len(df["Number"])):
    # print(df["Number"][num])
    for i in range(len(df1["ItemNum"])):
        if df1["ItemNum"][i] == df["Number"][num]:
            print(df1["ItemNum"][i])