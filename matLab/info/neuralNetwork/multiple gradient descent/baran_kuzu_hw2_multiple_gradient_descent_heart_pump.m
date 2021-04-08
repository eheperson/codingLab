% function [coeff] = gradient_descent(input,output)
%%% This file includes multiple gradient descent algortihm to train model function by using derivation of cost function.

X_general = [66  4.00  7;
             66  4.50  7;
             66  5.00  7;
             66  5.56  7;
             66  5.80  7;
             66  4.00  8;
             66  4.50  8;
             66  5.00  8;
             66  5.56  8;
             66  5.80  8;
             71  4.00  7;
             71  4.50  7;
             71  5.00  7;
             71  5.56  7;
             71  5.80  7;
             71  4.00  8;
             71  4.50  8;
             71  5.00  8;
             71  5.56  8;
             71  5.80  8;             
             73  4.00  7;
             73  4.50  7;
             73  5.00  7;
             73  5.56  7;
             73  5.80  7];
         
         
x1_max = max(X_general(:,1));
x1_min = min(X_general(:,1));
X_general(:,1) = (X_general(:,1) - x1_min)./(x1_max-x1_min);

x2_max = max(X_general(:,2));
x2_min = min(X_general(:,2));
X_general(:,2) = (X_general(:,2) - x2_min)./(x2_max-x2_min);

x3_max = max(X_general(:,3));
x3_min = min(X_general(:,3));
X_general(:,3) = (X_general(:,3) - x3_min)./(x3_max-x3_min);

Y_general = [13.40;
             12.52;
              9.22;
              6.82;
              1.51;
             26.60;
             23.54;
             20.30;
             14.06;
             13.40;
             14.81;
             14.07;
             13.40;
              6.84;
              2.12;
             23.23;
             23.41;
             19.26;
             19.12;
             14.99;
             11.39;
             10.57;
              9.28;
              6.66;
              2.41];
          
 Y_general = [108.40;
              102.71;
              92.61;
              83.01;
              58.44;
              182.60;
              172.50;
              164.35;
              149.32;
              139.17;
              96.50;
              88.40;
              98.32;
              77.93;
              56.86;
              182.94;
              171.62;
              175.14;
              154.84;
              149.63;
              105.99;
              97.09;
              92.88;
              78.95;
              50.86];

y1_max = max(Y_general);
y1_min = min(Y_general);
Y_general = (Y_general(:,1) - y1_min)./(y1_max - y1_min);
%figure

X0 = ones(length(X_general(:,1)),1);

% plot3(x1,x2,y);
% grid on
training_number = length(X0);
X_general = [X0 X_general];

%% firstly, model function H(x) should be defined to train the network.
%% H(x) = teta_0*x0 + teta_1*x1 + teta_2*x2 + teta_2*x3

teta = randi([-5 5],4,1);

%% then, cost function should be prepared in order to be appropriate form
%% J(teta) = 1/2m*summation((h(x) - y)^2)

% firstly initial values should be assigned.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Your Code Should be in here

alpha = 0.001;        % learning rate
epsilon = 0.0017;          %epsilon (approximate error value)

 error_func = 1/2*(teta(1,1).*X_general(:,1) + teta(2,1).*X_general(:,2) + teta(3,1).*X_general(:,3) + teta(4,1).*X_general(:,4) - Y_general(:,1)).^2;
% while iter <= iter_max
while  mean(error_func) > epsilon

 
    temp0 = 0;
    temp1 = 0;
    temp2 = 0;
    temp3 = 0;
    
    for i = 1 : 1 : training_number
        
        h(i,1) = teta(1,1)*X_general(i,1) + teta(2,1)*X_general(i,2) + teta(3,1)*X_general(i,3) + teta(4,1)*X_general(i,4); %model fuction
      
        temp0 = temp0 + (h(i,1)-Y_general(i,1))*X_general(i,1);              % dJ/dteta0
      
        temp1 = temp1 + (h(i,1)-Y_general(i,1))*X_general(i,2);     % dJ/dteta1
        
        temp2 = temp2 + (h(i,1)-Y_general(i,1))*X_general(i,3);     % dJ/dteta2
        
        temp3 = temp3 + (h(i,1)-Y_general(i,1))*X_general(i,4);     % dJ/dteta3

    end
    
        tmp0 = teta(1,1) - ((alpha/(2*training_number))*temp0);     

        tmp1 = teta(2,1) - ((alpha/(2*training_number))*temp1);     
        
        tmp2 = teta(3,1) - ((alpha/(2*training_number))*temp2);     
        
        tmp3 = teta(4,1) - ((alpha/(2*training_number))*temp3);
        
        teta(1,1) = tmp0;      %
                               %
        teta(2,1) = tmp1;      % simultaneous update 
                               % for tetha values
        teta(3,1) = tmp2;      %
                               %
        teta(4,1) = tmp3;      %
        
    for i = 1 : 1 : training_number
        
        %error function declaration
        %error value calculation
        
        error_func(i,1) = 1/2*(teta(1,1)*X_general(i,1) + teta(2,1)*X_general(i,2) + teta(3,1)*X_general(i,3) + teta(4,1)*X_general(i,4) - Y_general(i,1))^2;
        
        

   end
    mean(error_func)
    
  
    
        
end







%% Your Code Should be in here
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


h_teta_x = teta(1,1).*X_general(:,1) + teta(2,1).*X_general(:,2) + teta(3,1).*X_general(:,3) + teta(4,1).*X_general(:,4);

teta

figure
plot([1:1:training_number],Y_general);
hold on
plot([1:1:training_number],h_teta_x);
legend('Y_general','h_teta_x');

coeff = 0;

%plotDecisionBoundary(teta, X_general, Y_general)

% end