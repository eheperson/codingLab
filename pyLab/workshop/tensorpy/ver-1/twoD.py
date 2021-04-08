
def mult(m1, m2):
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
def sub(m1, m2):
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
def sum(m1, m2):
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
def mulN(m, num):
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
#def tensor(r, c):
#    """
#    That function returns 2D tensors
#    """
#    result = [[float(0) for x in range(c)] for y in range(r)] 
#    return result
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