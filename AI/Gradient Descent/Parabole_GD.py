import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

#create function cost 
def cost(x):
	m = A.shape[0]
	return 0.5/m * np.linalg.norm(A.dot(x)-b, 2)**2

#create function gradient
def grad(x):
	m = A.shape[0]
	return 1/m * A.T.dot(A.dot(x) - b)

#create function gradient descent 
def gradient_descent(x_init, learning_rate, iteration):
	x_list = [x_init]
	for i in range(iteration):
		x_new = x_list[-1] - learning_rate * grad(x_list[-1])
		if np.linalg.norm(grad(x)) / len(x_new) < 1e-12:
		 	break
		x_list.append(x_new)
	return x_list

#random data
b = np.array([[2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]]).T
A = np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]]).T

#draw data 
fig1 = plt.figure("GD for Line Regression")
ax = plt.axes(xlim = (-10, 40), ylim = (-10, 60))
plt.plot(A,b, 'ro')

#create vector 1 and vector A square
ones = np.ones((A.shape[0],1), dtype = np.int8)
A_square = np.array([A[:,0]**2]).T

#combine matrix A 
A = np.concatenate((A_square, A, ones), axis = 1)
# print(A)

##LINEAR REGRESSION
#draw parabole by linear regression 
x = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(b)

x0 = np.linspace(2,40, 1000)
y0_ln = x0*x0 * x[0][0] + x0 * x[1][0] + x[2][0]

plt.plot( x0, y0_ln, color = "black")
# plt.show() 

##GRADIENT DESCENT
#random x[[a],[b],[c]]
# ham can tim  global optimal la ham phuc tap, x la vector con A la ma tran vi vay co nhieu local optimal. 
# x_init = np.array([[-10.1],[5.1],[-20.1]])
# x_init = np.array([[-6.1],[0.1],[-82.1]])
# x_init = np.array([[-10.1],[10.1],[-10.1]])
x_init = np.array([[-2.1],[5.1],[-2.1]])
y0_init = x0 * x0 * x_init[0][0] + x0 * x_init[1][0] + x_init[2][0]
plt.plot(x0, y0_init, color = "red", alpha = 0.7)

#run gradient descent
learning_rate = 1e-6
iteration = 150
x_list = gradient_descent(x_init, learning_rate, iteration)
print(len(x_list))
for i in range(len(x_list)):
	y0_list = x0 * x0 * x_list[i][0][0] + x0 * x_list[i][1][0] + x_list[i][2][0]
	plt.plot(x0, y0_list, color = "yellow", alpha = 0.3)

#animation 
line , = ax.plot([],[], color = "blue")
def update(i):
	y0_gd = x0 * x0 * x_list[i][0][0] + x0 * x_list[i][1][0] + x_list[i][2][0]
	line.set_data(x0, y0_gd)
	return line, 
#ham lay nguyen do thi, lay ham va bien iters(so lan ve hay chinh la i), interval speed animation, blit lam muot hinh  
iters = np.arange(1, len(x_list), 1)
# print(iters)
line_anim = animation.FuncAnimation(fig1, update, iters, interval=50, blit=True)

plt.show()

#check iteration and learning rate
cost_list = []
iter_list = []
for i in range(len(x_list)):
	iter_list.append(i)
	cost_list.append(cost(x_list[i]))

plt.plot(iter_list, cost_list)
plt.xlabel("iteration")
plt.ylabel("Value of cost")

plt.show()



