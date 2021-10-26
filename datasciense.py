import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DG_weather.csv", encoding='utf-8', header=None)
df1 = df.iloc[1:10]
df1.loc[:][1] = df1[1].str[0:2]
# delete    df1['temp'] = df.loc[>0,1]=#df1[1].str[0:4]
df1.loc[:][1] = pd.to_numeric(df1.loc[:][1])
df1.to_csv('dg_weather1.csv', index=False, encoding='utf-8')
new_data = pd.read_csv("dg_weather1.csv", header=None, encoding='utf-8')
plt.plot(new_data[0], new_data[1], color='blue', linewidth=3.0)
plt.axis([new_data[0][1], new_data[0][8], 10, 42])
plt.title("DG Daily Temperature", fontdict={'fontname': "Comic Sans MS", 'fontsize': 20})
plt.xlabel('Time', fontdict={'fontname': "Comic Sans MS", 'fontsize': 15})
plt.ylabel("Temp", fontdict={'fontname': "Comic Sans MS", 'fontsize': 15})
plt.show()

# df = pd.read_csv('./movies/douban.csv')
# # # print(df.head())
# files = [file for file in os.listdir('movies')]
# all_months_data = pd.DataFrame()
# for file in files:
#     all_months_data = pd.concat([all_months_data, df])
# all_months_data.to_csv('all_data.csv', index=False, encoding='utf-8-sig')
# all_data = pd.read_csv("all_data.csv")
# # all_data['Year'] = all_data["描述"].str[0:4]
# all_data["Year"] = all_data["描述"].apply(lambda x: x.split("/")[0].strip())
# # all_data['Year']=all_data['Year'].astype("int32")
# all_data['Year'] = pd.to_numeric(all_data['Year'])
# # results = all_data.groupby("Year").sum()
# count_year = all_data['Year'].value_counts().values
# print(count_year)
#
# # years=range(Count_Year[0])
# plt.plot(all_data['Year'].value_counts().keys(), count_year)
# plt.ylabel("Movie counts")
# plt.xlabel("Year")
# plt.show()
