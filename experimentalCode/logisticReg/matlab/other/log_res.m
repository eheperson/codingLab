%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% logistic regression

clear all;
close all;
clc;

number_of_data = 1000;

mu1 = [2,3];
sigma1 = [1,1.5;1.5,3];
rng default;

rnd_number_1 = mvnrnd(mu1,sigma1,number_of_data);


mu2 = [5,4];
sigma2 = [1,1.5;1.5,3];
rng default;

rnd_number_2 = mvnrnd(mu2,sigma2,number_of_data);

figure
plot(rnd_number_1(:,1),rnd_number_1(:,2),'+');
hold on
plot(rnd_number_2(:,1),rnd_number_2(:,2),'o');

X0 = ones(2*length(rnd_number_1(:,1)),1);

X1 = [rnd_number_1(:,1);rnd_number_2(:,1)];
X2 = [rnd_number_1(:,2);rnd_number_2(:,2)];

X_general_unnormalized = [X0 X1 X2];
X_general = [X0 mat2gray(X1) mat2gray(X2)];

Y_general = [zeros(length(rnd_number_1(:,1)),1);ones(length(rnd_number_1(:,1)),1)];

training_number = length(X0);

%% model
% H(x) = 1/(1 + exp(teta_0*x0 + teta_1*x1 + teta_2*x2))

teta = randi([-20 100],3,1);

%% error function

error_func = -1./(training_number).*(Y_general.*log(1./(1 + exp(-(teta(1,1).*X_general(:,1) + teta(2,1).*X_general(:,2) + teta(3,1).*X_general(:,3))))) + (1 - Y_general).*log(1 - 1./(1 + exp(-(teta(1,1).*X_general(:,1) + teta(2,1).*X_general(:,2) + teta(3,1).*X_general(:,3))))));

learning_rate = 0.1;
epsilon = 1e-3*ones(length(X0),1);

iteration = 0;
iter_max = 20000;

figure
ax1 = subplot(3,1,1);   % mean error
h1 = animatedline;
ax2 = subplot(3,1,2);   % delta_error
h2 = animatedline;
ax3 = subplot(3,1,3);   % learning_rate
h3 = animatedline;

%% algorithm

while (sum(abs(error_func(:,1)) > epsilon) ~= 0) && iter_max > iteration
    
    iteration = iteration + 1
    
    internal_error_func = error_func;
    
    for i = 1 : 1 : training_number
        
        temp1 = teta(1,1) - learning_rate*(1/(1 + exp(-(teta(1,1)*X_general(i,1) + teta(2,1)*X_general(i,2) + teta(3,1)*X_general(i,3)))) - Y_general(i,1))*X_general(i,1);
        temp2 = teta(2,1) - learning_rate*(1/(1 + exp(-(teta(1,1)*X_general(i,1) + teta(2,1)*X_general(i,2) + teta(3,1)*X_general(i,3)))) - Y_general(i,1))*X_general(i,2);
        temp3 = teta(3,1) - learning_rate*(1/(1 + exp(-(teta(1,1)*X_general(i,1) + teta(2,1)*X_general(i,2) + teta(3,1)*X_general(i,3)))) - Y_general(i,1))*X_general(i,3);

        teta(1,1) = temp1;
        teta(2,1) = temp2;
        teta(3,1) = temp3;
        
        error_func(i,1) = -1/(training_number).*(Y_general(i,1)*log(1/(1 + exp(-(teta(1,1)*X_general(i,1) + teta(2,1)*X_general(i,2) + teta(3,1)*X_general(i,3))))) + (1 - Y_general(i,1))*log(1 - 1/(1 + exp(-(teta(1,1)*X_general(i,1) + teta(2,1)*X_general(i,2) + teta(3,1)*X_general(i,3))))));
        
        if isnan(error_func(i,1)) == 1
            error_func(i,1) = 0;
        end
        
        if isinf(error_func(i,1)) == 1
            error_func(i,1) = 10e3;
        end

    end
    
    mean(error_func)
    
    y_axis_limit = sum(error_func);
    
    xlim(ax1, [iteration - 50, iteration + 50])
    ylim(ax1, [y_axis_limit/5 y_axis_limit*5]);
    addpoints(h1,iteration,sum(error_func));
    drawnow limitrate
    
    if sum(isinf(internal_error_func)) == 0
        
        y_axis_limit = sum(internal_error_func) - sum(error_func);
        
        xlim(ax2, [iteration - 50, iteration + 50])
        ylim(ax2, [y_axis_limit/5 y_axis_limit*5]);
        addpoints(h2,iteration,sum(internal_error_func) - sum(error_func));
        drawnow limitrate
        
    end
    
    addpoints(h3,iteration,learning_rate)
    drawnow limitrate
    
    
end


h_teta_x = 1./(1 + exp(-(teta(1,1).*X_general(:,1) + teta(2,1).*X_general(:,2) + teta(3,1).*X_general(:,3))));

figure
plot([1:1:training_number],Y_general);
hold on
plot([1:1:training_number],h_teta_x);


plotDecisionBoundary(teta,X_general,Y_general)

%% logistic regression
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
