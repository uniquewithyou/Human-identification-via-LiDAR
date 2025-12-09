import matplotlib.pyplot as plt

"""
8 edges(left hand to right foot)
"""

# # GCN 層數標籤
# layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN']

# # 對應的準確率
# edges_4 = [52.8, 53.7, 54.1]
# edges_6 = [58.6, 65.2, 69.3]
# edges_8 = [58.0, 64.6, 64.5]
# edges_10 = [51.2, 56.9, 55.1]

# # 繪製折線圖
# plt.figure(figsize=(8, 5))
# plt.plot(layers, edges_4, marker='o', label='4 edges')
# plt.plot(layers, edges_6, marker='s', label='6 edges')
# plt.plot(layers, edges_8, marker='^', label='8 edges')
# plt.plot(layers, edges_10, marker='x', label='10 edges')


# # 標題與標籤
# # plt.title('Different Edge Counts')
# # plt.xlabel('GCN Layers')
# plt.xticks(fontsize=14)
# plt.ylabel('Accuracy(%)',fontsize=14)
# plt.yticks(fontsize=14)
# plt.ylim(0, 100)
# plt.grid(True)
# plt.legend(fontsize=13)

# # 顯示圖形
# plt.tight_layout()
# plt.show()
# plt.savefig('Edge_ablation_study(8 edges(left hand to right foot)).png', dpi=300)


"""
8 edges(left hand to right hand)
"""

# GCN 層數標籤
layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN']

# 對應的準確率
edges_4 = [52.8, 53.7, 54.1]
edges_6 = [58.6, 65.2, 69.3]
edges_8 = [57.2, 62.1, 63.5]
edges_10 = [51.2, 56.9, 55.1]

# 繪製折線圖
plt.figure(figsize=(8, 5))
plt.plot(layers, edges_4, marker='o', label='4 edges')
plt.plot(layers, edges_6, marker='s', label='6 edges')
plt.plot(layers, edges_8, marker='^', label='8 edges')
plt.plot(layers, edges_10, marker='x', label='10 edges')


# 標題與標籤
# plt.title('Different Edge Counts')
# plt.xlabel('GCN Layers')
plt.xticks(fontsize=14)
plt.ylabel('Accuracy(%)',fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(0, 100)
plt.grid(True)
plt.legend(fontsize=13)

# 顯示圖形
plt.tight_layout()
plt.show()
plt.savefig('Edge_ablation_study(8 edges(left hand to right hand)).png', dpi=300)