close all;
clear all;
clc;
clear;


%%% CLASSIFICATION Problem
%% logistic regression application

number_of_data = 100;

mu1 = [2,3];
sigma1 = [1,1.5;1.5,3];
rng default  % For reproducibility
rnd_number_1 = mvnrnd(mu1,sigma1,number_of_data);

mu2 = [8,10];
sigma2 = [1,1.5;1.5,3];
rng default  % For reproducibility
rnd_number_2 = mvnrnd(mu2,sigma2,number_of_data);

figure
plot(rnd_number_1(:,1),rnd_number_1(:,2),'+')
hold on
plot(rnd_number_2(:,1),rnd_number_2(:,2),'o')

X0 = ones(2*length(rnd_number_1(:,1)),1);

X1 = [rnd_number_1(:,1);rnd_number_2(:,1)];
X2 = [rnd_number_1(:,2);rnd_number_2(:,2)];

Y_general = [zeros(length(rnd_number_1(:,1)),1);ones(length(rnd_number_1(:,1)),1)];

X_general_unnormalized = [X0 X1 X2];
X_general = [X0 mat2gray(X1) mat2gray(X2)];


training_number = length(X0);


%% firstly, model function H(x) should be defined to train the network.
%% H(x) = 1/(1 + exp(teta_0*x0 + teta_1*x1 + teta_2*x2))

teta = randi([-20 100],3,1);

%% then, cost function should be prepared in order to be appropriate form
%% J(teta) = 1/m*summation((h(x) - y)^2)
%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Your code should be in here.
hx = 1./(1 + exp(-(teta(1,1).*X_general(:,1) + teta(2,1).*X_general(:,2) + teta(3,1).*X_general(:,3))));
error_func= 1/training_number*((hx(:,1) - Y_general(:,1)).^2);
%error_func= 1/training_number*(Y_general(:,1).*log(h_teta_x(:,1))+(1-Y_general(:,1)).*log(1-h_teta_x(:,1)));
alpha=0.0001;

epsilon=0.0020;

iter=0;
maxiter=1000000;
while  iter<maxiter % mean(error_func)>epsilon
    iter=iter+1;
    
    temp0=0;
    temp1=0;
    temp2=0;

    for i=1:1:training_number
    
       h(i,1) = 1/(1 + exp(-(teta(1,1)*X_general(i,1) + teta(2,1)*X_general(i,2) + teta(3,1)*X_general(i,3))));
    
        temp0=temp0+(h(i,1)- Y_general(i,1))*X_general(i,1);
    
       temp1=temp1+(h(i,1) - Y_general(i,1))*X_general(i,2);
       
       temp2=temp2+(h(i,1) - Y_general(i,1))*X_general(i,3);
    
    
    end

        tmp0=teta(1,1)-1/training_number*alpha*temp0;

        tmp1=teta(2,1)-1/training_number*alpha*temp1;

        tmp2=teta(3,1)-1/training_number*alpha*temp2;


        teta(1,1)=tmp0;

        teta(2,1)=tmp1;

        teta(3,1)=tmp2;


        
    %h_teta_x = 1./(1 + exp(-(teta(1,1).*X_general(:,1) + teta(2,1).*X_general(:,2) + teta(3,1).*X_general(:,3))));
    for i=1:i:training_number
        
        error_func(i,1)= (1/training_number)*((h(i,1) - Y_general(i,1))^2);
        %error_func(i,1)= 1/training_number*(Y_general(i,1)*log(h(i,1))+(1-Y_general(i,1))*log(1-h(i,1)))
    end
  mean(error_func)
end


%% Your code should be in here.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




h_teta_x = 1./(1 + exp(-(teta(1,1).*X_general(:,1) + teta(2,1).*X_general(:,2) + teta(3,1).*X_general(:,3))));

figure
plot([1:1:training_number],Y_general);
figure
plot([1:1:training_number],h_teta_x);


% for plotting boundary section in graph
% figure
% plot(rnd_number_1(:,1),rnd_number_1(:,2),'+')
% hold on
% plot(rnd_number_2(:,1),rnd_number_2(:,2),'o')
% 
% x1_boundary = abs(teta(1,1)/(teta(2,1)))*max(X_general_unnormalized(:,2));
% x2_boundary = abs(teta(1,1)/(teta(3,1)))*max(X_general_unnormalized(:,3));
% plot([0 x1_boundary*3],[x2_boundary*3 0]);

%plotDecisionBoundary(teta, X_general, Y_general)


coeff = 0;



% end