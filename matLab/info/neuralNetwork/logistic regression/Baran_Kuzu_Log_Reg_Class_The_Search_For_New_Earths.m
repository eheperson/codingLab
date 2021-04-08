close all;
clear all;
clc;
clear;

filename='exoTrain.csv';
keplertrain = csvread(filename,1,1,[1 1 100 100]);

%keplerdata1 = [keplertrain(:,1) keplertrain(:,2)];
%keplerdata2 = [keplertrain(:,3) keplertrain(:,4)];

X_kepler=keplertrain;

training_number=100;
Y_kepler=zeros(100,1);


for i=1:1:training_number
    
   if i <= 73
       Y_kepler(i,1) = 1;
   end
 
   if i>37
       Y_kepler(i,1) = 0;
   end 
end

X0 = ones(training_number,1);
X1 = X_kepler(:,1);
X2 = X_kepler(:,2);

X_general = [X0 X1 X2];
Y_general = Y_kepler;


% MU = mean(keplerdata1,1);
% SIGMA = cov(keplerdata1);
% rnd_number_1 = mvnrnd(MU,SIGMA,100);
% 
% MU = mean(keplerdata2,1);
% SIGMA = cov(keplerdata2);
% rnd_number_2 = mvnrnd(MU,SIGMA,100);
% 
% figure
% plot(rnd_number_1(:,1),rnd_number_1(:,2),'+')
% hold on
% plot(rnd_number_2(:,1),rnd_number_2(:,2),'o')



     % figure
     % plot(X_kepler(:,1),rnd_number(:,1),'+')
     % hold on
     % plot(X_kepler(:,2),rnd_number(:,2),'o')




teta = randi([-100 100],3,1)/10;


h_teta_x = 1./(1 + exp(-(teta(1,1).*X_general(:,1) + teta(2,1).*X_general(:,2) + teta(3,1).*X_general(:,3))));

error_func = 1./training_number.*(Y_general(:,1).*log(h_teta_x(:,1))+(1-Y_general(:,1)).*log(1-h_teta_x(:,1)));
alpha = 1;

epsilon=0.0020;

iter=0;
maxiter = 100000;

while  iter<maxiter 
    
    iter=iter+1;
    
    temp0 = 0;
    temp1 = 0;
    temp2 = 0;

    for i=1:1:training_number
    
       h(i,1) = 1/(1 + exp(-(teta(1,1)*X_general(i,1) + teta(2,1)*X_general(i,2) + teta(3,1)*X_general(i,3))));
    
       temp0 = temp0 + (h(i,1) - Y_general(i,1))*X_general(i,1);
    
       temp1 = temp1 + (h(i,1) - Y_general(i,1))*X_general(i,2);
       
       temp2 = temp2 + (h(i,1) - Y_general(i,1))*X_general(i,3);
    
    
    end

        tmp0 = teta(1,1) - 1/training_number*alpha*temp0;

        tmp1 = teta(2,1) - 1/training_number*alpha*temp1;

        tmp2 = teta(3,1) - 1/training_number*alpha*temp2;


        teta(1,1) = tmp0;

        teta(2,1) = tmp1;

        teta(3,1) = tmp2;
  
   
    for i = 1:1:training_number

        h(i,1) = 1/(1 + exp(-(teta(1,1)*X_general(i,1) + teta(2,1)*X_general(i,2) + teta(3,1)*X_general(i,3))));
        
        error_func(i,1) = 1/training_number*(Y_general(i,1)*log(h(i,1))+(1-Y_general(i,1))*log(1-h(i,1)));

    end
    
  mean(abs(error_func))
  
end

h_teta_x = 1./(1 + exp(-(teta(1,1).*X_general(:,1) + teta(2,1).*X_general(:,2) + teta(3,1).*X_general(:,3))));

figure
plot([1:1:training_number],Y_general);
figure
plot([1:1:training_number],h_teta_x);



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                           %
%              PLOT OF DATA SET             %
%                                           %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



% x1_boundary = abs(teta(1,1)/(teta(2,1)))*max(X_general_unnormalized(:,2));
% x2_boundary = abs(teta(1,1)/(teta(3,1)))*max(X_general_unnormalized(:,3));
% plot([0 x1_boundary*3],[0 x2_boundary*3]);




