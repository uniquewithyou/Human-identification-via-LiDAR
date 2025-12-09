import matplotlib.pyplot as plt

# GCN 層數標籤
layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN', '5 layers GCN']

# 對應的準確率
edges_4 = [52.8, 53.7, 54.1, 53.0]
edges_6 = [58.6, 65.2, 69.3, 62.7]

# 繪製折線圖
plt.figure(figsize=(8, 5))
plt.plot(layers, edges_4, marker='o', label='4 edges')
plt.plot(layers, edges_6, marker='s', label='6 edges')

# 標題與標籤
# plt.title('Different Edge Counts')
# plt.xlabel('GCN Layers')
plt.xticks(fontsize=14)
plt.ylabel('Accuracy(%)',fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(0, 80)
plt.grid(True)
plt.legend()

# 顯示圖形
plt.tight_layout()
plt.show()
plt.savefig('Different GCN Layers with Different Edges.png', dpi=300)