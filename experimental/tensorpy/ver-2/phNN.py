#
import phTensor as t
import layer as l
import weight as w

class nn(object):
    def __init__(self, X, T, hiddenLayers):
        #
        self.X = []  #input matrix of inputs    
        self.T = []  #input matrix of targets
        self.N = 0  #num of inputs
        #
        self.L = 0 #num of layers( input and output layers are included also)
        self.layersN = []  # array(list) of neuron numbers for each layer in nn architecture
        self.layerVector = [] # sequence of layers in nn archtecture
        self.weightVector = [] # sequence of weights in nn architecture
        #
        self.Y = [] #input matrix of outputs
        self.e = [] #input matrix of errors for each input
        #
        self.alpha = 0  #learning rate
        self.epsilon = 0 #min epsilon   
        self.maxIteration = 0   #maximum iteration
        self.error = 0  # error of network
        #
        self.errFcn = "" # error function name
        self.trainFcn = "" #train function name
        self.optimizer = "" #optimizer function name
        #
        #
        self.__architect(X, T, hiddenLayers)
    #
    #
    def __architect(self, x, t, layerArr):
        #---------------------------------------------------------------------------
        ## Declaring neuron numbers for input and output layers -  Begin
        inputL = 0
        outputL = 0
        #
        if str(x[0]) ==1 :
            inputL = 1
        else:
            inputL = len(x[0])
        #    
        if str(t[0]) ==1 :
            outputL = 1
        else:
            outputL = len(t[0])
        ## Declaring neuron numbers for input and output layers -  End
        #---------------------------------------------------------------------------
        #
        #---------------------------------------------------------------------------
        ## Declaring neuron numbers for hidden layers -  Begin
        #
        #checking if layer input of network is array or number
        if isinstance(layerArr ,list): 
            #continue from here if layer input of network is an array
            tmpLayer =[0 for x in range(len(layerArr))]
            for i in range(len(layerArr)):
                tmpLayer[i] = layerArr[i]
            #
            tmpLayer.append(outputL)
            tmpLayer.insert(0, inputL)
        #
        else :
            #continue from here if layer input of network is not an array
            tmpLayer =[layerArr]
            #
            tmpLayer.append(outputL)
            tmpLayer.insert(0,inputL)
        #
        ## Declaring neuron numbers for hidden layers -  End
        #---------------------------------------------------------------------------
        #
        #---------------------------------------------------------------------------
        ## Building Architecture -  Begin
        #
        self.X = x
        self.T = t
        self.layersN = tmpLayer
        self.L = len(tmpLayer)
        #
        self. layerVector =  l.nnLayerArchitect(self.layersN)
        self.weightVector = w.nnWeightArchitect(self.layersN)
        #
        ## Building Architecture -  End
        #---------------------------------------------------------------------------

    def architecture(self):
        for i in range(self.L):
            print("----------------------------------------")
            #
            if i==0 : 
                print("{}. layer           <input layer><{}x1>:".format(i,self.layersN[i]))
            elif i==self.L-1:
                print("{}. layer           <output layer><{}x1>:".format(i,self.layersN[i]))
            else :
                print("{}. layer      <{}. hidden layer, <{}x1>:".format(i, i+1, self.layersN[i]))
            
            self.layerVector[i].disp()
            #
            if(i != self.L-1):
                print("----------------------------------------")
                print("Weight Matrix                <{}x{}>:".format(i, i+1))
                self.weightVector[i].disp()
        print("----------------------------------------")


    def train(self):
        pass


if __name__ == "__main__":
    inputRow = 20
    inputColumn =3 

    targetRow = 20
    targetColumn = 2


    x =  [[0 for i in range(inputColumn)] for j in range(inputRow)]
    y =  [[0 for i in range(targetColumn)] for j in range(targetRow)]
    c = nn(x,y,[30, 20, 10])
    
    c.architecture()

