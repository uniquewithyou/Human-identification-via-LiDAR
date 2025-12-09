import matplotlib.pyplot as plt

# X 軸 (人數)
x = [5, 10, 15]

# Y 軸 (轉換為小時數據)
pointgait = [2 + 27/60, 6 + 38/60, 12 + 47/60]  # [2.45, 6.63, 12.78]
point_transformer = [8 + 31/60, 20 + 14/60, 31 + 25/60]  # [8.52, 20.23, 31.42]
ours = [1 + 11/60, 2 + 38/60, 3 + 49/60]  # [1.18, 2.63, 3.82]

# 畫折線圖
plt.figure(figsize=(8,6))
plt.plot(x, ours, marker="o", linestyle="-", linewidth=2, label="Ours")
plt.plot(x, point_transformer, marker="s", linestyle="-", linewidth=2, label="Point Transformer (2021)")
plt.plot(x, pointgait, marker="^", linestyle="-", linewidth=2, label="PointGait (2023)")

# 標籤與標題
plt.xlabel("Person per group", fontsize=12)
plt.ylabel("Training Time (hours)", fontsize=12)
# plt.title("Training Time Comparison", fontsize=14)
plt.xticks(x)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.show()
plt.savefig('Execution_Time_with_Different_Data_Size.png', dpi=300, bbox_inches='tight')