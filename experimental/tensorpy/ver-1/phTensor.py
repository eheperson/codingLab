from multipledispatch import dispatch
import numpy as np
import matplotlib.pyplot as plt
import twoD as d2


class _t(object):

    def __init__(self,arr = [], i=1, j=1, k=1, d=1):

        self.i = i
        self.j = j
        self.k = k

        self.d = d

        self.data = []
        self.mat = []

        self.shape(arr)
        self.__vec2mat()



    def shape(self, arr):
        
        strArr = str(arr)
        if len(strArr) >=3:
            check = 3
        else:
            check = len(arr) + 1
        dim = 0
        for i in range(check):
            if strArr[i] == '[':
                dim +=1

        if dim == 1:
            i = len(arr)
            j = 1
            k = 1
            self.i = i
            self.j = j
            self.k = k
        
        if dim ==2 :
            i = len(arr)
            j = len(arr[0])
            k = 1
            self.i = i
            self.j = j
            self.k = k
        
        if dim == 3:
            i = len(arr)
            j = len(arr[0]) 
            k = len(arr[0][0])
            self.i = i
            self.j = j
            self.k = k
        
        self.d = dim

        if dim == 1:
            for x in range(i):
                #print(a[i])
                self.data.append(arr[x])
        if dim == 2:
            for x in range(i):
                for y in range(j):
                    #print(a[i][j])
                    self.data.append(arr[x][y])
        if dim == 3:
            for x in range(i):
                for y in range(j):
                    for z in range(k):
                        #print(a[i][j][k])
                        self.data.append(arr[x][y][z])

    def disp(self):
        if self.d == 1:
            self.__disp1D()
        elif self.d == 2:
            self.__disp2D()
        elif self.d == 3:
            self.__disp3D()

    def __vec2mat(self):
        if self.d == 1:
            self.__vec2mat1D()
        elif self.d == 2:
            self.__vec2mat2D()
        elif self.d == 3:
            self.__vec2mat3D()

    def __disp1D(self):
        for x in range(self.i):
            print(self.data[x], end=" ")

    def __disp2D(self):
        index = 0
        for _ in range(self.i):
            print()
            for _ in range(self.j):
                print(" {0} ".format( self.data[index]), end=" ")
                index += 1

    def __disp3D(self):
        pass

    def __vec2mat1D(self):
        self.mat = self.data
        pass

    def __vec2mat2D(self):
        self.mat = [ [0 for _ in range(self.j) ] for _ in range(self.i)]
        index = 0
        for x in range(self.i):
            for y in range(self.j):
                self.mat[x][y] = self.data[index]
                index += 1

    def __vec2mat3D(self):
        pass


@dispatch(int)
def tensor(i) :
    tmp = []
    for x in range (i):
        tmp.append(0)

    return _t(tmp)

@dispatch(int,int)
def tensor(i, j):
    tmp = [[]]
    zeros = [[0 for _ in range(i)] for _ in range(j)]

    return _t(zeros)

@dispatch(int,int, int)
def tensor(i, j, k) :
    pass 

@dispatch(list)
def tensor(arr) :
    return _t(arr)
 









