import pickle
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Farthest Point Sampling (FPS) implementation
def farthest_point_sampling(point_cloud, num_samples):
    # 点云大小
    N, D = point_cloud.shape
    # 初始化
    centroids = np.zeros((num_samples, D))  # 关键点的数组
    distances = np.ones((N,)) * 1e10  # 记录每个点到已选点的最小距离
    farthest = np.random.randint(0, N)  # 随机选择第一个点
    for i in range(num_samples):
        centroids[i] = point_cloud[farthest]
        dist = np.sum((point_cloud - point_cloud[farthest]) ** 2, axis=1)  # 计算所有点到当前选点的距离
        mask = dist < distances  # 更新到选点的最小距离
        distances[mask] = dist[mask]
        farthest = np.argmax(distances)  # 选择距离最远的点
    return centroids


# 加载点云数据
try:
    with open('./000/08-sync-000-LiDAR-PCDs.pkl', 'rb') as f:
        data = pickle.load(f)
except Exception as e:
    print("An error occurred:", e)

# 示例点云数据
point_cloud_data = data[0]  
print("Point cloud data shape:", point_cloud_data.shape)
print("Number of category of point cloud data:", len(data))



# 使用 FPS 采样关键点
num_samples = 20  # 设置要采样的点的数量
key_points = farthest_point_sampling(point_cloud_data, num_samples)






# 将所有点初始化为蓝色
colors = np.full((point_cloud_data.shape[0], 3), [0, 0, 255], dtype=int)  # 蓝色RGB(0, 0, 255)

# 查找哪些点属于关键点，并将它们设为红色
for key_point in key_points:
    distances = np.sum((point_cloud_data - key_point) ** 2, axis=1)
    closest_index = np.argmin(distances)  # 找到最接近关键点的索引
    colors[closest_index] = [255, 0, 0]  # 将关键点设为红色 (RGB)

# 将RGB颜色数组转为 Plotly 支持的字符串格式
colors_hex = ['rgb({},{},{})'.format(c[0], c[1], c[2]) for c in colors]

# 可视化点云，显示关键点
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


# 打印关键点数量
print("Number of key points:", key_points.shape[0])
