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
        print("loaded", self.X.shape, self.Y.shape)

    def __len__(self):
        return self.X.shape[0]
    
    def __getitem__(self, idx):
        return{'X': self.X[idx], 'Y':self.Y[idx]}

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

    def forward(self, x):
        x = F.relu(nn.Conv2d(16, 16, kernel_size=3))
        x = F.relu(nn.Conv2d(16, 16, kernel_size=3))
        x = F.relu(nn.Conv2d(16, 31, kernel_size=3))
        x = F.max_pool2d(x)

        # 4x4
        x = F.relu(nn.Conv2d(32, 32, kernel_size=3))
        x = F.relu(nn.Conv2d(32, 32, kernel_size=3))
        x = F.relu(nn.Conv2d(32, 64, kernel_size=3))
        x = F.max_pool2d(x)

        # 2x2
        x = F.relu(nn.Conv2d(64, 64, kernel_size=3))
        x = F.relu(nn.Conv2d(64, 64, kernel_size=3))
        x = F.relu(nn.Conv2d(64, 64, kernel_size=3))
        x = F.max_pool2d(x)

        # 1x64
        x = x.view(-1, 64)
        x = nn.Linear(64, 1)(x)

        # value output
        return F.log_softmax(x)

chess_dataset = ChessValueDataset()
model = Net()
optimizer = optim.Adam(model.parameters())
