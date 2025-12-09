import matplotlib.pyplot as plt
import numpy as np

# GCN 層數標籤
number_of_layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN']


# 對應的準確率
vertex_5 = [58.6, 65.2, 69.3]
vertex_7_shoulder = [59.1, 68.7, 74.7]
vertex_7_thigh = [57.9, 65.6, 69.0]
vertex_9 = [58.2, 64.1, 67.3]



# 基本參數
bar_width = 0.10
space = 0.030 # 柱狀圖間距
fontsize = 20
# x = np.arange(len(categories))
x = np.arange(len(number_of_layers))

# 繪製柱狀圖
plt.figure(figsize=(12, 6))
plt.bar(x - bar_width - space, vertex_5, width=bar_width, label='5 Vertices',color='white',edgecolor='black')
# plt.bar(x - bar_width - space, missing_intra, width=bar_width, label='missing_intra', color='white',edgecolor='black')
plt.bar(x, vertex_7_shoulder, width=bar_width, label='7 Vertices(shoulder)',color='white', hatch='/', edgecolor='black')
plt.bar(x + bar_width + space, vertex_7_thigh, width=bar_width, label='7 Vertices(thigh)',color='white', hatch='.',edgecolor='black')
plt.bar(x + 2*bar_width + 2*space, vertex_9, width=bar_width, label='9 Vertices',color='white', hatch='\\',edgecolor='black')



# 座標與標題
# plt.xlabel('Scenarios')
plt.ylabel('Accuracy (%)', fontsize = 16)
# plt.title('Comparison of Different Scenarios')
plt.xticks(x, number_of_layers, fontsize = 16)
plt.yticks(fontsize = 16)
plt.ylim(0, 80)

plt.legend(fontsize = 14) # 添加圖例(右上角)

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
plt.savefig('Histogram_of_vertex_ablation_study.png', dpi=300, bbox_inches='tight')