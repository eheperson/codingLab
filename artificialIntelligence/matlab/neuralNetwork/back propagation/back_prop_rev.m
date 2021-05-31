
close all
load('class3_tr');          %% simple idea to get the code in run

% Epsilon 


%% User input
number_of_hidden_layer_node = 2;
number_of_output_layer_node = 2;
H = 4;
K = 2; 
I = 3;
%%% CLASSIFICATION Problem
%% Backpropagation Algorithm

%% Writing the dataset on the graph
variable = class3_tr;

length_of_class = length(variable(:,1))/3;

figure
plot(variable(1:length_of_class,1),variable(1:length_of_class,2),'+')
hold on
plot(variable(length_of_class+1:2*length_of_class,1),variable(length_of_class+1:2*length_of_class,2),'o')
hold on
plot(variable(2*length_of_class+1:3*length_of_class,1),variable(2*length_of_class+1:3*length_of_class,2),'*')

% Denotes Number of Training Examples
%N is for the FOR cycle
N = length(class3_tr);

% We define the error as N elemented series
error = 1;

error_func = ones(N,1);

error = sum(error_func);

%% Input values are arranged.
X0 = ones(3*length_of_class,1);                 % for bias input

X1 = variable(:,1);                             % for first input
X2 = variable(:,2);                             % for second input

Y_general = variable(:,3:4)';                    % target values

X_general_unnormalized = [X0 X1 X2];
X_general = [X0 mat2gray(X1) mat2gray(X2)]';     % normalization in order to provide better convergence


%parameters are arranged before calculations

%Weights for our system will be defined through using randi

epsilon = 0.01;
learning_rate = 1;
alfa = 0.5;

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
            

        end
        
        % y value calculation
        
        for k = 1 : 1 : K

            
        end
        
        % delta v coefficient calculation
        
        %% d_V() = zeros(K,H);
        %% first k, second h loop are established
        for k = 1 : 1 : K
            
            for h = 1 : 1 : H
                

                
            end
            
        end
        
        % delta w coefficient calculation
        
        %% d_W() = zeros(H,I);
        %% first h, second in loop are established
        
        for h = 1 : 1 : H
            
            for in = 1 : 1 : I

                
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

y_model_plot = 2*y(1,:) + 1*y(2,:);

hold on
plot(y_model_plot)

