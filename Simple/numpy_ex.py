import numpy as np
x=np.array(list(range(1,11)),dtype=int)
x_1= x.reshape(2,5)
y=np.array(list(range(1,11)),dtype=int)
y_1= y.reshape(2,5)
y_1T=y.reshape(5,2)
print ('Reshaped x',x_1)
print('Reshaped y',y_1)

print('------------------------------------')
print ('sum', x_1+y_1)

print('alternate way to sum', np.add(x_1,y_1))

print('Multiply', x_1*y_1)

print('way 2 to multiply',np.multiply(x_1,y_1))

print (' dot mulitplication',x_1.dot(y_1T))