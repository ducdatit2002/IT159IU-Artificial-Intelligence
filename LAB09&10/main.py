from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Perceptron

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title('Iris flower dataset (training set)')
plt.show()

# Filter dataset to only include setosa and versicolor samples
X_sv = X_train[(y_train == 0) | (y_train == 1)]
y_sv = y_train[(y_train == 0) | (y_train == 1)]

# Convert labels to binary (0 for setosa, 1 for versicolor)
y_sv = np.where(y_sv == 0, -1, 1)

perceptron = Perceptron(random_state=0)
perceptron.fit(X_sv[:, :2], y_sv)
y_pred = perceptron.predict(X_test[:, :2])
y_pred_train = perceptron.predict(X_sv[:, :2])
train_error = np.mean(y_pred_train != y_sv)
print(f'Training error: {train_error:.2%}')

# Test error
test_error = np.mean(y_pred != np.where(y_test == 0, -1, 1))
print(f'Test error: {test_error:.2%}')