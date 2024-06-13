import math
import numpy as np

class Perceptron(object):
    def __init__(self, tau=0.01, epochs=50, gamma=1.0):
        self.tau = tau
        self.epochs = epochs
        self.gamma = gamma

    def train(self, X, y):
        print('X.shape[0]: ', 'X.shape[1]: ', X.shape[0], X.shape[1])
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.epochs):
            errors = 0
            for xi, target in zip(X, y):
                if target != self.predict(xi):
                    error = (target -self.predict(xi))
                    self.w_[1:] += error * xi
                    self.w_[0] += error
                    errors += int(error != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self,X):
        return  np.where(self.net_input(X) >= 0.0,1,-1)
