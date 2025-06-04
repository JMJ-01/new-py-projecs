import numpy as np
My_list= (1,2,3,4,5,6,7,8,9,10,11,12)

#array = np.array(My_list,dtype=int)

#array2= array.reshape(1,-1)
#print(array2)
#print(array2.shape)
#print (array2.ndim)

#My_list2=(23,24,25,26)
#My_list3=(33,34,35,36)
#My_list4=(44,45,46,47)
#mul_arr = np.array([My_list2,My_list3,My_list4])
#print (mul_arr)
#mul_arr.reshape(2, -1)
a=np.arange(60)
print(a)

b=a.reshape (5,3,2,2)
print ('array b is..')
print (b)
print ('Dimension of b ', b.ndim)
print ('Computes overall sum (axis none)',np.sum(b))
print ('Computes sum of each column',np.sum(b, axis=0))
print ('Computes sum of each row',np.sum(b, axis=1))
print ('Computes sum of ? (1)',np.sum(b, axis=2))
print ('Computes sum of ? (2)',np.sum(b, axis=3))

print ( 'Block one',b[0])