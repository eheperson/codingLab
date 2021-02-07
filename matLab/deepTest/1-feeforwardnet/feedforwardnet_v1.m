clc;
clear all;
close all;
%%

% Load the training data.
[x,t] = simplefit_dataset;

%Construct a feedforward network with one hidden layer of size 10.
net = feedforwardnet(10);

%Train the network net using the training data.
net = train(net,x,t);

%View the trained network.
view(net)

% Estimate the targets using the trained network.
y = net(x);

% Assess the performance of the trained network. The default performance function is mean squared error.

perf = perform(net,y,t)