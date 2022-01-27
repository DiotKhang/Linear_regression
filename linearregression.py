import numpy as np
import matplotlib.pyplot as plt
arr1 = np.loadtxt('tinhtien.txt', dtype =int,delimiter= ' ')
arr1 = arr1.T
X = np.ones((1,arr1.shape[1]),dtype= int)
X[0,:]= arr1[0,:]
X = X.T
y = np.ones((1,arr1.shape[1]),dtype= int)
y[0,:]= arr1[1,:]
y = y.T
'''
plt.plot(X, y,'ro')
plt.axis([0, 10, 0, 60])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
'''
print('X', X)
print('y', y)
#plt.show()
# Building Xbar 
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)
print("one", one)
print("xbar", Xbar)
# Calculating weights of the fitting line 
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)
# Preparing the fitting line 
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(0, 10, 2)
y0 = w_0 + w_1*x0
# Drawing the fitting line 
plt.plot(X.T, y.T, 'ro')     # data 
plt.plot(x0, y0)               # the fitting line
plt.axis([-10, 10, -10, 60])
plt.xlabel('Quang duong (km)')
plt.ylabel('So tien (VND)')
plt.show()
so_km = input('Nhap so km ')
so_km = int(so_km)
y1= w_1*so_km + w_0
print('Voi quang duong',so_km,'(km) thi so tien la: %.0f (VND)' %(y1) )