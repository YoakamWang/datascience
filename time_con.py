# https://stackoverflow.com/questions/45286086/how-to-convert-strftime-or-string-format-to-timestamp-date-in-python
# https://www.programiz.com/python-programming/datetime/strptime
# https://www.educba.com/timestamp-to-date-in-python/#:~:text=The%20timestamp%20to%20date%20is%20the%20conversion%20of,to%20date%20using%20the%20installed%20module%20or%20method.

# import datetime as dt
# from datetime import datetime
# import time
#
# import pandas as pd
#
# now1 = dt.datetime.now()
# current_month = now1.month
# current_year = now1.year
# month_start_date = dt.datetime.today().strftime("%Y/%m/01")
# month_end_date = "30"
# final_month_end_date = dt.datetime.today().strftime("%Y/%m/" + month_end_date)
#
# # Use datetime.strptime to convert from string to datetime
# month_start = datetime.strptime(month_start_date, "%Y/%m/%d")
# month_end = datetime.strptime(final_month_end_date, "%Y/%m/%d")
# # datetime to timestamp
# time_start = datetime.strptime("2022.07.21 10:22:59", "%Y.%m.%d %H:%M:%S")
# # Use time.mktime to convert datetime to timestamp    "2022.07.22 13:19:25"
# timestamp_start = time.mktime(time_start.timetuple())
# timestamp_end = timestamp_start + 3600
# # timestamp to datetime
# datetime_end = datetime.fromtimestamp(timestamp_end).strftime("%Y.%m.%d %H:%M:%S")
# # Let's print the time stamps
# # print("Start timestamp: {0}".format(timestamp_start))
# # print("End timestamp: {0}".format(datetime_end))
#
# # print("The element", searchValue, " is found at: ", index)
# with open("wavedata_save07211127.csv") as f:
#     data = pd.read_csv(f)
#     time_start1 = datetime.strptime(data.date[2], "%Y.%m.%d %H:%M:%S")
#     # Use time.mktime to convert datetime to timestamp    "2022.07.22 13:19:25"
#     timestamp_start1 = time.mktime(time_start1.timetuple())
#     timestamp_end1 = timestamp_start1 + 3000
#     datetime_end1 = datetime.fromtimestamp(timestamp_end1).strftime("%Y.%m.%d %H:%M:%S")
#     print(datetime_end1)
#     # print(data['date'])
#     index = 0
#     # arr = data.date
#     # searchValue = datetime_end1
#     # index1 = arr.index(searchValue)
#     while index < len(data['date']):
#         if data.date[index] == datetime_end1:
#             print(index)
#             break
#         index += 1
# print(data)

def f1(a, b, c=0, *args, **kw):
    print("a = ", a, "b = ", b, "c = ", c, "args = ", args, "kw = ", kw)


def f2(a, b, c=0, *, d, **kw):
    print("a = ", a, "b = ", b, "c = ", c, "d = ", d, "kw = ", kw)


f1(1, 2)

f1(1, 2, c=3)

f1(1, 2, 3, 'a', 'b')

f1(1, 2, 3, 4, 'a', 'b', x=99)

f2(1, 2, d=99, ext=None)
