clc;
close all;
clear all;
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Binary Classification Example For Healt of Plants
%   
%   Dataset Definition : 
%       X0 : Bias
%       X1 : pH
%       X2 : Temperature (Centigrade)
%       X3 : Moisture Percentage
%       Y  : 1 if healtly, 0 is not healty
%
%   For Healty Plants : 
%       pH should be between 5,5 and 8,5
%       Temperature should be between 24 and 34 centigrades
%       Moinsture percentage should be between %45 and %55
%
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%

%% Create Dataset

M = 200; %Mumber of Samples

% bias = 1;
% phMin = 0;
% phMax = 0;
% tempMin = 0;
% tempMax = 0;
% moisMin = 0;
% moisMax = 0;

X0healthy = ones(1,M/2);
X1healthy = randi([54,85],1,M/2)/10;
X2healthy = randi([239,351],1,M/2)/10;
X3healthy = randi([450,550],1,M/2)/10;
Yhealthy = ones(1,M/2);

X0unhealthy = ones(1,M/2);
X1unhealthy = randi([10,140],1,M/2)/10;
X2unhealthy = randi([10,500],1,M/2)/10;
X3unhealthy = randi([10,900],1,M/2)/10;
Yunhealthy = zeros(1,M/2);


X0 = [X0healthy X0unhealthy]';
X1 = [X1healthy X1unhealthy]';
X2 = [X2healthy X2unhealthy]';
X3 = [X3healthy X3unhealthy]';

X = [X0 mat2gray(X1) mat2gray(X2) mat2gray(X3)];
Y =  [Yhealthy Yunhealthy]';

figure
scatter3(X1healthy, X2healthy, X3healthy, 'rx' )
hold on
scatter3(X1unhealthy, X2unhealthy, X3unhealthy, 'bo' )

%% Model
% firstly, model function H(x) should be defined to train the network.
% H(x) = 1/(1 + exp(teta_0*x0 + teta_1*x1 + teta_2*x2))

theta = randi([-20 100],3,1);

%% Error Function 

error_func = -1./(M).*(Y.*log(1./(1 + exp(-(theta(1,1).*X(:,1) + theta(2,1).*X(:,2) + theta(3,1).*(X(:,3) + X(:,4) )))))...
                                  + (1 - Y).*log(1 - 1./(1 + exp(-(theta(1,1).*X(:,1) + theta(2,1).*X(:,2) + theta(3,1).*(X(:,3) + X(:,4) ) )))));        

                              
learning_rate = 0.001;
epsilon = 1e-5*ones(length(X0),1);

iteration = 0;
iterMax = 50000;

%% Learning Algorithm
while (sum(abs(error_func(:,1)) > epsilon ) ~= 0) && iterMax > iteration
    
    iteration = iteration + 1;
    
    internal_error_func = error_func; % That line is foranimation
    
    for i = 1:1:M
       h(i) = 1./(1 + exp(-(theta(1,1).*X(i,1) + theta(2,1).*X(i,2) + theta(3,1).*(X(i,3) + X(i,4) ))));
       
       temp1 = theta(1,1) - learning_rate*( h(i) - Y(i,1))*X(i,1);
       
       temp2 = theta(2,1) - learning_rate*( h(i) - Y(i,1))*X(i,2);
       
       temp3 = theta(3,1) - learning_rate*( h(i) - Y(i,1))*X(i,3);
   
        
       theta(1,1) = temp1;
       theta(2,1) = temp2;
       theta(3,1) = temp3;
       
       
       error_func(i, 1) = -1/(M)*(Y(i,1)*log(1/(1 + exp(-(theta(1,1)*X(i,1) + theta(2,1)*X(i,2) + theta(3,1).*(X(i,3) + X(i,4) )))))...
                                  + (1 - Y(i,1))*log(1 - 1/(1 + exp(-(theta(1,1)*X(i,1) + theta(2,1)*X(i,2) + theta(3,1).*(X(i,3) + X(i,4) )))))); 
    
       if isnan(error_func(i,1)) 
           error_func(i,1) = 0;
       end
       
       if isinf(error_func(i,1))
           error_func(i,1) = 10e+3;
       end
    
    end
    
    mean(error_func) %% Print out error mean to console
    
end


%% Plot Output

h_teta_x = 1./(1 + exp(-(theta(1,1).*X(:,1) + theta(2,1).*X(:,2) + theta(3,1).*(X(:,3) + X(:,4) ))));

figure
plot([1:1:M],Y, 'x');
figure
plot([1:1:M],h_teta_x, 'x');





% end