import matplotlib.pyplot as plt
import numpy as np

"""
8 edges(left hand to right foot)
"""

# # GCN 層數標籤
# number_of_layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN']


# # 對應的準確率
# edges_4 = [52.8, 53.7, 54.1]
# edges_6 = [58.6, 65.2, 69.3]
# edges_8 = [58.0, 64.6, 64.5]
# edges_10 = [51.2, 56.9, 55.1]



# # 基本參數
# bar_width = 0.10
# space = 0.030 # 柱狀圖間距
# fontsize = 20
# # x = np.arange(len(categories))
# x = np.arange(len(number_of_layers))

# # 繪製柱狀圖
# plt.figure(figsize=(12, 6))
# plt.bar(x - bar_width - space, edges_4, width=bar_width, label='4 edges',color='white',edgecolor='black')
# # plt.bar(x - bar_width - space, missing_intra, width=bar_width, label='missing_intra', color='white',edgecolor='black')
# plt.bar(x, edges_6, width=bar_width, label='6 edges ',color='white', hatch='/', edgecolor='black')
# plt.bar(x + bar_width + space, edges_8, width=bar_width, label='8 edges(left hand to right foot)',color='white', hatch='.',edgecolor='black')
# plt.bar(x + 2*bar_width + 2*space, edges_10, width=bar_width, label='10 edges',color='white', hatch='\\',edgecolor='black')




# # 座標與標題
# # plt.xlabel('Scenarios')
# plt.ylabel('Accuracy (%)', fontsize = 16)
# # plt.title('Comparison of Different Scenarios')
# plt.xticks(x, number_of_layers, fontsize = 16)
# plt.yticks(fontsize = 16)
# plt.ylim(0, 80)

# plt.legend(fontsize = 15) # 添加圖例(右上角)

# plt.grid(axis='y', linestyle='--', alpha=0.6)
# plt.tight_layout()
# plt.show()
# plt.savefig('Histogram_of_edge_ablation_study(8 edges(left hand to right foot)).png', dpi=300, bbox_inches='tight')







"""
8 edges(left hand to right hand)
"""

# GCN 層數標籤
number_of_layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN']


# 對應的準確率
edges_4 = [52.8, 53.7, 54.1]
edges_6 = [58.6, 65.2, 69.3]
edges_8 = [57.2, 62.1, 63.5]
edges_10 = [51.2, 56.9, 55.1]



# 基本參數
bar_width = 0.10
space = 0.030 # 柱狀圖間距
fontsize = 20
# x = np.arange(len(categories))
x = np.arange(len(number_of_layers))

# 繪製柱狀圖
plt.figure(figsize=(12, 6))
plt.bar(x - bar_width - space, edges_4, width=bar_width, label='4 edges',color='white',edgecolor='black')
# plt.bar(x - bar_width - space, missing_intra, width=bar_width, label='missing_intra', color='white',edgecolor='black')
plt.bar(x, edges_6, width=bar_width, label='6 edges ',color='white', hatch='/', edgecolor='black')
plt.bar(x + bar_width + space, edges_8, width=bar_width, label='8 edges(left hand to right hand)',color='white', hatch='.',edgecolor='black')
plt.bar(x + 2*bar_width + 2*space, edges_10, width=bar_width, label='10 edges',color='white', hatch='\\',edgecolor='black')




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
plt.savefig('Histogram_of_edge_ablation_study(8 edges(left hand to right hand)).png', dpi=300, bbox_inches='tight')