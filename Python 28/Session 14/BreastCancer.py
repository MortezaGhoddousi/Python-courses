from sklearn.datasets import load_breast_cancer
import numpy as np


def hardlim(n):
    if n >= 0:
        return 1
    else:
        return 0

data = load_breast_cancer()

P = data['data']
T = data['target']

print(P.shape, T.shape)

W = np.zeros([1, 569])
b = np.zeros([1, 30])

for i in range(1000):
    n = np.matmul(W, P) + b
    a = 

