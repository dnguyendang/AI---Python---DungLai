from sklearn import datasets, neighbors
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

digit = datasets.load_digits() # tep co 1797 data
digit_X = digit.data
digit_y = digit.target

randIndex = np.arange(digit_X.shape[0])
np.random.shuffle(randIndex)

digit_X = digit_X[randIndex]
digit_y = digit_y[randIndex]

X_train, X_test, y_train, y_test = train_test_split(digit_X, digit_y, test_size=360)

knn = neighbors.KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train, y_train)
y_predict = knn.predict(X_test)

accuracy = accuracy_score(y_predict, y_test)
print(accuracy)

#test 1 data
plt.gray()
plt.imshow(X_test[0].reshape(8,8))
print(y_test[0])
print(knn.predict(X_test[0].reshape(1, -1))) # reshape(1,-1) -> dua [1][2] ve dang 
# [[1]
# [2]]
plt.show()

# plt.hist(digit_y)
# plt.show()

# #xem thu anh 
# print(digit_X[100])
# img1 = digit_X[100]
# plt.gray()
# plt.imshow(img1.reshape(8,8))
# plt.show()

