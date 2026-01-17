import numpy as np
#Slicing Number arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])

#Return 2,3,4,5
print(np1[1:5])
#return form something till the end of the array
print(np1[3:])

#return negative slices
print(np1[-3:-1])

#slices with steps
print(np1[1:5])
print(np1[1:5:2])

#steps on entire aray
print(np1[::2])
print(np1[::3])

#slice a 2d array
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#pull out a single item
print(np2[1,-1])

#slice a 2d array 2,3
print(np2[0:1,1:3])

#slicefrom both rows 2,3 and 7,8
print(np2[0:2,1:3])
#all on numpy docs