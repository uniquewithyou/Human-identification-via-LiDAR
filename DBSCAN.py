# import numpy as np
# import pickle
# from sklearn.cluster import DBSCAN
# import plotly.graph_objects as go





# """
# ./000/08-sync-000-LiDAR-PCDs.pkl 是第一個人的正面照
# ./0006/01-cr/
# """
# # 加载人体点云数据
# try:
#     with open('./000/08-sync-000-LiDAR-PCDs.pkl', 'rb') as f:
#         data = pickle.load(f)
# except Exception as e:
#     print("An error occurred:", e)

# # 定义DBSCAN聚类函数
# def cluster_body_parts(point_cloud, eps=0.1, min_samples=10):
#     dbscan = DBSCAN(eps=eps, min_samples=min_samples)
#     labels = dbscan.fit_predict(point_cloud)

#     # 确定不同簇的数量
#     unique_labels = np.unique(labels)
#     clusters = {label: point_cloud[labels == label] for label in unique_labels if label != -1}  # -1 为噪声点
#     print(f"Found {len(clusters)} clusters")
    
#     return clusters, labels
# # 示例点云数据
# point_cloud_data = data[0]
# # 使用DBSCAN进行初步分群
# eps = 0.05  # 调整该参数来适应点云的密度    180 度的視角用eps = 0.086, data[10] better ,min_samples = 45  # 需要根据点云密度调整
# min_samples =  10 # 需要根据点云密度调整

# clusters, labels = cluster_body_parts(point_cloud_data, eps=eps, min_samples=min_samples)

# # 可视化分群结果
# # 为每个簇生成不同颜色
# colors = np.array([
#     [np.random.randint(0, 255) for _ in range(3)] for _ in range(len(np.unique(labels)))
# ], dtype=int)
# colors_hex = ['rgb({},{},{})'.format(color[0], color[1], color[2]) for color in colors[labels]]

# fig = go.Figure(data=[go.Scatter3d(
#     x=point_cloud_data[:, 0],
#     y=point_cloud_data[:, 1],
#     z=point_cloud_data[:, 2],
#     mode='markers',
#     marker=dict(
#         size=3,
#         color=colors_hex
#     )
# )])
# fig.show()

# # 打印每个聚类的点数量
# for i, (label, cluster_points) in enumerate(clusters.items()):
#     print(f"Cluster {i} (Label {label}): {cluster_points.shape[0]} points")


# # import numpy as np
# # import pickle
# # from sklearn.cluster import DBSCAN
# # from scipy.spatial import ConvexHull
# # import plotly.graph_objects as go

# # # 加载人体点云数据
# # try:
# #     with open('./000/08-sync-000-LiDAR-PCDs.pkl', 'rb') as f:
# #     # with open('./180/08-sync-180-LiDAR-PCDs.pkl', 'rb') as f:
# #         data = pickle.load(f)
# # except Exception as e:
# #     print("An error occurred:", e)

# # # 定义DBSCAN聚类函数
# # def cluster_body_parts(point_cloud, eps=0.1, min_samples=10):
# #     dbscan = DBSCAN(eps=eps, min_samples=min_samples)
# #     labels = dbscan.fit_predict(point_cloud)

# #     unique_labels = np.unique(labels)
# #     clusters = {label: point_cloud[labels == label] for label in unique_labels if label != -1}
# #     print(f"Found {len(clusters)} clusters")
    
# #     return clusters, labels

# # # 密度計算函數
# # def compute_cluster_densities(clusters):
# #     densities = {}
# #     for label, points in clusters.items():
# #         if len(points) >= 4:  # ConvexHull 需要至少 4 個點（3D）
# #             try:
# #                 hull = ConvexHull(points)
# #                 volume = hull.volume
# #                 density = len(points) / volume if volume > 0 else np.inf
# #                 densities[label] = density
# #             except Exception as e:
# #                 print(f"Cluster {label}: ConvexHull failed - {e}")
# #                 densities[label] = np.nan
# #         else:
# #             densities[label] = np.nan
# #     return densities

# # # 取得點雲資料
# # point_cloud_data = data[0]
# # print(f"data 有 {point_cloud_data.shape[0]} 個點")

# # # 執行 DBSCAN 分群
# # eps = 0.10
# # min_samples = 45
# # clusters, labels = cluster_body_parts(point_cloud_data, eps=eps, min_samples=min_samples)

# # # 計算每個群的密度
# # densities = compute_cluster_densities(clusters)

# # """ 找出這群z值最大的點 """
# # # 取得 cluster label = 1 的點群（注意 clusters 是 dict，key 是 label）
# # cluster_points = clusters[1]  # clusters[1] 而不是 clusters[0][1]

# # # 找出 z 值最大的位置（z 是第 3 維 = index 2）
# # max_z_index = np.argmax(cluster_points[:, 2])

# # # 找到對應的點
# # max_z_point = cluster_points[max_z_index]

# # print(f"Cluster 1 中 z 最大的點為: {max_z_point}，z = {max_z_point[2]:.3f}")

# # """找出每個cluster中的點數還有密度"""
# # # 顯示結果
# # # print(clusters[0][1])
# # for i, (label, cluster_points) in enumerate(clusters.items()):
# #     print(f"Cluster {i} (Label {label}): {cluster_points.shape[0]} points, Density: {densities[label]:.2f}")

# # """點雲可視化"""
# # colors = np.array([
# #     [np.random.randint(0, 255) for _ in range(3)] for _ in range(len(np.unique(labels)))
# # ], dtype=int)
# # colors_hex = ['rgb({},{},{})'.format(color[0], color[1], color[2]) for color in colors[labels]]

# # fig = go.Figure(data=[go.Scatter3d(
# #     x=point_cloud_data[:, 0],
# #     y=point_cloud_data[:, 1],
# #     z=point_cloud_data[:, 2],
# #     mode='markers',
# #     marker=dict(
# #         size=3,
# #         color=colors_hex
# #     )
# # )])
# # fig.show()







 


# # # 將點雲根據 y = -0.2 分成兩群
# # group_above = point_cloud_data[point_cloud_data[:, 1] > -0.16]
# # group_below = point_cloud_data[point_cloud_data[:, 1] <= -0.16]

# # print(f"Group ABOVE y = -0.2 有 {group_above.shape[0]} 個點")
# # print(f"Group BELOW y = -0.2 有 {group_below.shape[0]} 個點")

# # fig = go.Figure()

# # # group_above：紅色
# # fig.add_trace(go.Scatter3d(
# #     x=group_above[:, 0],
# #     y=group_above[:, 1],
# #     z=group_above[:, 2],
# #     mode='markers',
# #     marker=dict(size=3, color='red'),
# #     name='y > -0.16'
# # ))

# # # group_below：藍色
# # fig.add_trace(go.Scatter3d(
# #     x=group_below[:, 0],
# #     y=group_below[:, 1],
# #     z=group_below[:, 2],
# #     mode='markers',
# #     marker=dict(size=3, color='blue'),
# #     name='y <= -0.16'
# # ))

# # fig.update_layout(title='Point Cloud Split by y = -0.16')
# # fig.show()



import numpy as np
import pickle
from sklearn.cluster import DBSCAN
import plotly.graph_objects as go

# 讀取人體點雲數據
try:
    with open('./315/08-sync-315-LiDAR-PCDs.pkl', 'rb') as f:
        data = pickle.load(f)
except Exception as e:
    print("An error occurred:", e)

# 定義DBSCAN聚類函數
def cluster_body_parts(point_cloud, eps=0.1, min_samples=10):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(point_cloud)

    # 確定不同簇的數量
    unique_labels = np.unique(labels)
    clusters = {label: point_cloud[labels == label] for label in unique_labels if label != -1}  # -1 為噪聲點
    print(f"Found {len(clusters)} clusters (excluding noise)")
    
    return clusters, labels

# 選一幀點雲
point_cloud_data = data[0]

# DBSCAN 分群
eps = 0.05
min_samples = 9
clusters, labels = cluster_body_parts(point_cloud_data, eps=eps, min_samples=min_samples)

# 找到點數最多的群
largest_cluster_label = max(clusters, key=lambda k: clusters[k].shape[0])
print(f"Largest cluster is label {largest_cluster_label}")

# 產生顏色 (最大群=淡綠色，其他群 & 噪聲=藍色)
colors = {}
for label in np.unique(labels):
    if label == largest_cluster_label:
        colors[label] = 'rgb(0,0,255)'  # 淡綠色
    else:
        colors[label] = 'rgb(255,0,0)'  # 藍色 (包含其他群 + 噪聲)

# 每個點對應顏色
colors_hex = [colors[label] for label in labels]

# 繪圖
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

# 輸出每個 cluster 的大小
for i, (label, cluster_points) in enumerate(clusters.items()):
    print(f"Cluster {i} (Label {label}): {cluster_points.shape[0]} points")
