%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

close all
load('class3_tr');

%% User input
number_of_hidden_layer_node = 2;
number_of_output_layer_node = 2;

%%% CLASSIFICATION Problem
%% Backpropagation Algorithm

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Writing the dataset on the graph
variable = class3_tr;

length_of_class = length(variable(:,1))/3;

figure
plot(variable(1:length_of_class,1),variable(1:length_of_class,2),'+')
hold on
plot(variable(length_of_class+1:2*length_of_class,1),variable(length_of_class+1:2*length_of_class,2),'o')
hold on
plot(variable(2*length_of_class+1:3*length_of_class,1),variable(2*length_of_class+1:3*length_of_class,2),'*')

%% Writing the dataset on the graph
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Input values are arranged.
X0 = ones(3*length_of_class,1);                 % for bias input

X1 = variable(:,1);                             % for first input
X2 = variable(:,2);                             % for second input

Y_general = variable(:,3:4)';                    % target values

X_general_unnormalized = [X0 X1 X2];
X_general = [X0 mat2gray(X1) mat2gray(X2)]';     % normalization in order to provide better convergence

%% Input values are arranged.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Constant definition



%% Constant definition
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Training algorithm
size(X_general)


%% Training algorithm
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Test



%% Test
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

figure
Y_plot = zeros(1,330);

Y_plot(1:110) = 0;
Y_plot(111:220) = 1;
Y_plot(221:330) = 2;

plot(Y_plot)

y_model_plot = 2*y(1,:) + 1*y(2,:);

hold on
plot(y_model_plot)


