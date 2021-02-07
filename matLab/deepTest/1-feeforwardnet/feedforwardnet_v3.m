clc;
clear all;
close all;
%%

% Load The training data
e = bodyfatInputs;
t = bodyfatTargets;
% or
% load bodyfat_dataset

%Construct a feedforward network with one hidden layer of size 10.
net = feedforwardnet(20);

%Train the network net using the training data.
[net,tr] = train(net,bodyfatInputs,bodyfatTargets);



trainFcn = 'trainlm';  % Levenberg-Marquardt backpropagation.

% Create a Fitting Network
hiddenLayerSize = 10;
net = fitnet(hiddenLayerSize,trainFcn);

% Choose Input and Output Pre/Post-Processing Functions
% For a list of all processing functions type: help nnprocess
net.input.processFcns = {'removeconstantrows','mapminmax'};
net.output.processFcns = {'removeconstantrows','mapminmax'};

%% Setup Division of Data for Training, Validation, Testing

net.divideFcn = 'dividerand';  % Divide data randomly
net.divideMode = 'sample';  % Divide up every sample

net.divideParam.trainRatio = 70/100;
net.divideParam.valRatio = 15/100;
net.divideParam.testRatio = 15/100;

%% Choose a Performance Function
net.performFcn = 'mse';  % Mean Squared Error

%% Choose Plot Functions

net.plotFcns = {'plotperform','plottrainstate','ploterrhist', ...
    'plotregression', 'plotfit'};

%% Train the Network
[net,tr] = train(net,x,t);

%% Test the Network
y = net(x);
e = gsubtract(t,y);
performance = perform(net,t,y)

%% Recalculate Training, Validation and Test Performance
trainTargets = t .* tr.trainMask{1};
valTargets = t .* tr.valMask{1};
testTargets = t .* tr.testMask{1};
trainPerformance = perform(net,trainTargets,y)
valPerformance = perform(net,valTargets,y)
testPerformance = perform(net,testTargets,y)

%% Network Diagram and Plots

%network structure
view(net) 

% Plots
figure, plotperform(tr)
figure, plottrainstate(tr)
figure, ploterrhist(e)
figure, plotregression(t,y)
figure, plotfit(net,x,t)

