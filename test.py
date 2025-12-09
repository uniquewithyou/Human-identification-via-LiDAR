import pickle
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# 加载点云数据
try:
    with open('./000/08-sync-000-LiDAR-PCDs.pkl', 'rb') as f:
        data = pickle.load(f)
except Exception as e:
    print("An error occurred:", e)

# 示例点云数据
print("Number of category of point cloud data:", len(data))
point_cloud_data = data[4]  
print("Point cloud data shape:", point_cloud_data.shape)
print("Number of category of point cloud data:", len(data))

# 创建颜色数组，初始化为蓝色 (所有点为蓝色)
colors = np.full((point_cloud_data.shape[0], 3), [0, 0, 255], dtype=int)  # 蓝色RGB(0, 0, 255)

# # 将目标点 (例如第1个点) 设为红色
# target_index = 0 # 选择你想标记的点
# colors[target_index] = [255, 0, 0]  # 红色RGB(255, 0, 0)

# 将RGB颜色数组转为 Plotly 支持的字符串格式
colors_hex = ['rgb({},{},{})'.format(c[0], c[1], c[2]) for c in colors]
# 打印颜色数组的类型
print("Type of colors_hex:", type(colors_hex))
# 打印颜色数组的长度
print("Length of colors_hex:", len(colors_hex))


# 创建散点图，使用自定义颜色
fig = go.Figure(data=[go.Scatter3d(
    x=point_cloud_data[:, 0],
    y=point_cloud_data[:, 1],
    z=point_cloud_data[:, 2],
    mode='markers',
    marker=dict(
        size=3,  # 设置点的大小
        color=colors_hex  # 使用RGB颜色值
    )
)])

# 显示图形
fig.show()
