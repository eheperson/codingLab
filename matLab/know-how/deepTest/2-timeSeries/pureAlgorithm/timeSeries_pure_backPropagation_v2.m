clear all;
close all;
clc;

%% Prepare Input Dataset

[X,T] = valve_dataset;
X = cell2mat(X);
T = cell2mat(T);

delay = 1;

[xs, ts, xi] = prep(X,T,delay);

dataset = [xs ; ts];

dataset = dataset';

N = length(dataset);

x0 = ones (N,1);                % bias input              
x1 = dataset(:,1);              % for first input
x2 = dataset(:,2);              % for second input

                
xUnnormalized = [x0 x1 x2];
x = [x0 mat2gray(x1) mat2gray(x2)]';  

t = dataset(:,3)';

%% error parameters

errorArr = ones(N,1);
error = sum(errorArr);

%% Network PArameters
hiddenLayerSize = 10;
inputSize = 3;
targetSize = 1;
%% Weightss
w = randi([5 10],hiddenLayerSize,inputSize)./100;
wTemp = randi([5 10],hiddenLayerSize,inputSize)./100;
v = randi([5 10],targetSize,hiddenLayerSize)./100;
vTemp = randi([5 10],targetSize,hiddenLayerSize)./100;

%% delta matrices
dW = zeros(hiddenLayerSize,inputSize);
dV = zeros(targetSize,hiddenLayerSize);

%% Learning parameters 
epsilon = 0.001;
learning_rate = 1;
alfa = 0.1;

%%
z = zeros(hiddenLayerSize,N);
y = zeros(targetSize,N);

%% TRAINING SECTION

while error>epsilon
%     iteration = iteration + 1;
    % initialize all delta values
    dW = zeros(hiddenLayerSize,inputSize);
    dV = zeros(targetSize, hiddenLayerSize);
    
    %Forward adn Back Propagation Session
    
    for i = 1 : 1 : N
        
        %z value calculation
        for h = 1 : 1 : hiddenLayerSize
            z(h,i) = tansig(w(h,1)*x(1,i) + w(h,2)*x(2,i) + w(h,3)*x(3,i));
            %z(h,i) = 2/(1 + exp(-2*( w(h,1)*x(1,i) + w(h,2)*x(2,i) + w(h,3)*x(3,i) ) ) ) - 1 ;
            %tansig function
            % n = 2/(1+exp(-2*n))-1
        end

        for k = 1 : 1 : targetSize
            
            y(k,i) = tansig(v(k,1)*z(1,i) + v(k,2)*z(2,i) + v(k,3)*z(3,i) + v(k,4)*z(4,i));
            %y(k,i) = 2/(1 + exp(-2*( v(k,1)*z(1,i) + v(k,2)*z(2,i) + v(k,3)*z(3,i) + v(k,4)*z(4,i) ) ) ) -1;
            %tansig function
            % n = 2/(1+exp(-2*n))-1
        end
         
        % delta v coefficient calculation
        
        for k = 1 : 1 : targetSize
            
            for h = 1 : 1 : hiddenLayerSize
                
                dV(k,h) = dV(k,h) - (alfa)*(y(k,i) - t(k,i))*z(h,i);
                
            end
            
        end
        
        % delta w coefficient calculation
        for h = 1 : 1 : hiddenLayerSize
            
            for in = 1 : 1 : inputSize
                
                for k = 1 : 1 : targetSize
                    
                    dW(h,in) = dW(h,in) - (alfa)*((y(k,i) - t(k,i))*v(k,h))*z(h,i)*(1 - z(h,i))*x(in,i);
               
                end
%             
            end
        end
        
        % calculate error
        errorArr(i,1) = sum(1/2*(t(:,i) - y(:,i)).^2);
    end
    
    error = sum(errorArr)/N
    
    % Simultaneous update weights of network
    v = v + dV/N;
    v = w + dW/N;

end
