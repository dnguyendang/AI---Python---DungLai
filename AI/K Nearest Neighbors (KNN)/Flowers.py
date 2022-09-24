from sklearn import datasets
import numpy as np
import math
import operator 

def calculate_distance(p1, p2): # 2 vector co cung chieu nhau 
	dimension = len(p1) # dimension la chieu 
	distance = 0

	for i in range(dimension):
		distance += (p1[i]-p2[i])**2

	return math.sqrt(distance) 

# def get_k_neighbors(training_X, label_y, point, k):
# 	distances = []
# 	neighbors = [] # danh sach k cai gan nhat dua theo khoang cach cta tim duoc 
# 	#cho nay phuc tap, vi can sap xep khoang cach nhung dam bao luc lay ra dung label tuong ung
# 	#tuc la sort 1 list theo 1 list khac 
# 	for i in range(len(training_X)):
# 		distance = calculate_distance(training_X[i], point)
# 		distances.append((distance, label_y[i])) #tuple 

# 	distances.sort(key=operator.itemgetter(0)) #sort by distance
# 	#if itemgetter(1) -> sort by label_y

# 	for i in range(k):
# 		neighbors.append(distances[i][1])

# 	return neighbors

# ham get_k_neighbors nhung khong dung thu vien, tim k thang nho nhat nhung khong dung thu vien 
def get_k_neighbors(training_X, label_y, point, k):
	distances = []
	neighbors = []

	#calculate distance from point to each data point 
	for i in range(len(training_X)):
		distance = calculate_distance(training_X[i], point)
		distances.append(distance)

	#position of k smallest distances
	index = []

	#get k closet points 
	while len(neighbors) < k:
		i = 0
		min_distance = 9999
		min_index = 0
		while i < len(distances):
			#skip the nearest points that hace counted
			if i in index:
				i += 1
				continue
			#update smallest distance and index 
			if distances[i] <= min_distance:
				min_distance = distances[i]
				min_index = i	

			i += 1	
		
		#add min index so we skip it in the next iteration 
		index.append(min_index)
		neighbors.append(label_y[min_index])	

	return neighbors

def highest_votes(labels):
	labels_count = [0,0,0]	# index cua labels_count chinh la label cua y luon 

	for label in labels:
		labels_count[label] += 1 

	max_count = max(labels_count)

	return labels_count.index(max_count)

def predict(training_X, label_y, point, k):
	neighbors_labels = get_k_neighbors(training_X, label_y, point, k)

	return highest_votes(neighbors_labels)

def accuracy(predicts, groundTruth): # groundTruth la thu mk da biet r nhung khong dung ma chi de kiem tra 
	total = len(predicts)
	correct_count = 0

	for i in range(total):
		if predicts[i] == groundTruth[i]:
			correct_count += 1

	accuracy = correct_count / total

	return accuracy

iris = datasets.load_iris()
# include 150 data 
iris_x = iris.data #data (sepal length, sepal width, petal length, petal width)
iris_y = iris.target #label
#kieu du lieu numpy array

#shuffle by index when using numpy array 
# a = np.array([1,2,3])
# print(a)
# index = np.array([2,0,1])
# a = a[index]
# print(a)

#tao 1 array 150 index tu 0->149 
randIndex = np.arange(iris_x.shape[0])
#shuffle index
np.random.shuffle(randIndex) # ngau nhien theo kieu can bang 
#shuffle data
iris_x = iris_x[randIndex]
iris_y = iris_y[randIndex]
#np.ones(150) -> tao ra 150 so 1 
#np.zeros(150) -> tao ra 150 so 0

#chia data thanh training set 100 data and test set 50 data 
X_train = iris_x[:100,:]
X_test = iris_x[100:,:]
y_train = iris_y[:100]
y_test = iris_y[100:]

k = 5
y_predict = []
for p in X_test:
	label = predict(X_train, y_train, p, k)
	y_predict.append(label)

accuracy = accuracy(y_predict, y_test)

print(accuracy)