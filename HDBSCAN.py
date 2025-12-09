import numpy as np
import pickle
import hdbscan
import plotly.graph_objects as go

# 加载人体点云数据
try:
    with open('./000/08-sync-000-LiDAR-PCDs.pkl', 'rb') as f:
        data = pickle.load(f)
except Exception as e:
    print("An error occurred:", e)

# 定义HDBSCAN聚类函数
def cluster_body_parts(point_cloud, min_cluster_size=10, min_samples=5):
    hdb = hdbscan.HDBSCAN(min_cluster_size = min_cluster_size, min_samples = min_samples)
    labels = hdb.fit_predict(point_cloud)

    # 确定不同簇的数量
    unique_labels = np.unique(labels)
    clusters = {label: point_cloud[labels == label] for label in unique_labels if label != -1}  # -1 为噪声点
    print(f"Found {len(clusters)} clusters")
    
    return clusters, labels

# 示例点云数据
point_cloud_data = data[5]
print(data[5].shape)
# 使用HDBSCAN进行初步分群
min_cluster_size = 30  # 调整该参数来控制最小簇大小
min_samples = 5  # 调整该参数来控制邻域的最小样本数量

clusters, labels = cluster_body_parts(point_cloud_data, min_cluster_size = min_cluster_size, min_samples = min_samples)

# 可视化分群结果
# 为每个簇生成不同颜色
colors = np.array([
    [np.random.randint(0, 255) for _ in range(3)] for _ in range(len(np.unique(labels)))
], dtype=int)
colors_hex = ['rgb({},{},{})'.format(color[0], color[1], color[2]) for color in colors[labels]]

fig = go.Figure(data=[go.Scatter3d(
    x=point_cloud_data[:, 0],
    y=point_cloud_data[:, 1],
    z=point_cloud_data[:, 2],
    mode='markers',
    marker=dict(
        size=3,
        color=colors_hex
    )
)])
fig.show()

# 打印每个聚类的点数量
for i, (label, cluster_points) in enumerate(clusters.items()):
    print(f"Cluster {i} (Label {label}): {cluster_points.shape[0]} points")
