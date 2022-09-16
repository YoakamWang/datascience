import pandas as pd
import pdfplumber


def extract_table_info(filepath):
    with pdfplumber.open(filepath) as pdf:
        page = pdf.pages[1]
        # table_info = page.extract_table()
        # df_table = pd.DataFrame(table_info[1:], columns=table_info[0])
        # df_table.to_csv('dmeo.csv', index=False, encoding='gbk')
        tables_info = page.extract_tables()
        for index in range(len(tables_info)):
            # 设置表格的第一行为表头，其余为数据
            df_table = pd.DataFrame(tables_info[index][1:], columns=tables_info[index][0])
            print(df_table.iloc[0][3])
            df_table.to_csv('dmeo'+str(index)+".csv", index=False, encoding='gbk')


extract_table_info('56511e00_drw.pdf')
# import pandas as pd
# import tabula
# tabula.convert_into("56112E01_drw.pdf","out.csv",output_format="csv",pages=1)
# table_info.to_csv('dmeo.csv', index=False, encoding='gbk')
# import camelot
# tabals=camelot.read_pdf("56511e00_drw.pdf")
# tabals.export('foo.csv', f='csv', compress=True)
# import tabula
# df=tabula.read_pdf("56112E01_drw.pdf", area=(2200,1220,2800,2462), pages=1)
# for index in range(len(df)):
#     df_table = pd.DataFrame(df[index][1:], columns=df[index])
# print(df_table.head())
# import pdfplumber
# from PyPDF2 import PdfFileReader
#
# pdf_reader=PdfFileReader("56511e00_drw.pdf")
# with pdfplumber.open("56511e00_drw.pdf") as pdf:
#     for i in range(pdf_reader.getNumPages()):
#         page=pdf.pages[i]
#         table=page.extract_tables(table_settings={
# 			"vertical_strategy":"text",
# 			"horizontal_strategy":"text",
# 		})

# import pdfplumber
# from openpyxl import Workbook
# with pdfplumber.open("56511e00_drw.pdf") as pdf:
# 	table_page1 = pdf.pages[0]
# 	table = table_page1.extract_table(
# 		table_settings={
# 			"vertical_strategy":"text",
# 			"horizontal_strategy":"text",
# 		})
# 	print(table)
#
# workbook = Workbook()
# sheet = workbook.active
# for row in table:
# 	if not ''.join([str(item) for item in row]) == '':
# 		sheet.append(row)
# 	workbook.save(filename="4.xlsx")