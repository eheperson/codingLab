
f = [0 100 200 300 400 500 600 700 800]; %force
x = [0 0.15 0.23 0.31 0.37 0.50 0.57 0.68 0.77]; %deflection

%slope calculation for linear model
% we use x = f*a model for our problem
a = (x(9) - x(1))/(f(9) - f(1));

figure

%plot the data 
plot(f,x, 'o')

hold on

% calculate the x est?mated deflect?on
%for our l?near model (x = f*a)
% x_p ?s the l?near model ?nput
x_p = f*a

%plot the linear model
plot(f,x_p, '--')


%plot specifications
xlabel('force')
ylabel('deflection')
title('force-deflection characteristic')
legend('real data', 'linear model', [330 55 0 0])