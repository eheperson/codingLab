% function [coeff] = gradient_descent(input,output)
%%% This file includes simple gradient descent algortihm to train model function by using derivation of cost function.

x = [0:1:20];

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


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% YOUR CODE SHOULD BE HERE

% firstly initial values for the cost function should be assigned.














%% YOUR CODE SHOULD BE HERE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


teta

figure
plot(x,y);
hold on
plot(x,(teta(1,1)+teta(2,1)*x))

coeff = 0;

% end