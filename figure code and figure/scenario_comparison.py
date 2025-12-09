import matplotlib.pyplot as plt
import numpy as np

# 分類條件
categories = ['Normal', 'Carrying', 'Umbrella', 'Occlusion', 'Night', 'Overall']

# 各方法的準確率
pointgait = [68.6, 56.8, 35.6, 68.8, 61.7, 58.3]
point_transformer = [53.2, 43.2, 39.1, 47.9, 47.1, 46.1]
ours = [69.3, 62.1, 52.7, 60.3, 62.5, 61.4]

# 基本參數
bar_width = 0.17
space = 0.025 # 柱狀圖間距
fontsize = 20
x = np.arange(len(categories))

# # 繪製柱狀圖
# plt.figure(figsize=(12, 6))
# plt.bar(x - bar_width, pointgait, width=bar_width, label='PointGait (2023)', color='crimson')
# plt.bar(x, point_transformer, width=bar_width, label='Point Transformer (2021)', color='steelblue',hatch='//')
# plt.bar(x + bar_width, ours, width=bar_width, label='Ours', color='darkgray',hatch='..')

# 繪製柱狀圖
plt.figure(figsize=(12, 6))
plt.bar(x - bar_width-space, ours, width=bar_width, label='Ours', color='white',edgecolor='black')
plt.bar(x, pointgait , width=bar_width, label='Pointgait',color='white', hatch='/', edgecolor='black')
plt.bar(x + bar_width+space, point_transformer, width=bar_width, label='Point Transformer',color='white', hatch='.',edgecolor='black')

# 座標與標題
# plt.xlabel('Scenarios')
plt.ylabel('Accuracy (%)', fontsize = 16)
# plt.title('Comparison of Different Scenarios')
plt.xticks(x, categories, fontsize = 16)
plt.yticks(fontsize = 16)
plt.ylim(0, 80)

# # 顯示數值標籤
# for i in range(len(categories)):
#     plt.text(x[i] - bar_width, pointgait[i] + 1, str(pointgait[i]), ha='center', fontsize=8)
#     plt.text(x[i], point_transformer[i] + 1, str(point_transformer[i]), ha='center', fontsize=8)
#     plt.text(x[i] + bar_width, ours[i] + 1, str(ours[i]), ha='center', fontsize=8)

plt.legend(fontsize = 15) # 添加圖例(右上角)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
plt.savefig('scenario_comparison.png', dpi=300, bbox_inches='tight')