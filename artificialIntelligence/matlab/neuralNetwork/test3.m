clc;
clear all;
close all;

net = network;

%% Number of inputs and layers
net.numInputs = 2 ;
%number of input source
% I
net.numlayers = 3 ;
%number of layers
% L
%% Bias connections
net.biasConnect(1) = 1;
net.biasConnect(3) = 1;
% net.biasConnect(i) > bias connection oof the i th layer
% net.biasConnect = [1;0;1]
% L-by-1

%% Input and layer weight connections
net.inputConnect(1,1) = 1;
net.inputConnect(1,2) = 1;
net.inputConnect(2,2) = 1;
% net.inputConnect(i,j) > input-weight connection going to i th layer from the j th input 
% net.inputConnect = [1 0; 1 1; 0 0]
%L-by-I

net.layerConnect(3,1) = 1;
net.layerConnect(3,2) = 1;
net.layerConnect(3,3) = 1;
% net.layerConnect(i,j) > 1ayer-weight connection going to the i th layer from the j th layer
% net.layerConnect = [0 0 0; 0 0 0; 1 1 1]
% L-by-L

%% Output connections

net.outputConnect(2) = 1;
net.outputConnect(3) = 1;
%net.outputConnect(i) > output conncet from the i th layer to the external world
% net.outputConnect = [ 0 1 1]
% 1-by-L


net.inputs{1}.exampleInput = [0 10 5; 0 3 10]
net.inputs{1}.processFcns = {'removeconstantrows', 'mapminmax'}

net.inputs{2}.size = 5

net.layers{1}.size = 4
net.layers{1}.transferFcn = 'tansig'
net.layers{1}.initFcn = 'initnw'

net.layers{2}.size = 3
net.layers{2}.transferFcn = 'logsig'
net.layers{2}.initFcn = 'initnw'

net.layers{3}.initFcn = 'initnw'
view(net)