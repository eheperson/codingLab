import matplotlib.pyplot as plt
#
#
class phNN:
    def __init__(self, X=[], T=[],):
        self.X = X
        self.T = T
        self.Y = []

        self.alpha = 0
        self.epsilon = 0
        self.iterMax = 0
        self.N = len(X) 

        self.construction ={'X' : [],
               'Y' : [],
               'T' : [],

               'theta' : [],
               'tmp' : [],
               'temp' : [],

               'a1' : [],

               'z2' : [],
               'a2' : []}


    def initParams(self, alpha = 0.01, epsilon = 0.0001, iterMax = 1000):
        self.alpha = alpha
        self.epsilon = epsilon
        self.iterMax = iterMax

    def construct(self, layers):
        l1 = layers[0]
        l2 = layers[1]

        self.construction['X'] = one2two(self.X, axis=0)
        self.construction['T'] = one2two(self.T, axis=0)
        self.construction['Y'] = tensor(self.N,1)

        self.construction['theta'] = tensor(l2,l1)
        self.construction['tmp'] = tensor(l2,l1)
        self.construction['temp'] = tensor(l2,l1)

        self.construction['a1'] = tensor(l1,1)


        self.construction['z2'] = tensor(l2,1)
        self.construction['a2'] = tensor(l2,1)
        print(self.construction['X'])
    def plotOut(self, str1, str2):
        m1 = self.construction['T']
        m2 = self.construction['Y']
        m1 = flatten(m1)
        m2 = flatten(m2)
        plt.figure(1)
        plt.plot(m1, str1, m2, str2)
        plt.axis('equal')
        plt.show()

    def train(self):
        """
        Training function for initialized and builded neural network
        that function doesn't take any input argument

        train() function must be called after construct() and initParams() functions

        """
        N = self.N
        iterMax = self.iterMax
        iteration = 0

        while iterMax > iteration :

            iteration = iteration + 1

            for i in range(N) : 
                self.construction['a1'] = [self.construction['X'][i][:]]
                self.construction['z2'] = matMul(self.construction['theta'], self.construction['a1'])
                self.construction['Y'][i][:] = self.construction['z2'][0]

                self.construction['temp'] = matSum(self.construction['temp'], matSub(self.construction['z2'], [self.construction['T'][i][:]]))

            self.construction['theta'] = matSub(self.construction['tmp'], matMulNum(self.construction['temp'], (self.alpha/(2*N))))

            if iteration%1000 == 0:
                print("Iteration  : ", iteration)
                print("Mean Error : ", phNN.errorFcn(self.construction['Y'], self.construction['T']))

    @classmethod
    def errorFcn(cls,m1,m2):
        if len(str(m1)) == 1:
            r1 = 1
        else:
            r1 = len(m1)

        if len(str(m1[0])) == 1:
            c1 = 1
        else:
            c1 = len(m1[0])
        
        if len(str(m2)) == 1:
            r2 = 1
        else:
            r2 = len(m2)

        if len(str(m2[0])) ==1:
            c2 = 1
        else:
            c2 = len(m2[0])


        if r1 != r2 or c1 != c2:
            print("Matrix dimension must be agree")
            return -1

        error = 0.0

        for i in range(r1):
            for j in range(c1):
                error = error + (m1[i][j] - m2[i][j])**2

        error = error/(r1*c1*2)
        return error

#
#
##--------------------------------------------------------------------------------------
## Required Linear Algebra Operation Functions for Training - Begin
##--------------------------------------------------------------------------------------
def matMul(m1, m2):
    """
    Matrix Multiplication Function for 2D Matrices
    """

    if len(str(m1)) == 1:
        r1 = 1
    else:
        r1 = len(m1)

    if len(str(m1[0])) == 1:
        c1 = 1
    else:
        c1 = len(m1[0])
    
    if len(str(m2)) == 1:
        r2 = 1
    else:
        r2 = len(m2)

    if len(str(m2[0])) ==1:
        c2 = 1
    else:
        c2 = len(m2[0])

    result = [[0 for x in range(c2)] for y in range(r1)] 
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] +=  float(m1[i][k]*m2[k][j])
    return result
#
def matSub(m1, m2):
    """
    Matrix substraction operator for 2D Matrices
    """

    if len(str(m1)) == 1:
        r1 = 1
    else:
        r1 = len(m1)

    if len(str(m1[0])) == 1:
        c1 = 1
    else:
        c1 = len(m1[0])
    
    if len(str(m2)) == 1:
        r2 = 1
    else:
        r2 = len(m2)

    if len(str(m2[0])) ==1:
        c2 = 1
    else:
        c2 = len(m2[0])


    if r1 != r2 or c1 != c2:
        print("Matrix dimension must be agree")
        return -1

    result = [[0 for x in range(c1)] for y in range(r1)]

    for i in range(r1):
        for j in range(c1):
            result[i][j] = float(m1[i][j] - m2[i][j])
    return result
#
def matSum(m1, m2):
    """
    Matrix substraction operator for 2D Matrices
    """

    if len(str(m1)) == 1:
        r1 = 1
    else:
        r1 = len(m1)

    if len(str(m1[0])) == 1:
        c1 = 1
    else:
        c1 = len(m1[0])
    
    if len(str(m2)) == 1:
        r2 = 1
    else:
        r2 = len(m2)

    if len(str(m2[0])) ==1:
        c2 = 1
    else:
        c2 = len(m2[0])


    if r1 != r2 or c1 != c2:
        print("Matrix dimension must be agree")
        return -1

    result = [[0 for x in range(c1)] for y in range(r1)]

    for i in range(r1):
        for j in range(c1):
            result[i][j] = float(m1[i][j] + m2[i][j])
    return result
#
def matMulNum(m, num):
    """
    Matrix multiplication with zero-order tensor (number)
    """
    if len(str(m)) == 1:
        r = 1
    else:
        r = len(m)

    if len(str(m[0])) == 1:
        c = 1
    else:
        c = len(m[0])

    result = [[0 for x in range(c)] for y in range(r)]
    for i in range(r):
        for j in range(c):
            result[i][j] = m[i][j]*float(num)

    return result
#
def linSpace(first, last, inc):
    """
    range of array between 'first' and 'end' by increment of 'inc'
    """
    array = []
    element = first

    size = last - first

    for i in range(size):
        array.append(float(element))
        element = element + inc
        
        if element > last:
            break

    return array
#
def one2two(array, axis = 0):
    """
    convert 1D arrays to 2D arrays according to axis
    """
    new = []

    if axis == 0:
        for i in range(len(array)):
            new.append([float(array[i])])

    elif axis == 1:
        for i in range(len(array)):
            new.append(float(array[i]))
        new = [new]
    else:
        print(" 'axis' must be '0' or '1'")
        return -1

    return new
#
def transpose(arr):
    """
    Transpose of 2D matrix
    """
    r = len(arr)

    if len(str(arr[0])) == 1:
        c = 1
    else:
        c = len(arr[0])

    result = [[0 for x in range(r)] for y in range(c)] 
    
    for i in range(r):
        # iterate through rows
        for j in range(c):
            # iterate through columns
            result[j][i] = arr[i][j]

    return result
#
def tensor(r, c):
    """
    That function returns 2D tensors
    """
    result = [[float(0) for x in range(c)] for y in range(r)] 
    return result
#
#
def flatten(m1):
    if len(str(m1)) == 1:
        r1 = 1
    else:
        r1 = len(m1)

    if len(str(m1[0])) == 1:
        c1 = 1
    else:
        c1 = len(m1[0])
    
    result = [float(0) for x in range(c1*r1)] 
    
    ii = 0
    for i in range(r1):
        for j in range(c1):
            result[ii] = m1[i][j]
            ii = ii+1
    return result
##--------------------------------------------------------------------------------------
## Required Linear Algebra Operation Functions for Training - End
##--------------------------------------------------------------------------------------
