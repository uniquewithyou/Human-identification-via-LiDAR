import pickle
import numpy as np
import plotly.graph_objects as go

# Farthest Point Sampling (FPS) implementation
def farthest_point_sampling(point_cloud, num_samples):
    N, D = point_cloud.shape
    centroids = np.zeros((num_samples, D))  # 关键点数组
    distances = np.ones((N,)) * 1e10  # 记录每个点到已选点的最小距离
    farthest = np.random.randint(0, N)  # 随机选择第一个点
    for i in range(num_samples):
        centroids[i] = point_cloud[farthest]
        dist = np.sum((point_cloud - point_cloud[farthest]) ** 2, axis=1)  # 计算所有点到当前点的距离
        mask = dist < distances  # 更新距离
        distances[mask] = dist[mask]
        farthest = np.argmax(distances)  # 选择距离最远的点
    return centroids

# Ball query implementation
def ball_query(point_cloud, centroids, radius):
    groups = []
    for centroid in centroids:
        distances = np.linalg.norm(point_cloud - centroid, axis=1)
        group = point_cloud[distances < radius]  # 找到距离小于半径的点
        groups.append(group)
    return groups

# 加载点云数据
try:
    with open('./000/08-sync-000-LiDAR-PCDs.pkl', 'rb') as f:
        data = pickle.load(f)
except Exception as e:
    print("An error occurred:", e)                    -0.

# 示例点云数据
point_cloud_data = data[0]
print("Point cloud data shape:", point_cloud_data.shape)

# 使用 FPS 采样关键点
num_samples = 10  # 采样点的数量
key_points = farthest_point_sampling(point_cloud_data, num_samples)
print("Key points shape:", key_points.shape)

# 使用 ball query 进行分组
radius = 0.10  # 定义查询的半径
groups = ball_query(point_cloud_data, key_points, radius)

# 为可视化创建颜色数组，初始化为蓝色
colors = np.full((point_cloud_data.shape[0], 3), [0, 0, 255], dtype=int)

# 分配不同的颜色给每个组
for i, group in enumerate(groups):
    color = np.random.randint(0, 255, size=3)  # 随机生成颜色
    for point in group:
        distances = np.sum((point_cloud_data - point) ** 2, axis=1)
        closest_index = np.argmin(distances)
        colors[closest_index] = color  # 将分组点的颜色设置为该组的颜色

# 将RGB颜色数组转为 Plotly 支持的字符串格式
colors_hex = ['rgb({},{},{})'.format(c[0], c[1], c[2]) for c in colors]

# 创建3D点云图，并使用分组后的颜色
fig = go.Figure(data=[go.Scatter3d(
    x=point_cloud_data[:, 0],
    y=point_cloud_data[:, 1],
    z=point_cloud_data[:, 2],
    mode='markers',
    marker=dict(
        size=3,  # 设置点的大小
        color=colors_hex  # 使用分组后的RGB颜色值
    )
)])

# 显示图形
fig.show()

# 打印关键点数量
print("Number of key points:", key_points.shape[0])
