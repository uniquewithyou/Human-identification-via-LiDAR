import matplotlib.pyplot as plt
import numpy as np  # 先匯入 numpy

# GCN 層數標籤
layers = ['After 1 block', 'After 2 block', 'After 3 block']

# 對應的準確率
three_layer_GCN = [58.9, 65.2,np.nan]  # 使用 nan 來表示缺失值

four_layer_GCN = [60.2, 62.7, 69.3]

# 繪製折線圖
plt.figure(figsize=(8, 5))
plt.plot(layers, three_layer_GCN , marker='o', label='3 layer GCN')
plt.plot(layers, four_layer_GCN, marker='s', label='4 layer GCN')
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
plt.savefig('Residual_link_ablation_study.png', dpi=300)


