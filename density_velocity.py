import matplotlib.pyplot as plt

# 資料點
points = {
    "right foot": (5.86, 22),
    "left hand": (3.93, 17),
    "head": (2.97, 13),
    "right hand": (1.31, 10),
    "left foot": (0.19, 5),
}

# 按照速度 (x 值) 排序
sorted_points = sorted(points.items(), key=lambda item: item[1][0])
labels = [item[0] for item in sorted_points]
x_vals = [item[1][0] for item in sorted_points]
y_vals = [item[1][1] for item in sorted_points]

# 畫折線圖
plt.figure(figsize=(8,6))
plt.plot(x_vals, y_vals, marker="o", linestyle="-", linewidth=2, markersize=8,color="blue")

# 標註每個點名稱
for label, x, y in zip(labels, x_vals, y_vals):
    plt.text(x+0.1, y+0.3, label, fontsize=10)

plt.xlabel("Speed (m/s)", fontsize=12)
plt.ylabel("Density (point cloud numbers/cm³)", fontsize=12)
# plt.title("Speed vs Point Cloud Density", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("density_velocity.png", dpi=300)  # 儲存成 PNG
plt.show()
