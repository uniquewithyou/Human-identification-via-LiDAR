import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import NNConv, global_mean_pool
from torch_geometric.data import Data, Batch
from torch_geometric.loader import DataLoader
from DCT import *
from DBSCAN_limbs import *



class ECCGCNModel(nn.Module):
    def __init__(self, in_channels=20, hidden_channels=64, num_classes=10):
        super(ECCGCNModel, self).__init__()

        # 升維 from 20 → 64
        self.linear_expand = nn.Linear(in_channels, hidden_channels)

        # Edge feature encoder (edge_dim = 20 → edge_weight matrix)
        edge_network1 = nn.Sequential(nn.Linear(20, 64 * 64), nn.ReLU())
        edge_network2 = nn.Sequential(nn.Linear(20, 64 * 64), nn.ReLU())
        edge_network3 = nn.Sequential(nn.Linear(20, 64 * 64), nn.ReLU())

        # ECC Layers
        self.conv1 = NNConv(hidden_channels, hidden_channels, edge_network1, aggr='mean')
        self.conv2 = NNConv(hidden_channels, hidden_channels, edge_network2, aggr='mean')

        # 拼接後再學習的 GCN
        self.fuse_conv = NNConv(hidden_channels * 2, hidden_channels, edge_network3, aggr='mean')

        # classifier
        self.classifier = nn.Sequential(
            nn.Linear(hidden_channels, 64),
            nn.ReLU(),
            nn.Linear(64, num_classes)
        )

    def forward(self, data: Batch):
        x, edge_index, edge_attr, batch = data.x, data.edge_index, data.edge_attr, data.batch

        # 線性升維
        x_high = self.linear_expand(x)  # [N, 64]

        # GCN path
        x1 = F.relu(self.conv1(x_high, edge_index, edge_attr))
        x2 = F.relu(self.conv2(x1, edge_index, edge_attr))

        # 將升維的原始 + 學習後拼接
        x_fused = torch.cat([x_high, x2], dim=1)  # [N, 128]
        x_fused = F.relu(self.fuse_conv(x_fused, edge_index, edge_attr))  # [N, 64]

        # Global pooling → [batch_size, hidden]
        out = global_mean_pool(x_fused, batch)

        return self.classifier(out)



if __name__ == "__main__":
    #parameters
    batch_size = 1
    num_nodes = 5
    num_edges = 4
    DCT_dim = 20
    node_dim = 20
    edge_dim = 20
    num_classes = 10
    # 準備資料
    data_list = final_point_cloud

    model = ECCGCNModel(in_channels=20, hidden_channels=64, num_classes)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()

    # 訓練
    for epoch in range(1, 51):
        model.train()
        total_loss = 0
        for batch in train_loader:  # train_loader 回傳 Batch 型別
            optimizer.zero_grad()
            out = model(batch)  # shape: [batch_size, num_classes]
            loss = criterion(out, batch.y)  # 假設 batch.y 是 [batch_size]
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch:03d} | Loss: {total_loss:.4f}")
