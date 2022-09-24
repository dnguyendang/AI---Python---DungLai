import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans
import numpy

# import picture
# ham imread se doc anh thanh matran du lieu
img = plt.imread("b.jpg")

#xem cach bieu dien du lieu cua anh duoi dang vector
print(img.shape)
# kich thuoc anh (341,512, 3) - tuple -> 341 dong, moi dong gom 512 pixel, moi pixel la 1 vector du lieu 3 chieu (Red, Green, Blue)

#transform du lieu thanh dang vector (1 hang) de traning model 
height = img.shape[0]
width = img.shape[1]

img = img.reshape(height*width, 3) 
# ham reshape de transform 

#sau khi transform thi chon k he so phan loai va fit de training model 
#chon K tu ban phim 
K = int(input())

kmeans = KMeans(n_clusters = K).fit(img)

#gan nhan cho tung pixel du lieu, du doan labels cua data theo clusters 
labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_
#check 
print(labels)
print(clusters)

#create new picture: 2 way 
#C1 tao kich thuong anh sau do them tung pixel 
#C2 thay tung pixel vao vector pixel (..., 3) -> sau do chuyen vector do ve dang ma tran anh anh dau ( .., ... , 3)

#C2
img2 = numpy.zeros_like(img)
#create img2 has the size like img ( img now is the vector has in form of (... , 3) ) but the whole pixel is only white or black 

#them tung pixel cho vector img2
for i in range(len(img2)):
	img2[i] = clusters[labels[i]]

#transform vecotr (..., 3) ve dang anh (..., ..., 3)
img2 = img2.reshape(height, width, 3)

print(img2.shape)
# hien thi anh 
imgplot = plt.imshow(img2)
plt.show()

#C1 
img3 = numpy.zeros((height, width, 3), dtype = numpy.uint8)
#create black image
index = 0
#insert pixel to the new image
for i in range(height):
	for j in range(width):
		img3[i][j] = clusters[labels[index]] 
		index += 1

plt.imshow(img3)
plt.show()

