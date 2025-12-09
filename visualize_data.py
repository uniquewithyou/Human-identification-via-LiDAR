import pickle
import numpy as np
import pandas as pd
import plotly.graph_objects as go
# 000/00-000-LiDAR-PCDs.pkl

# 載入點雲數據
try:
    with open('./000/08-sync-000-LiDAR-PCDs.pkl', 'rb') as f:
        data = pickle.load(f)
except Exception as e:
    print("An error occurred:", e)

# 查看數據結構
point_cloud_data = data[1]  
print("Point cloud data shape:", point_cloud_data.shape)
print("Number of category of point cloud data:", len(data))

# 創建顏色數組，初始為藍色
colors = np.full((point_cloud_data.shape[0], 3), [0, 0, 255], dtype=int)  # 藍色RGB(0, 0, 255)







# 根據高度設置顏色
colors_hex = ['rgb({},{},{})'.format(c[0], c[1], c[2]) for c in colors]
# 打印顏色數組的類型
print("Type of colors_hex:", type(colors_hex))
# 打印顏色數組的長度
print("Length of colors_hex:", len(colors_hex))


# 创建散点图，使用自定义颜色
fig = go.Figure(data=[go.Scatter3d(
    x=point_cloud_data[:, 0],
    y=point_cloud_data[:, 1],
    z=point_cloud_data[:, 2],
    mode='markers',
    marker=dict(
        size=3,  # 設計置點的大小
        color=colors_hex  # 使用RGB颜色值
    )
)])

# 顯示圖形
fig.show()


