clc;
clear;
clear all;
 %%
 %%
 
a = csvread('winequality-red.csv',1,0);

[x, t] = chemical_dataset;
trainFcn = 'trainlm';  % Levenberg-Marquardt backpropagation.

% Create a Fitting Network
hiddenLayerSize = 10;
net = feedforwardnet(hiddenLayerSize,trainFcn);

% Setup Division of Data for Training, Validation, Testing
net.divideParam.trainRatio = 70/100;
net.divideParam.valRatio = 15/100;
net.divideParam.testRatio = 15/100;


net.trainParam.epochs = 1000;
net.trainparam.goal   = 0;
net.trainParam.max_fail = 6;
net.trainParam.min_grad = 1e-7;
net.trainParam.mu = 0.001;
net.trainParam.mu_dec = 0.1;
net.trainParam.mu_inc = 10;
net.trainParam.mu_max  = 1e10;
net.trainParam.show = 25;
net.trainParam.showCommandLine = false;
net.trainParam.showWindow = true;
net.trainParam.time = Inf;

[x, t] = bodyfat_dataset;

[net,tr] = train(net,x,t);

% Test the Network
y = net(x);
e = gsubtract(t,y);
performance = perform(net,t,y)


view(net)


