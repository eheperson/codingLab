clear all;
close all
load('class3_tr');          %% simple idea to get the code in run

% Epsilon 


%% User input
number_of_hidden_layer_node = 2;
number_of_output_layer_node = 1;

H = 100000;
K = 1; 
I = 3;
%%% CLASSIFICATION Problem
%% Backpropagation Algorithm

%% Writing the dataset on the graph
[X,T] = valve_dataset;
X = cell2mat(X);
T = cell2mat(T);

delay = 1;

[xs, ts, xi] = prep(X,T,delay);

dataset = [xs ; ts];

variable = dataset';



% Denotes Number of Training Examples
%N is for the FOR cycle
N = length(variable);

% We define the error as N elemented series
error = 1;

error_func = ones(N,1);

error = sum(error_func);

%% Input values are arranged.
X0 = ones(N,1);                 % for bias input

X1 = variable(:,1);                             % for first input
X2 = variable(:,2);                             % for second input

Y_general = variable(:,3)';                    % target values

X_general_unnormalized = [X0 X1 X2];
X_general = [X0 mat2gray(X1) mat2gray(X2)]';     % normalization in order to provide better convergence


%parameters are arranged before calculations

%Weights for our system will be defined through using randi

epsilon = 0.001;
learning_rate = 1;
alfa = 0.1;

error_previous = 1;

% coefficient initialization

%% (1) define parametric coefficients, the reason is that user can change the dimensions of the layers,
%% (2) paving the way for creating for loops
W = randi([5 10],H,I)./100;
W_previous = randi([5 10],H,I)./100;
V = randi([5 10],K,H)./100;
V_previous = randi([5 10],K,H)./100;

% W = zeros(H,I);
% W_previous = randi([5 10],H,I)./100;
% V = zeros(K,H);
% V_previous = randi([5 10],K,H)./100;

%% (1) delta (d_W, d_V) and its real values (W,V) must be the same dimesions to each other
d_W = zeros(H,I);
d_V = zeros(K,H);

% temp variables including model values

%% (1) sigmoidal function and the total output must be arranged properly with the outputs of them:
%% z -> sigmoid function, so H output are produced. N - training set
z = zeros(H,N);
%% y -> total function, so K output are produced. N - training set
y = zeros(K,N);

figure
iteration = 0;      % iteration number obtained
ax1 = subplot(3,1,1);
h1 = animatedline;   % iteration graph is produced with animation feature
ax2 = subplot(3,1,2);
h2 = animatedline;
ax3 = subplot(3,1,3);
h3 = animatedline;

%% comparing with the total error
while error > epsilon
    iteration = iteration + 1;
    %% initialize all delta values after the training session
    d_W = zeros(H,I);
    d_V = zeros(K,H);
    
    % training session is started
    for i = 1 : 1 : N
        
        % z value calculation

        for h = 1 : 1 : H
            
            z(h,i) = 2/(1 + exp(-2*( W(h,1)*X_general(1,i) + W(h,2)*X_general(2,i) + W(h,3)*X_general(3,i) ) ) )  -1 ;
            % n = 2/(1+exp(-2*n))-1
        end
  
        
        % y value calculation
        
        for k = 1 : 1 : K

            y(k,i) = 2/(1 + exp(-2*( V(k,1)*z(1,i) + V(k,2)*z(2,i) + V(k,3)*z(3,i) + V(k,4)*z(4,i) ) ) ) -1;
            % n = 2/(1+exp(-2*n))-1
        end
         
        % delta v coefficient calculation
   
        %% d_V() = zeros(K,H);
        %% first k, second h loop are established
        for k = 1 : 1 : K
            
            for h = 1 : 1 : H
                
                d_V(k,h) = d_V(k,h) - (alfa)*(y(k,i) - Y_general(k,i))*z(h,i);
                
            end
            
        end
     
  
        % delta w coefficient calculation
        
        %% d_W() = zeros(H,I);
        %% first h, second in loop are established
     
        for h = 1 : 1 : H
            
            for in = 1 : 1 : I
                
                for k = 1 : 1 : K
                
                    d_W(h,in) = d_W(h,in) - (alfa)*((y(k,i) - Y_general(k,i))*V(k,h))*z(h,i)*(1 - z(h,i))*X_general(in,i);
               
                end
%             
            end
        end
        
   
        error_func(i,1) = sum(1/2*(Y_general(:,i) - y(:,i)).^2);
 end
    
    
    % we have to update the real weights(V,W) after the whole training process 
    % 
    

    
    error = sum(error_func)/N
    
%     if abs(error_previous - error) > 1e-5
%         learning_rate = learning_rate + 0.1;
%     else
%         learning_rate = learning_rate - 1e-6*learning_rate;
%     end
%     
%     
%     if abs(error_previous - error) > 1e-4
%         V = V + d_V/N + 0.1*V_previous/N;
%         W = W + d_W/N + 0.1*W_previous/N;
%     else 
%         V = V + d_V/N;
%         W = W + d_W/N;
%     end
    
    V = V + d_V/N;
    W = W + d_W/N;

    W_previous = d_W;
    V_previous = d_V;
    
end 
    
     


figure
Y_plot = zeros(1,330);

Y_plot(1:110) = 0;
Y_plot(111:220) = 1;
Y_plot(221:330) = 2;

plot(Y_plot)

y_model_plot =y(1,:);

hold on
plot(y_model_plot)

