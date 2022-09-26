import matplotlib.pyplot as plt
import matplotlib.patches as mpathes

fig, ax = plt.subplots()
B = [0.5, 1.5, 2.5, 3.5]

values_11 = [0.0527, 0.8292, 0.8953, 1.0828]
values_20 = [0.1642, 0.2052, 0.6543, 0.8217]
values_8 = [0.0656, 0.2080, 0.5948, 0.8152]
values_14 = [0.6184, 0.2702, 0.2184, 0.2499]
# 绘制时序数据
plt.scatter(B, values_11)
plt.scatter(B, values_20)
plt.scatter(B, values_8)
plt.scatter(B, values_14)

rec = mpathes.Rectangle([B[0], values_11[0]], 3, max(values_11) - min(values_11), color='#ADD8E6', alpha=0.2)
rec1 = mpathes.Rectangle([B[0], values_20[0]], 3, max(values_20) - min(values_20), color='#E6E6FA', alpha=0.2)
rec2 = mpathes.Rectangle([B[0], values_8[0]], 3, max(values_8) - min(values_8), color='#7FFFAA', alpha=0.2)
rec3 = mpathes.Rectangle([B[0], values_14[0]], 3, max(values_14) - min(values_14), color='skyblue', alpha=0.2)
ax.add_patch(rec)
ax.add_patch(rec1)
ax.add_patch(rec2)
ax.add_patch(rec3)
plt.plot(B, values_11, linestyle="solid", color='blue')
plt.plot(B, values_20, linestyle="solid", color='red')
plt.plot(B, values_8, linestyle="solid", color='green')
plt.plot(B, values_14, linestyle="solid", color='black')
# plt.gcf().autofmt_xdate()
plt.title("Encoder Installation Test")
plt.ylabel("The accuracy    %")
plt.xlabel("Installation displacement     mm")
plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# # 函数图
# x = np.arange(0, 3, 0.03)
# y = x ** 2 - 3 * x + 2
# plt.plot(x, y)
# #plt.scatter([1.5], [-0.25], s=25, c='r')  # 标注最小值
# # 点的标签（座标中加减的 `0.15` 是显示位置的偏移，避免挡住点）
# plt.text(1.5 + 0.15, -0.25 - 0.15, 'minima', ha='center', va='bottom', fontsize=10.5)  # horizontal alignment
#
# # 画两条虚线
# plt.plot([0, 1.5], [-0.25, -0.25], c='b', linestyle='--')
# plt.plot([1.5, 1.5], [0, -0.25], c='b', linestyle='--')
#
# # # 座标轴调位
# # ax = plt.gca()
# # # 移到原点
# # ax.xaxis.set_ticks_position('bottom')
# # ax.yaxis.set_ticks_position('left')
# # ax.spines['bottom'].set_position(('data', 0))
# # ax.spines['left'].set_position(('data', 0))
# plt.show()
