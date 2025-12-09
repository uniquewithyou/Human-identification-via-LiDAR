import numpy as np
import pickle
from sklearn.cluster import DBSCAN
from scipy.spatial import ConvexHull
import plotly.graph_objects as go
from DBSCAN import *











""" 選出軀幹跟頭部的點雲 """


# 選出被標為 noise（label = -1）的點
noise_points = point_cloud_data[labels == -1]

# 檢查是否有 noise 點
if noise_points.shape[0] > 0:
    # 繪製 noise 點
    fig_noise = go.Figure(data=[go.Scatter3d(
        x=noise_points[:, 0],
        y=noise_points[:, 1],
        z=noise_points[:, 2],
        mode='markers',
        marker=dict(
            size=3,
            color='black'
        )
    )])
    fig_noise.update_layout(title='DBSCAN Noise Points (Label = -1)')
    fig_noise.show()
else:
    print("沒有找到任何 noise 點（label = -1）")


# 將點雲根據 y = -0.2 分成兩群
group_left = noise_points[noise_points[:, 1] > -0.16]
group_right = noise_points[noise_points[:, 1] <= -0.16]
group_head = noise_points[noise_points[:, 2] >= 0.6]
group_left_hand = noise_points[(noise_points[:, 2] < -0.6) & (noise_points[:, 2] > -0.1) & (noise_points[:, 1] > -0.16)]





fig = go.Figure()

# group_above：紅色
fig.add_trace(go.Scatter3d(
    x=group_left[:, 0],
    y=group_left[:, 1],
    z=group_left[:, 2],
    mode='markers',
    marker=dict(size=3, color='red'),
    name='y > -0.16'
))

# group_below：藍色
fig.add_trace(go.Scatter3d(
    x=group_right[:, 0],
    y=group_right[:, 1],
    z=group_right[:, 2],
    mode='markers',
    marker=dict(size=3, color='blue'),
    name='y <= -0.16'
))



# # group_above：紅色
# fig.add_trace(go.Scatter3d(
#     x=group_head[:, 0],
#     y=group_head[:, 1],
#     z=group_head[:, 2],
#     mode='markers',
#     marker=dict(size=3, color='red'),
#     name='y > -0.16'
# ))

# # group_below：藍色
# fig.add_trace(go.Scatter3d(
#     x=group_head[:, 0],
#     y=group_head[:, 1],
#     z=group_head[:, 2],
#     mode='markers',
#     marker=dict(size=3, color='blue'),
#     name='y <= -0.16'
# ))

fig.update_layout(title='Point Cloud Split by y = -0.16')
fig.show()