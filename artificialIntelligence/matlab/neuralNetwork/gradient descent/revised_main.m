% function [coeff] = gradient_descent(input,output)
%%% This file includes simple gradient descent algortihm to train model function by using derivation of cost function.
clear all;
close all;
clc;

x = [0:1:100];

y = 12 + x.*3;      %% model for the output

y = awgn(y,100);    %% additionally, the noise is added to the signal.

figure
plot(x,y);

training_number = length(x);


%% firstly, model function H(x) should be defined to train the network.
%% H(x) = teta_0 + teta_1*x

%% initial values for teta
teta = ones(2,1);

%% then, cost function should be prepared in order to be appropriate form
%% J(teta) = 1/2m*summation((h(x) - y)^2)
error_func = 1/2*(teta(1,1) + teta(2,1).*x - y).^2;



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% YOUR CODE SHOULD BE HERE

% firstly initial values for the cost function should be assigned.

alpha = 0.001;        % learning rate
iter_max = 20000;
iter = 0;
epsilon = 1e-10;

% while iter <= iter_max
while mean(error_func) > epsilon

    temp1 = 0;
    temp0 = 0;
    
    for i = 1 : 1 : training_number
        
        h(i) = teta(1,1) + teta(2,1)*x(i);
      
        temp0 = temp0 + (h(i)-y(i));        % dJ/dteta0
      
        temp1 = temp1 + (h(i)-y(i))*x(i);   % dJ/dteta1

    end
    
        tmp1 = teta(1,1) - ((alpha/(2*training_number))*temp0);

        tmp2 = teta(2,1) - ((alpha/(2*training_number))*temp1);

        teta(1,1) = tmp1;

        teta(2,1) = tmp2;
        
    for i = 1 : 1 : training_number
        
        error_func(1,i) = 1/2*(teta(1,1)+teta(2,1)*x(i) - y(i))^2;
        
    end
    
    mean(error_func)
    iter = iter + 1;
        
end

%% YOUR CODE SHOULD BE HERE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
teta
figure
plot(x,y, 'rx');

hold on
plot(x,(teta(1,1)+teta(2,1)*x), 'b');

% coeff = 0;


