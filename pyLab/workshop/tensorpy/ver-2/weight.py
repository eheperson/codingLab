import phTensor 

class _w(phTensor._t):
    def __init__(self, arr = [], i=1, j=1, k=1, d=1):
        super().__init__(arr = [], i=1, j=1, k=1, d=1)


def nnWeightArchitect(weightArr):
    tmp = []

    for i in range(len(weightArr) - 1):
        tmp.append(phTensor.tensor(weightArr[i], weightArr[i+1]))
        
    return tmp

if __name__ == "__main__":

    inputL = 2
    hidden1 = 5
    hidden2 = 5
    hidden3 = 5
    outputL = 1

    layers = [inputL, hidden1, hidden2, hidden3, outputL]

    w = nnWeightArchitect(layers)

    for i in range(len(layers)):
        print("---------------------------------")
        print("W_{}{}   :".format(i, i+1))
        w[i].disp()
    print("---------------------------------")
