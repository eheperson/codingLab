import numpy as np

# Create array 
x = np.array([1,2,3,4,5])

print(type(x))

xZeros = np.zeros((4,4))
print(xZeros)

xOnes = np.ones((3,3))
print(xOnes)

print(np.ones((4,4))*5)

aranged = np.arange(10,50,5)
print(aranged)

aranged = np.arange(0,2,0.2)
print(aranged)

linSpace = np.linspace(0,4,12)
print(linSpace)

rand = np.random.rand(3,4)
print(rand)

randNormal = np.random.randn(2,5)
print(randNormal)

randInt= np.random.randint(1,50,15)
print(randInt)

unitMatrice = np.eye(13)
print(unitMatrice)

y = np.arange(24)
print(y)

z = y.reshape(6,4)
print(z)

t = y.reshape(2,3,4)
print(t)

yMax = y.max()
print(yMax)

yMin = y.min()
print(yMin)

yArgMax = y.argmax()
print(yArgMax)

yArgMin = y.argmin()
print(yArgMin)

a = np.arange(60)
a.shape = [2, -1, 5]
print(a.shape)

##########################################################################


oneD = np.arange(10)
print(oneD)

oneD_square = oneD**2
print(oneD_square)

print(oneD[3])
print(oneD[3:6])

oneD[4] = 10
print(oneD)
print(oneD_square)

for i in oneD:
    print(i*5)

###########################################################################
# indexleme
d = np.random.rand(16)
multiD = d.reshape(4,4)

print(d)
print(multiD)

#diziyi eskihaline getirme
print(multiD.ravel)
print(d)
print(d[0:2:1])
print(d[:3])

for satir in multiD.flat:
    print(satir)

for satir in np.ndenumerate(multiD):
    print(satir)

xa = np.array([[1,2],[2,3]])
xb = np.array([[6,7]])
xab0 = np.concatenate((xa,xb), axis=0)
xab1 = np.concatenate((xa,xb.T), axis=1)

print(xa)
print(xb)
print(xab0)
print(xab1)

xc = np.array([2,3])
xd = np.array([5,6])

xe = np.vstack((xc, xd))

xf = np.hstack((xc,xd))

print(xc)
print(xd)
print(xe)
print(xf)

###########################################
#islemler

arr1 = np.array([20,30,40,50])
arr2 = np.arange(4)

print(arr1)
print(arr2)

print(arr1*arr2)

print(arr1**3)

print(arr1>30)

arr1 += 40
print(arr1)

arr3 = np.random.rand(15)
print(arr3)

print(arr3.sum())

arr4 = np.arange(20).reshape(4,5)
print(arr4)

print(arr4.sum(axis=0))
print(arr4.sum(axis=1))

print(arr4.min(axis=0))
print(arr4.min(axis=1))

print(arr4.max(axis=0))
print(arr4.max(axis=1))

#cumulative sum
print(arr4.cumsum(axis=0))
print(arr4.cumsum(axis=1))

# istatistics
arr5 = np.random.randint(30)
print(np.mean(arr5))
print(np.median(arr5))
print(np.std(arr5))
print(np.var(arr5))

# copy array
arr5_copy = np.copy(arr5)

arr6 = np.array(['ankara', 'istanbul','istanbul', 'bursa', 'hatay','bursa','izmir','mersin', 'hatay'])
print(np.unique(arr6))