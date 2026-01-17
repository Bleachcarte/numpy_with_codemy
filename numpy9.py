import numpy as np

#filtering Numpy arrays with Boolean index lists

np1 = np.array([1,2,3,4,5,6,7,8,9,10])
# x = [True,True,False,False,False,False,False,False,False,False]
#
# print(np1)
# print(np1[x])


# filtered = []
# for thing in np1:
#     if thing%2 == 0:
#         filtered.append(True)
#     else:
#         filtered.append(False)
#
# print(np1)
# print(filtered)
# print(np1[filtered])`

#shortcut
filtered = np1%2 == 1
print(np1)
print(filtered)
print(np1[filtered])