
a = [[2, 3], [10, 7], [33, 22]]

def shape(a):
    b = str(a)

    if len(b) >=3:
        check = 3
    else:
        check = len(a) + 1
    dim = 0
    for i in range(check):
        if b[i] == '[':
            dim +=1

    if dim == 1:
        i = len(a)
        j = 1
        k = 1
        return [i,j,k,dim]
    
    if dim ==2 :
        i = len(a)
        j = len(a[0])
        k = 1
        return [i,j,k,dim]
    
    if dim == 3:
        i = len(a)
        j = len(a[0]) 
        k = len(a[0][0])
        return [i,j,k,dim]

def disp(a, s):
    data = []
    if s[3] == 1:
        for i in range(s[0]):
            #print(a[i])
            data.append(a[i])
    if s[3] == 2:
        for i in range(s[0]):
            for j in range(s[1]):
                #print(a[i][j])
                data.append(a[i][j])
    if s[3] == 3:
        for i in range(s[0]):
            for j in range(s[1]):
                for k in range(s[2]):
                    #print(a[i][j][k])
                    data.append(a[i][j][k])
    return data
    

def get(a=[0], i=1,j=1,k=1):
    s = shape(a)
    d = disp(a,s)

    if s[3] == 1:
        return d[ i  -1 ]

    elif s[3] == 2:
        a = s[0] - (s[0] - i)
        b = s[1] - (s[1] - j)
        print("s[0]:", s[0], "  s[1]:", s[1], "  i:", i, "  j:", j)
        return d[a*b - 1]

    else:
        pass


def set(a=[0], v = 0,  i=1,j=1,k=1):
    s = shape(a)
    d = disp(a,s)

    if s[3] == 1:
        d[ i  - 1] = v

    elif s[3] == 2:
        a = s[0] - (s[0] - i)
        b = s[1] - (s[1] - j)
        print("s[0]:", s[0], "  s[1]:", s[1], "  i:", i, "  j:", j)
        d[a*b - 1] = v

    else:
        pass

print("a : ", a)

s = shape(a)
print("s : ", s)

d = disp(a,s)
print("d : ", d)


i = get(a,3,2)
print("i : ", i)

