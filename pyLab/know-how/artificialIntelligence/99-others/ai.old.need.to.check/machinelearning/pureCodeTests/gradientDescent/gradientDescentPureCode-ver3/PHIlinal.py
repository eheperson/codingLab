"""
Linear algebra library formachine learning applications 

    matMul(m1,m2)  : accepts 2 2D matrix and returns matrix multiplication of them

    linSpec(startIndex, endIndex, increment) : 
"""
import matplotlib.pyplot as plt
#
##--------------------------------------------------------------------------------------
## Neural Network Builder Functions - Begin
##--------------------------------------------------------------------------------------
#
# Hyperparameters for training algorithm
# That dictionary stores hyperparameters
hyperParams = {'alpha':0,
               'epsilon':0,
               'iterMax':0,
               'N':0}

#Construction Neural Network grid
# that dictionary stores theta and neurons as a matrix
construction ={'X' : [],
               'Y' : [],
               'T' : [],

               'theta' : [],
               'tmp' : [],
               'temp' : [],

               'a1' : [],

               'z2' : [],
               'a2' : []}

def initParams(alpha=0.1, maxIteration=1000, epsilon=1e-3):
    """
    Hyperparameters initialization function 

    initParams(alpha, maxIteration, epsilon=)
    """
    hyperParams['alpha'] = alpha
    hyperParams['epsilon'] = epsilon
    hyperParams['iterMax'] = maxIteration
    #print(hyperParams)

def construct(X, T, layers):
    """
    Builder function for Neural network 

    construct(X, T, layers)
    """
    hyperParams['N'] = len(X)

    l1 = layers[0]
    l2 = layers[1]

    construction['X'] = one2two(X, axis=0)
    construction['T'] = one2two(T, axis=0)
    construction['Y'] = tensor(hyperParams['N'],1)

    construction['theta'] = tensor(l2,l1)
    construction['tmp'] = tensor(l2,l1)
    construction['temp'] = tensor(l2,l1)

    construction['a1'] = tensor(l1,1)


    construction['z2'] = tensor(l2,1)
    construction['a2'] = tensor(l2,1)
    #print(construction['X'])
    #print(construction['T'])
    #print(construction['Y'])
##--------------------------------------------------------------------------------------
## Neural Network Builder Functions - End
##--------------------------------------------------------------------------------------
#
#
##--------------------------------------------------------------------------------------
## Neural Network Training Functions - Begin
##--------------------------------------------------------------------------------------
#
def train():
    """
    Training function for initialized and builded neural network
    that function doesn't take any input argument

    train() function must be called after construct() and initParams() functions

    """
    N = hyperParams['N']
    iterMax = hyperParams['iterMax']
    iteration = 0

    while iterMax > iteration :

        iteration = iteration + 1

        for i in range(N) : 
            construction['a1'] = [construction['X'][i][:]]
            construction['z2'] = matMul(construction['theta'], construction['a1'])
            construction['Y'][i][:] = construction['z2'][0]

            construction['temp'] = matSum(construction['temp'], matSub(construction['z2'], [construction['T'][i][:]]))

        construction['theta'] = matSub(construction['tmp'], matMulNum(construction['temp'], (hyperParams['alpha']/(2*N))))

        if iteration%1000 == 0:
            print("Iteration  : ", iteration)
            print("Mean Error : ", errorFcn(construction['Y'], construction['T']))
#
def errorFcn(m1,m2):
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
##--------------------------------------------------------------------------------------
## Neural Network Training Functions - End
##--------------------------------------------------------------------------------------
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
#
def plotOut(str1, str2):
    m1 = construction['T']
    m2 = construction['Y']
    m1 = flatten(m1)
    m2 = flatten(m2)
    plt.figure(1)
    plt.plot(m1, str1, m2, str2)
    plt.axis('equal')
    plt.show()
##--------------------------------------------------------------------------------------
## Required Linear Algebra Operation Functions for Training - End
##--------------------------------------------------------------------------------------


if __name__ == "main":

    print("incorret use of module")

    m2 = [[1,2,3]]
    m1 = [[4], [5], [6]]
    print(matMul(m1,m2))
    
    c = linSpace(0,10,1)
    d = one2two(c, axis=1)

    print(c)
    print(d)


    a = [[1,2,3], [4,5,6]]
    b = transpose(a)

    print(b)

    a = tensor(1,2)
    print(a)


    a= [[2]]
    b= [[3]]
    print(matMul(a,b))

    a = [[3,4,5]]
    b= [[1,4,6]]

    print(matSub(b,a))

    T = [1.1,3.3,4.1,5.6,12,13,15.2,19.2,21,22.7]

    Y = tensor(len(T),1)

    print(Y)

    X = linSpace(1, 11, 1)
    print(len(X))