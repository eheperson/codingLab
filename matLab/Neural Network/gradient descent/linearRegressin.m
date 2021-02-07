clear all;
close all;
clc;
%%

a = 4;
b = 12;
c = randi([-5,5],1,100);
%c = randperm(100,100);
x = [1:1:100];
%%

% Model for output
y = a*x + b + c;      
% additionally, the noise is added to the signal.
y = awgn(y,10);    

figure
plot(x,y, 'x');

training_number = length(x);


%% model function H(x) definition
%% H(x) = theta_0 + theta_1*x

% initial values for theta
theta = ones(2,1);

%error function
error_func = 1/2*(theta(1,1) + theta(2,1).*x - y).^2;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Learning Parameters

%Learning Rate
alpha = 0.001;
%Max iteraton
iter_max = 20000;
%Iteration Couter
iter = 0;
%epsilon value ( expected minimum error)
epsilon = 1e-10;

%% Training Cycle

% while iter <= iter_max
% or
% mean(error_func) > epsilon
% while iter <= iter_max
while mean(error_func) > epsilon

    temp1 = 0;
    temp0 = 0;
    
    for i = 1 : 1 : training_number
        
        h(i) = theta(1,1) + theta(2,1)*x(i);
      
        temp0 = temp0 + (h(i)-y(i));        % dJ/dtheta0
      
        temp1 = temp1 + (h(i)-y(i))*x(i);   % dJ/dtheta1

    end
    
        tmp1 = theta(1,1) - ((alpha/(2*training_number))*temp0);

        tmp2 = theta(2,1) - ((alpha/(2*training_number))*temp1);

        theta(1,1) = tmp1;

        theta(2,1) = tmp2;
        
    for i = 1 : 1 : training_number
        
        error_func(1,i) = 1/2*(theta(1,1)+theta(2,1)*x(i) - y(i))^2;
        
    end
    
    mean(error_func)
    iter = iter + 1;
        
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Training REsults
theta(2,1)
fprintf(" a : %f \n", theta(2,1));
fprintf(" b : %f \n", theta(1,1));
figure
plot(x,y, 'bx');

hold on
plot(x,(theta(1,1) + theta(2,1)*x), 'r');


