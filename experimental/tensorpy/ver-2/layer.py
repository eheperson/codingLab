import phTensor 
from multipledispatch import dispatch

class _l(phTensor._t):
    def __init__(self, arr = [], i=1, j=1, k=1, d=1):
        super().__init__(arr = [], i=1, j=1, k=1, d=1)
        self.activationF = ""

    def sigmoid(self):
        pass

    def tansig(self):
        pass

    def purelin(self):
        pass


def nnLayerArchitect(layerArr):
    tmp = []

    for i in range(len(layerArr)):
        tmp.append(phTensor.tensor(1, layerArr[i]))
        
    return tmp

if __name__ == "__main__":

    inputL = 2
    outputL = 1
    hidden1 = 5
    hidden2 = 5
    hidden3 = 5

    layers = [inputL, hidden1, hidden2, hidden3, outputL]

    l = nnLayerArchitect(layers)

    for i in range(len(layers)):
        print("---------------------------------")
        print("{}. layer :".format(i+1))
        l[i].disp()
    print("---------------------------------")
