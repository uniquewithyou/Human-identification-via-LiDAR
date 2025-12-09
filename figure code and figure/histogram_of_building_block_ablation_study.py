import matplotlib.pyplot as plt
import numpy as np

# GCN 層數標籤
number_of_layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN']

# 對應的準確率
missing_intra = [37.6, 39.7, 39.3]
missing_cross = [22.1, 24.2, 23.5]
Ours = [58.6, 65.2, 69.3]



# 基本參數
bar_width = 0.08
space = 0.025 # 柱狀圖間距
fontsize = 20
# x = np.arange(len(categories))
x = np.arange(len(number_of_layers))

# 繪製柱狀圖
plt.figure(figsize=(12, 6))
plt.bar(x - bar_width - space, Ours, width=bar_width, label='ours',color='white',edgecolor='black')
# plt.bar(x - bar_width - space, missing_intra, width=bar_width, label='missing_intra', color='white',edgecolor='black')
plt.bar(x, missing_intra, width=bar_width, label='missing_cross ',color='white', hatch='/', edgecolor='black')
plt.bar(x + bar_width + space, missing_cross, width=bar_width, label='missing_intra',color='white', hatch='.',edgecolor='black')



# 座標與標題
# plt.xlabel('Scenarios')
plt.ylabel('Accuracy (%)', fontsize = 16)
# plt.title('Comparison of Different Scenarios')
plt.xticks(x, number_of_layers, fontsize = 16)
plt.yticks(fontsize = 16)
plt.ylim(0, 80)

plt.legend(fontsize = 15) # 添加圖例(右上角)

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
plt.savefig('Histogram_of_building_block_ablation_study.png', dpi=300, bbox_inches='tight')



