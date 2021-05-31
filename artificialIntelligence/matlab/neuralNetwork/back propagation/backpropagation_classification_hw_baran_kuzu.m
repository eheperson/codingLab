%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all;
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
m=330;
alpha=0.0000001;
epsilon=0.0011;

a_3=ones(2,330);

W=ones(2,3);
V=2*ones(2,3);

gradV=zeros(2,3);
gradW=zeros(2,3);

tempW=zeros(2,3);
tempV=zeros(2,3);

error_func=(1/2)*( a_3 - Y_general).^2;

a_1=X_general;

while(epsilon<mean(mean(error_func)))

W=ones(2,3);
V=2*ones(2,3);

a_2=1 ./( 1+exp( -W*a_1));
a_3=1./(1+exp(-V*[ones(1,330);a_2]));




%                                             **********************
%                                             **********************
%                                             **********************
%                                             **  sorunlu bölge,  **
%                                             **  aþaðýdaki iç içe**
%                                             **  for döngüsü     **
%                                             **********************
%                                   ******************************************
%                                     **************************************
%                                        ********************************
%                                            ************************
%                                               ******************
%                                                   **********
%                                                      ****

for i=1:1:330
    for h=1:1:2

        gradV = gradV + (transpose(a_3(:,i)-Y_general(:,i)))*a_2(:,i);
        gradW = gradW + ((transpose(V(:,2:end)))*(a_3(:,i)-Y_general(:,i))).*a_2(:,i).*(1.-a_2(:,i));        
    end   
end



tempW= W -(alpha/(2*m))*gradW;
tempV= V -(alpha/(2*m))*gradV;

W = tempW;
V = tempV;


        
error_func=(1/(2*m))*(a_3 - Y_general).^2;

mean(mean(error_func))

end

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

y_model_plot = 2*a_3(1,:) + 1*a_3(2,:);

hold on
plot(y_model_plot)


