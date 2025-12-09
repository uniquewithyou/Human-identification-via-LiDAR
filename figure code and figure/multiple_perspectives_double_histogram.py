import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# 分類條件
# categories = ['Normal', 'Carrying', 'Umbrella', 'Occlusion', 'Night', 'Overall']
number_of_layers= ['2 layers', '3 layers', '4 layers']



# 各方法的準確率
# pointgait = [68.6, 56.8, 35.6, 68.8, 61.7, 58.3]
# point_transformer = [53.2, 43.2, 39.1, 47.9, 47.1, 46.1]
# ours = [69.3, 62.1, 52.7, 60.3, 62.5, 61.4]

single_degree_0 = [58.68, 65.23, 69.36]
single_degree_180 = [52.11, 61.89, 63.22]
zero_and_180_pair_degree = [53.42, 62.17, 64.52]
single_degree_45 = [53.29, 56.72, 57.84]
single_degree_225 = [48.65, 49.16, 47.29]
fortyfive_and_225_pair_degree= [48.80, 52.33, 51.26]
single_degree_90 = [43.26, 48.77, 45.21]
single_degree_270 = [44.31, 48.92, 44.83]
ninety_and_270_pair_degree = [47.53, 50.18, 53.25]
single_degree_135 = [48.72, 49.63, 47.37]
single_degree_315 = [52.97, 58.66, 59.70]
one35_and_315_pair_degree  = [49.21, 52.41, 51.89]

# 基本參數
bar_width = 0.10
space = 0.025 # 柱狀圖間距
fontsize = 20
# x = np.arange(len(categories))
x = np.arange(len(number_of_layers))

# # 繪製柱狀圖
# plt.figure(figsize=(12, 6))
# plt.bar(x - bar_width, pointgait, width=bar_width, label='PointGait (2023)', color='crimson')
# plt.bar(x, point_transformer, width=bar_width, label='Point Transformer (2021)', color='steelblue',hatch='//')
# plt.bar(x + bar_width, ours, width=bar_width, label='Ours', color='darkgray',hatch='..')

# 繪製柱狀圖
# plt.figure(figsize=(12, 6))
# plt.bar(x - bar_width-space, ours, width=bar_width, label='Ours', color='white',edgecolor='black')
# plt.bar(x, pointgait , width=bar_width, label='Pointgait',color='white', hatch='/', edgecolor='black')
# plt.bar(x + bar_width+space, point_transformer, width=bar_width, label='Point Transformer',color='white', hatch='.',edgecolor='black')

# plt.figure(figsize=(12, 6))
# plt.bar(x - 3*bar_width - 3*space, single_degree_0, width=bar_width, label='0 degree', color='white',edgecolor='black')
# plt.bar(x - 2*bar_width - 2*space, single_degree_45 , width=bar_width, label='45 degree',color='white', hatch='/', edgecolor='black')
# plt.bar(x - bar_width - space, single_degree_90, width=bar_width, label='90 degree',color='white', hatch='.',edgecolor='black')
# plt.bar(x, single_degree_135, width=bar_width, label='135 degree',color='white', hatch='\\',edgecolor='black')
# plt.bar(x + bar_width + space, single_degree_180, width=bar_width, label='180 degree',color='white', hatch='-\\',edgecolor='black')
# plt.bar(x + 2*bar_width + 2*space, single_degree_225, width=bar_width, label='225 degree',color='white', hatch='/-',edgecolor='black')
# plt.bar(x + 3*bar_width + 3*space, single_degree_270, width=bar_width, label='270 degree',color='white', hatch='x',edgecolor='black')
# plt.bar(x + 4*bar_width + 4*space, single_degree_315, width=bar_width, label='315 degree',color='white', hatch='o',edgecolor='black')

# 繪製柱狀圖
# plt.figure(figsize=(12, 6))
# plt.bar(x - bar_width - space, zero_and_180_pair_degree, width=bar_width, label='0 and 180 pair degree', color='white',edgecolor='black')
# plt.bar(x, fortyfive_and_225_pair_degree, width=bar_width, label='46 and 225 pair degree', color='white',edgecolor='black',hatch='//')
# plt.bar(x + bar_width + space, ninety_and_270_pair_degree, width=bar_width, label='90 and 270 pair degree', color='white',edgecolor='black',hatch='..')
# plt.bar(x + 2*bar_width + 2*space, one35_and_315_pair_degree, width=bar_width, label='135 and 315 pair degree ', color='white',edgecolor='black',hatch='\\')
plt.figure(figsize=(12, 6))
plt.bar(x - 2*bar_width - 2*space, zero_and_180_pair_degree, width=bar_width, label='0 and 180 pair degree', color='white',edgecolor='black')
plt.bar(x - bar_width - space, fortyfive_and_225_pair_degree, width=bar_width, label='46 and 225 pair degree', color='white',edgecolor='black',hatch='//')
plt.bar(x , ninety_and_270_pair_degree, width=bar_width, label='90 and 270 pair degree', color='white',edgecolor='black',hatch='..')
plt.bar(x + bar_width + space, one35_and_315_pair_degree, width=bar_width, label='135 and 315 pair degree ', color='white',edgecolor='black',hatch='\\')
# 座標與標題
# plt.xlabel('Scenarios')
plt.ylabel('Accuracy (%)', fontsize = 16)
# plt.title('Comparison of Different Scenarios')
plt.xticks(x, number_of_layers, fontsize = 16)
plt.yticks(fontsize = 16)
plt.ylim(0, 80)


# 把 xtick labels 往左移 (例如 0.1)
for label in plt.gca().get_xticklabels():
    label.set_horizontalalignment('right')  # 對齊方式改成右對齊
    # label.set_x(label.get_position()[0] - 0.1)  # 向左平移 0.1

# # 顯示數值標籤
# for i in range(len(categories)):
#     plt.text(x[i] - bar_width, pointgait[i] + 1, str(pointgait[i]), ha='center', fontsize=8)
#     plt.text(x[i], point_transformer[i] + 1, str(point_transformer[i]), ha='center', fontsize=8)
#     plt.text(x[i] + bar_width, ours[i] + 1, str(ours[i]), ha='center', fontsize=8)

plt.legend(fontsize = 15) # 添加圖例(右上角)
# plt.legend(fontsize=15, bbox_to_anchor=(1.01, 1), loc='upper left')


plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
plt.savefig('Histogram_of_double_perspectives.png', dpi=300, bbox_inches='tight')