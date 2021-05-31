import phTensor as t
import numpy as np

"""
data = [[2, 3], [10, 7], [33, 22]]

tensor = t.tensor(data)

print(" i          : ", tensor.i)
print(" j          : ", tensor.j)
print(" k          : ", tensor.k)
print(" dimension  : ", tensor.d)
print(" data       : ", tensor.data)
print(" matrix     : ", tensor.mat)

tensor.disp()



tensor2 = t.tensor(5,20)

tensor2.disp()

print(" i          : ", tensor2.i)
print(" j          : ", tensor2.j)
print(" k          : ", tensor2.k)
print(" dimension  : ", tensor2.d)
print(" data       : ", tensor2.data)
print(" matrix     : ", tensor2.mat)


layers = [3, 5, 5, 5, 5, 5, 2]
tmp = []
for i in range(len(layers) - 1):
    tmp.append(t.tensor(layers[i], layers[i+1]))

l = []

for i in range(10):
    l.append(t.tensor(3,3))

print(tmp)
"""




import layer as L
import weight as W

inputL = 2
outputL = 1
hidden1 = 5
hidden2 = 5
hidden3 = 5

layers = [inputL, hidden1, hidden2, hidden3, outputL]

print(len(layers))
input = t.tensor(1,2)

input.disp()