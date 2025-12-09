import matplotlib.pyplot as plt

# GCN 層數標籤
layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN']

# 對應的準確率
vertex_5 = [58.6, 65.2, 69.3]
vertex_7_shoulder = [59.1, 68.7, 74.7]
vertex_7_thigh = [57.9, 65.6, 69.0]
vertex_9 = [58.2, 64.1, 67.3]

# 繪製折線圖
plt.figure(figsize=(8, 5))
plt.plot(layers, vertex_5, marker='o', label='5 Vertices')
plt.plot(layers, vertex_7_shoulder, marker='s', label='7 Vertices(shoulder) ')
plt.plot(layers, vertex_7_thigh, marker='^', label='7 Vertices(thigh)')
plt.plot(layers, vertex_9, marker='x', label='9 Vertices')
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
plt.savefig('Vertex_ablation_study.png', dpi=300)