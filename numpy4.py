import numpy1 as np
#Copy vs view

np1 = np.array([0,1,2,3,4,5])

# #create a view
# np2= np1.view()
#
# print(f'The original NP1 {np1}')
# print(f'The original NP2 {np2}')
#
# np1[0]= 42
#
# print(f'Changed NP1 {np1}')
# print(f'The original NP2 {np2}')
# np2[0] = 45
# print(f'Changed NP1 {np1}')
# print(f'changed NP2 {np2}')

#creata a copy
np2 = np1.copy()
print(f'The original NP1 {np1}')
print(f'The original NP2 {np2}')
np2[0]= 42

print(f'Changed NP1 {np1}')
print(f'The original NP2 {np2}')