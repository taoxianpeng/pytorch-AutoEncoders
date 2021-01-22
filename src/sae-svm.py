from torchvision import datasets
from torchvision.datasets import ImageFolder
import torch
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def load_datasets(path):
    datasets = ImageFolder(path)
    
def load_modal():
    modal = torch.load('D:\GitHub\pytorch-AutoEncoders\src\SEAutoEncoder_modal.pt')
    return modal
def clas_svm():
    pass
def clas_pso_svm():
    pass
def clas_spso_svm():
    pass
def plot():
    pass

if __name__ == "__main__":
    antoEncoder = load_modal()
    print(antoEncoder)

