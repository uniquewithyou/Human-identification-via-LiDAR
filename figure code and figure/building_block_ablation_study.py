import matplotlib.pyplot as plt

# GCN 層數標籤
layers = ['2 layers GCN', '3 layers GCN', '4 layers GCN']

# 對應的準確率
missing_intra = [37.6, 39.7, 39.3]
missing_cross = [22.1, 24.2, 23.5]
original = [58.6, 65.2, 69.3]


# 繪製折線圖
plt.figure(figsize=(8, 5))
plt.plot(layers, missing_intra, marker='o', label='missing intra-frame')
plt.plot(layers, missing_cross, marker='s', label='missing cross-frame')
plt.plot(layers, original, marker='^', label='original')



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
plt.savefig('Building_block_ablation_study.png', dpi=300)