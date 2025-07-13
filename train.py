#!/usr/bin/env python3
"""
Author: Aleksa Zatezalo
Description: Uses pytorch to train nueral net on chess games.
Date: July 2025
"""

from torch.utils.data import Dataset
import numpy as np
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F

class ChessValueDataset(Dataset):
    def __init__(self):
        dat = np.load("processed/dataset.npz")
        self.X = dat['arr_0']
        self.Y = dat['arr_1']
        print(self.X.shape, self.Y.shape)

    def __len__(self):
        return self.X.shape[0]
    
    def __getitem__(self, idx):
        return{self.X[idx], self.Y[idx]}

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.a1 = F.relu(nn.Conv2d(5, 16, kernel_size=3))
        self.a2 = F.relu(nn.Conv2d(16, 16, kernel_size=3))
        self.a3 = F.relu(nn.Conv2d(16, 32, kernel_size=3))

        self.b1 = F.relu(nn.Conv2d(32, 32, kernel_size=3))
        self.b2 = F.relu(nn.Conv2d(32, 32, kernel_size=3))
        self.b3 = F.relu(nn.Conv2d(32, 64, kernel_size=3))

        self.c1 = F.relu(nn.Conv2d(64, 64, kernel_size=3))
        self.c2 = F.relu(nn.Conv2d(64, 64, kernel_size=3))
        self.c3 = F.relu(nn.Conv2d(64, 128, kernel_size=3))

        self.d1 = F.relu(nn.Conv2d(128, 128, kernel_size=3))
        self.d2 = F.relu(nn.Conv2d(128, 128, kernel_size=3))
        self.d3 = F.relu(nn.Conv2d(128, 128, kernel_size=3))

        self.lost = nn.Linear(128, 1)

    def forward(self, x):
        x = F.relu(self.a1(x))
        x = F.relu(self.a2(x))
        x = F.relu(self.a3(x))
        x = F.max_pool2d(x, 2)

        # 4x4
        x = F.relu(self.b1)
        x = F.relu(self.b2)
        x = F.relu(self.b3)
        x = F.max_pool2d(x)

        # 2x2
        x = F.relu(self.c1)
        x = F.relu(self.c2)
        x = F.relu(self.c3)
        x = F.max_pool2d(x)

        # 1x128
        x = F.relu(self.d1)
        x = F.relu(self.d2)
        x = F.relu(self.d3)

        x = x.view(-1, 128)
        x = self.last(x)

        # value output
        return F.log_softmax(x)

chess_dataset = ChessValueDataset()
model = Net()
optimizer = optim.Adam(model.parameters())

device = "cpu"

model.train()
for batch_idx, (data, target) in enumerate(train_loader):
    data = data.unsqueeze_(-1)
    print(data.shape)
    print(target.shape)
    data, target = data.to(device), target.to(device)
    optimizer.zero_grad()
    output = model(data)
    loss = F.all_loss(output, target)
    loss.backward()
    optimizer.step()
