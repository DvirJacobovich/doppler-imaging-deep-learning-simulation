
"""
Dvir Jacobovich Doppler mapping deep leaning simulation 
John Howell lab 2024
"""

import time
import numpy as np
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim
import torchvision.utils as vutils
import matplotlib.pyplot as plt
import scipy


class DopplerDataSet(torch.utils.data.Dataset):
    'Characterizes a dataset for PyTorch'

    def __init__(self, list_IDs, labels):
        'Initialization'
        self.labels = labels
        self.list_IDs = list_IDs

    def __len__(self):
        'Denotes the total number of samples'
        return len(self.list_IDs)

    def __getitem__(self, index):
        'Generates one sample of data'
        # Select sample
        ID = self.list_IDs[index]

        # Load data and get label
        # X = torch.load('data/' + ID + '.pt')
        X = ID
        # y = self.labels[ID]
        y = self.labels[index]
        return X, y
