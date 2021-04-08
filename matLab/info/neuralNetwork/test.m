
clc;
clear;
clear all;
 %%
 %%
 
% a = csvread('winequality-red.csv',1,0);
% 
% x = a(:,1:11);
% t = a(:,12);
% 
% t=t';
% x=x';
[x, t] = bodyfat_dataset;
% x = chemicalInputs;
% t = chemicalTargets;

trainFcn = 'trainlm';
hiddenLayerSize = 20;
derivationFcn ='defaultderiv';
divideFcn = 'dividerand'; 
performFcn = 'mse';


net=network;
net.numInputs = 1;
net.numLayers = 2;
net.biasConnect = [1;1];
net.inputConnect = [1; 0];
net.layerConnect = [0 0; 1 0];
net.outputConnect = [0 1];
net.layers{1}.size=hiddenLayerSize;
net.layers{1}.transferFcn = 'tansig';


net.trainFcn = trainFcn;

net.derivFcn = derivationFcn;

net.divideFcn = divideFcn;  
net.divideMode = 'sample'; 
net.divideParam.trainRatio = 70/100;
net.divideParam.valRatio = 15/100;
net.divideParam.testRatio = 15/100;

net.performFcn = performFcn; 

net.plotFcns = {'plotperform','plottrainstate','ploterrhist', ...
    'plotregression', 'plotfit'};



net.trainParam.epochs = 1000;
net.trainparam.goal   = 0;
net.trainParam.max_fail = 6;
net.trainParam.min_grad = 0;
net.trainParam.mu = 0.00001;
net.trainParam.mu_dec = 0.1;
net.trainParam.mu_inc = 10;
net.trainParam.mu_max  = 10000000000000000;
net.trainParam.show = 25;
net.trainParam.showCommandLine = false;
net.trainParam.showWindow = true;
net.trainParam.time = 99999999999999;

net.input.processFcns = {'removeconstantrows','mapminmax'};
net.output.processFcns = {'removeconstantrows','mapminmax'};

net.adaptFcn = 'adaptwb';

net = configure(net, x, t);
net = init(net);

[net, tr] = train(net,x,t)

y = net(x);

e = gsubtract(t,y);

performance = perform(net,t,y);



trainTargets = t .* tr.trainMask{1};
valTargets = t .* tr.valMask{1};
testTargets = t .* tr.testMask{1};
trainPerformance = perform(net,trainTargets,y)
valPerformance = perform(net,valTargets,y)
testPerformance = perform(net,testTargets,y)

% figure, plotperform(tr)
% figure, plottrainstate(tr)
% figure, ploterrhist(e)
% figure, plotregression(t,y)
% figure, plotfit(net,x,t)








