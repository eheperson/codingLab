#
#
print("*\n*")
def testFcn(param):
    print('ellooo   ' + param)
#
testFcn(param='Co')
#
def squareFcn(x):
    """
    That is a docstring.
    It gives info about function

    """
    return x**2
#
output = squareFcn(4)
print("*\n*")
print(output)
#
#
print("*\n*")
tmpList = [1,2,3,4,5]
print(list(map(squareFcn,tmpList)))
#
#
# Lambda functions
lambda var: var**2
#
print(list(map(lambda x: x**2,tmpList)))
#
print(list(filter(lambda x: x%2 == 0, tmpList)))
#
#
s = 'EllO MotherFuckerS'
#
print(s.lower())
#
print(s.upper())
print(s.split())
#
#
tweet = 'is this end of the beginnign or the beginning of the end?'
tweet.split(' ')[1]
#
d = {'k1': 1, 'k2': 2}
d.keys()
d.items()
d.values()
#
#
tempList = [1,2,3,4,5]
tempList.pop()
#
first = tempList.pop(0)
#
#
#
print ('x' in ['x', 'y', 'z'])
#
#
x = [(1,2), (3,4), (5,6)]
for item in x:
    print(item)
#
for a, b in x:
    print(a)
    print(b)