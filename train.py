#!/usr/bin/env python3
"""
Author: Aleksa Zatezalo
Description: Uses pytorch to train nueral net on chess games.
Date: July 2025
"""

from torch.utils.data import Dataset
import numpy as np
import torch
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
    
chess_dataset = ChessValueDataset()

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

    def forward(self, x):
        x = F.relu(nn.Conv2d(5, 10, kernel_size=3))
        x = F.relu(nn.Conv2d(10, 10, kernel_size=3))
        x = F.relu(nn.Conv2d(10, 10, kernel_size=3))
        x = F.max_pool2d(x)

        # 4x4
        x = F.relu(nn.Conv2d(20, 20, kernel_size=3))
        x = F.relu(nn.Conv2d(20, 20, kernel_size=3))
        x = F.relu(nn.Conv2d(20, 20, kernel_size=3))
        x = F.max_pool2d(x)

        # 2x2
        x = F.relu(nn.Conv2d(40, 40, kernel_size=3))
        x = F.relu(nn.Conv2d(40, 40, kernel_size=3))
        x = F.relu(nn.Conv2d(40, 40, kernel_size=3))
        x = F.max_pool2d(x)

        # 1x1
        x = x.view(-1, 1)

        x = F.relu(F.max_pool2d(self.conv1(x)), 2)
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fe1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

