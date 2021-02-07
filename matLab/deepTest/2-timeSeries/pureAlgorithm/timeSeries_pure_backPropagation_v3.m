clear all;
close all;
clc;

%% Prepare Dataset
[X,T] = valve_dataset;
X = cell2mat(X);
T = cell2mat(T);

% Convert input matrix to Argmax model
delay = 1;
[xs, ts, xi] = prep(X,T,delay);
N = length(xs);
x0 = ones (N,1);            % bias input              
x1 = xs(1,:)';              % for first input
x2 = xs(2,:)';              % for second input
                
% normalize data
x = [x0 mat2gray(x1) mat2gray(x2)];  
t = mat2gray(ts');

%% error parameters
errorArr = ones(N,1);
error = sum(errorArr);

%% Network PArameters                                                       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
layer1 = 3;                                                                 %Size of the layer 1 (nput layer) 
layer2 = 10;                                                                %Size of the layer 2 (hidden layer 1)
layer3 = 10;                                                                 %Size of the layer 3 (hidden layer 2)
layer4 = 1;                                                                 %Size of the layer 4 (output layer)
%% Weigh Matrices                                                           %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
w1 = randi([5 10],layer1,layer2)./100;                                      % w1 weight is between layer 1 and layer 2
w2 = randi([5 10],layer2,layer3)./100;                                      % w2 weight is between layer 2 and layer 3
w3 = randi([5 10],layer3,layer4)./100;                                      % w3 weight is between layer 3 and layer 4
%% Bias values for each layer                                               %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
b1 = 0;                                                                     %Bias value of the layer 1               
b2 = 1;                                                                     %Bias value of the layer 2
b3 = 1;                                                                     %Bias value of the layer 3
b4 = 1;                                                                     %Bias value of the layer 4
%% Z matrices                                                               %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
z1 = zeros(1,layer1);
z2 = zeros(1,layer2);
z3 = zeros(1,layer3);
z4 = zeros(layer3,layer4);
%% H matrices for activation function output                                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
h1 = zeros(1,layer1);                                                       %activation function output of the layer1( it is equal to the input x size)
h2 = zeros(1,layer2);                                                       %activation function output of the layer2
h3 = zeros(1,layer3);                                                       %activation function output of the layer2
h4 = zeros(1,layer4);                                                       %activation function output of the layer2( it is equal to the output t size)
%% d matricies for the backpropagation gradient errors for each layer unit  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% there is  no  d1 for layer 1                                              %we do not need calculate gradient error for the input layer
d2 = zeros(1,layer2);                                                       %backpropagation error matrices for layer 2
d3 = zeros(1,layer3);                                                       %backpropagation error matrices for layer 3
d4 = zeros(1,layer4);                                                       %backpropagation error matrices for layer 4
%% D matricies for the partial derivation for eash weight matrix            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
D1 = zeros(layer1, layer2);                                                 %partial derivation of weight1 matrix
D2 = zeros(layer2, layer3);                                                 %partial derivation of weight2 matrix
D3 = zeros(layer3, layer4);                                                 %partial derivation of weight3 matrix

%% Error parameters to the error value calculation                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
errorArr = ones(N,1);
error = sum(errorArr);
%% Learning parameters to optimizenetwork learning performance              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
epsilon = 0.001;
learning_rate = 1;
alpha = 0.0001;
%% TRAINING SECTION

while error>epsilon
    
    D1 = zeros(layer1, layer2);
    D2 = zeros(layer2, layer3);
    D3 = zeros(layer3, layer4);
    for i = 1:N
       
       % % % Forward Pass
       
       h1 = x(i,:);
       
       z2 = h1*w1 + b2;
       h2 = tansig(z2);
       
       z3 = h2*w2 +b3;
       h3 = tansig(z3);
       
       z4 = h3*w3 + b4;
       h4 = tansig(z4);
       
       % % % Backward Pass
       
       d4 = h4 - t(i,:); 
       d3 = (w3').*(d4.*h3.*(1-h3));
       d2 = (d3*w2').*h2.*(1-h2);
       
       % Partial Derivations
       D3 = D3 + h3'*d4;
       D2 = D2 + h2'*d3;
       D1 = D1 + h1'*d2;
       
       tempw1 = w1 - alpha*D1;
       tempw2 = w2 - alpha*D2;
       tempw3 = w3 - alpha*D3;
       
       % % % Collecting error values for each individual data in dataset
       errorArr(i,1) = sum(1/2*(t(i,:) - h4).^2);
    end
    
    % % % Calculationg error of the network
    error = sum(errorArr)/N
    
    % Updating Weight matrices
    w1 = tempw1;
    w2 = tempw2;
    w3 = tempw3;
end
