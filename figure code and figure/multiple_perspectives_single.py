import matplotlib.pyplot as plt

"""
0 and 180 degree
"""
# # GCN 層數標籤
# layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN']

# # 對應的準確率
# # edges_4 = [16.1, 18.3, 17.9]
# single_degree_0 = [58.68, 65.23, 69.36]
# single_degree_180 = [52.11, 61.89, 63.22]
# pair_degree = [53.42, 62.17, 64.52]

# # 繪製折線圖
# plt.figure(figsize=(8, 5))
# plt.plot(layers, single_degree_0, marker='o', label='0 degree')
# plt.plot(layers, single_degree_180, marker='s', label='180 degree')
# plt.plot(layers, pair_degree, marker='^', label='0 and 180 degree')
# # 標題與標籤
# # plt.title('Different Edge Counts')
# # plt.xlabel('GCN Layers')
# plt.xticks(fontsize=14)
# plt.ylabel('Accuracy(%)',fontsize=14)
# plt.yticks(fontsize=14)
# plt.ylim(0, 100)
# plt.grid(True)
# plt.legend(fontsize=14)

# # 顯示圖形
# plt.tight_layout()
# plt.show()
# plt.savefig('Multiple_perspective(0 and 180 degree).png', dpi=300)



"""
45 and 225 degree
"""
# # GCN 層數標籤
# layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN']

# # 對應的準確率
# # edges_4 = [16.1, 18.3, 17.9]
# single_degree_45 = [53.29, 56.72, 57.84]
# single_degree_225 = [48.65, 49.16, 47.29]
# pair_degree = [48.80, 52.33, 51.26]

# # 繪製折線圖
# plt.figure(figsize=(8, 5))
# plt.plot(layers, single_degree_45, marker='o', label='45 degree')
# plt.plot(layers, single_degree_225, marker='s', label='225 degree')
# plt.plot(layers, pair_degree, marker='^', label='45 and 225 degree')
# # 標題與標籤
# # plt.title('Different Edge Counts')
# # plt.xlabel('GCN Layers')
# plt.xticks(fontsize=14)
# plt.ylabel('Accuracy(%)',fontsize=14)
# plt.yticks(fontsize=14)
# plt.ylim(0, 100)
# plt.grid(True)
# plt.legend(fontsize=14)

# # 顯示圖形
# plt.tight_layout()
# plt.show()
# plt.savefig('Multiple_perspective(45 and 225 degree).png', dpi=300)



"""
90 and 270 degree
"""

# # GCN 層數標籤
# layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN']

# # 對應的準確率
# # edges_4 = [16.1, 18.3, 17.9]
# single_degree_90 = [43.26, 48.77, 45.21]
# single_degree_270 = [44.31, 48.92, 44.83]
# pair_degree = [47.53, 50.18, 53.25]

# # 繪製折線圖
# plt.figure(figsize=(8, 5))
# plt.plot(layers, single_degree_90, marker='o', label='90 degree')
# plt.plot(layers, single_degree_270, marker='s', label='270 degree')
# plt.plot(layers, pair_degree, marker='^', label='90 and 270 degree')
# # 標題與標籤
# # plt.title('Different Edge Counts')
# # plt.xlabel('GCN Layers')
# plt.xticks(fontsize=14)
# plt.ylabel('Accuracy(%)',fontsize=14)
# plt.yticks(fontsize=14)
# plt.ylim(0, 100)
# plt.grid(True)
# plt.legend(fontsize=14)

# # 顯示圖形
# plt.tight_layout()
# plt.show()
# plt.savefig('Multiple_perspective(90 and 270 degree).png', dpi=300)

"""
135 and 315 degree
"""

# GCN 層數標籤
layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN']

# 對應的準確率
# edges_4 = [16.1, 18.3, 17.9]
single_degree_135 = [48.72, 49.63, 47.37]
single_degree_315 = [52.97, 58.66, 59.70]
pair_degree = [49.21, 52.41, 51.89]

# 繪製折線圖
plt.figure(figsize=(8, 5))
plt.plot(layers, single_degree_135, marker='o', label='135 degree')
plt.plot(layers, single_degree_315, marker='s', label='315 degree')
plt.plot(layers, pair_degree, marker='^', label='135 and 315 degree')
# 標題與標籤
# plt.title('Different Edge Counts')
# plt.xlabel('GCN Layers')
plt.xticks(fontsize=14)
plt.ylabel('Accuracy(%)',fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(0, 100)
plt.grid(True)
plt.legend(fontsize=14)

# 顯示圖形
plt.tight_layout()
plt.show()
plt.savefig('Multiple_perspective(135 and 315 degree).png', dpi=300)
