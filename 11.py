import numpy as np

def step(x):
    return 1 if x >= 0 else 0

class Perceptron:
    def __init__(self):
        self.w = np.zeros(2)
        self.b = 0

    def train(self, X, y, lr=0.1, epochs=10):
        for _ in range(epochs):
            for xi, target in zip(X, y):
                pred = step(np.dot(xi, self.w) + self.b)
                error = target - pred
                self.w += lr * error * xi
                self.b += lr * error

    def predict(self, X):
        return [step(np.dot(x, self.w) + self.b) for x in X]

# Inputs
X = np.array([[0,0],[0,1],[1,0],[1,1]])

# AND Gate
y_and = np.array([0,0,0,1])
p1 = Perceptron()
p1.train(X, y_and)
print("AND:", p1.predict(X))

# OR Gate
y_or = np.array([0,1,1,1])
p2 = Perceptron()
p2.train(X, y_or)
print("OR :", p2.predict(X))