#
import phTensor as t

class nn(object):
    def __init__(self, X, T, layers):
        
        self.X = X                          #input matrix of inputs    
        self.T = T  #input matrix of targets
        self.Y = [] #input matrix of outputs
        self.e = [] #input matrix of errors for each input
        
        self.alpha = 0  #learning rate
        self.epsilon = 0 #min epsilon   
        self.maxIteration = 0   #maximum iteration
        self.error = 0  # error of network

        self.N = 0  #num of inputs

        self.inputL = 0 #input layer neuron number
        self.outputL = 0 #output layer neuron number
        self.layers = [] #list of all layer's neurons
        self.hiddenL=[] #neuron numbers of hidden layers
        self.errFcn = "" # error function name
        self.trainFcn = "" #train function name

        self.construction = []
        self.activationsL = []  #activations for each layer
        

        self.__setParams(X, T, layers)
        self.construct()

    def __setParams(self, x, t, layer):

        if isinstance(layer ,list):
            tmpLayer =[0 for x in range(len(layer))]
            for i in range(len(layer)):
                tmpLayer[i] = layer[i]
            
            if str(x[0]) ==1 :
                self.inputL = 1
            else:
                self.inputL = len(x[0])
            
            if str(t[0]) ==1 :
                self.outputL = 1
            else:
                self.outputL = len(t[0])



            tmpLayer.append(self.outputL)
            tmpLayer.insert(0, self.inputL)

            self.layers = tmpLayer

            tmpActivations =[0 for x in range(len(layer) + 1)]

            self.activationsL = tmpActivations


        else :
            tmpLayer =[layer]

            if str(x[0]) ==1 :
                self.inputL = 1
            else:
                self.inputL = len(x[0])
            
            if str(t[0]) ==1 :
                self.outputL = 1
            else:
                self.outputL = len(t[0])

            tmpLayer.append(self.outputL)
            tmpLayer.insert(0, self.inputL)

            self.layers = tmpLayer

            tmpActivations =[0, 0]

            self.activationsL = tmpActivations

    def construct(self):

        tmp = []
        for i in range(len(self.layers) - 1):
            tmp.append(t.tensor(self.layers[i], self.layers[i+1]))
        
        self.construction = tmp

    def train(self):
        pass


inputRow = 20
inputColumn =3 

targetRow = 20
targetColumn = 2


x =  [[0 for i in range(inputColumn)] for j in range(inputRow)]
y =  [[0 for i in range(targetColumn)] for j in range(targetRow)]
c = nn(x,y,[5, 5, 5])
print(c.construction[1].mat)

