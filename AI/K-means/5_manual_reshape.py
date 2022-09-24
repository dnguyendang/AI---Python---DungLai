import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy
from PIL import Image

# import picture
# imread function reads the picture into data matrix 
img = plt.imread("a.jpg")

# trasform data into vector in order to train model  
width = img.shape[0]
height = img.shape[1]

# display how to represent data as vector 
# size of picture (341,512,3) - tuple -> 341 line, there are 512 pixel in each line
# each pixel is a 3-dimensional data vector (red, green, blue)
print(img.shape)

#reshape function to transform 
img = img.reshape(width*height,3)

# fit data and train model 
kmeans = KMeans(n_clusters=10).fit(img)

# assign labels to each data pixel, predict labels of data album sơn tùng m-tpby clusters
labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_

# check
print(labels)
print(clusters)

# create a black image 
img2 = numpy.zeros((width,height,3), dtype=numpy.uint8)

# insert pixel to the new image 
index = 0
for i in range(width):
	for j in range(height):
		label_of_pixel = labels[index]
		img2[i][j] = clusters[label_of_pixel]
		index += 1

# save the new image to specified location
im = Image.fromarray(img2)
im.save("a-10.jpg")

# display the new picture 
plt.imshow(img2)
plt.show()
