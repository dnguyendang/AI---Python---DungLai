import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 

#random data
b = [2,5,7,9,11,16,19,23,22,29,35,37,40,46,42,39,31,30,28,20,15,10,6]
A = [2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

#Visualize data
plt.plot(A, b, 'ro')

#change row vector to column vector
A = np.array([A]).T
b = np.array([b]).T

#create vector 1 
ones = np.ones((A.shape[0],1), dtype=np.int8)

# print(A[:,0])    			dau : la lay tu dau den cuoi 

#craete A square
A_square = np.array([A[:,0]**2]).T
# print(x_square)

#combine vector A square , vector A and vector 1
A = np.concatenate((A_square, A, ones), axis = 1)
# print(A)

#use fomular 
# x = (A^TA)^-1A^T b
x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)
# print (x)

#test data to draw parabole 

x0 = np.linspace(1,25, 10000) 
# x0 la vector chua cac diem trai tu 1 den 25 va co 10k diem 
y0 = x0*x0 * x[0][0] + x0 * x[1][0] + x[2][0]


#test new data 
x_test = 12
y_test = x_test * x_test * x[0][0] + x_test * x[1][0] + x[2][0]
print(y_test)

plt.plot(x0, y0)
plt.show()