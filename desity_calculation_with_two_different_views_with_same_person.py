import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_point_counts(file_path, num_frames=30):
    """載入點雲檔案並計算前 num_frames 幀的點數"""
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    
    counts = []
    max_frames = min(len(data), num_frames)
    for i in range(max_frames):
        counts.append({"Frame": i, "NumPoints": data[i].shape[0]})
    return pd.DataFrame(counts)

# 載入兩個不同的資料
file1 = './000/08-sync-000-LiDAR-PCDs.pkl'
file2 = './180/08-sync-180-LiDAR-PCDs.pkl'

df1 = load_point_counts(file1, num_frames=30)
df2 = load_point_counts(file2, num_frames=30)

# 存成 CSV
df1.to_csv("point_counts_data1.csv", index=False)
df2.to_csv("point_counts_data2.csv", index=False)
print("✅ 已存成 point_counts_data1.csv 和 point_counts_data2.csv")

# 畫折線圖
plt.figure(figsize=(10,6))
plt.plot(df1["Frame"], df1["NumPoints"], marker="o", linestyle="-", linewidth=2, label="0 degree", color="blue")
plt.plot(df2["Frame"], df2["NumPoints"], marker="s", linestyle="--", linewidth=2, label="180 degree", color="red")

plt.title("Point Counts per Frame (First 30 Frames)")
plt.xlabel("Frame Index")
plt.ylabel("Number of Points")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("point_counts_comparison_with_differnt_0_and_180_views.png", dpi=300)  # 儲存成 PNG
plt.show()
