import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 加载点云数据
try:
    with open('./000/08-sync-000-LiDAR-PCDs.pkl', 'rb') as f:
        data = pickle.load(f)
except Exception as e:
    print("An error occurred:", e)

# 計算前 10 幀 (data[0] ~ data[9]) 的點數
point_counts = []
for i in range(len(data)-1):
    num_points = data[i].shape[0]
    point_counts.append({"Frame": i, "NumPoints": num_points})
    print(f"Frame {i}: {num_points} points")

# 存成 DataFrame
df = pd.DataFrame(point_counts)

# 輸出到 CSV
df.to_csv("point_counts_0_to_9.csv", index=False)
print("✅ 已經把每幀的點數存成 point_counts_0_to_29.csv")

# 畫折線圖
plt.figure(figsize=(8,5))
plt.plot(df["Frame"], df["NumPoints"], marker="o", linestyle="-", linewidth=2)
plt.title("Point Counts per Frame (0-29)")
plt.xlabel("Frame Index")
plt.ylabel("Number of Points")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("point_counts_lineplot.png", dpi=300)  # 儲存成 PNG
plt.show()
