%% FORWARD - BACKWARD - CENTERED DIFFERENCE COMPARISION
%
clc;
clear all;
close all;
%
%% Numerical Solution
%initial and final time
%
x0 = 10;
%
dt = 0.001;
%
t_init = 0;
t_final = 5;
%
t = [t_init:dt:t_final-dt];
%
length_of_loop = (t_final-t_init)/dt;
%
%% ode45, ode23 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
options = odeset('RelTol', 1e-8, 'AbsTol', 1e-10, 'MaxStep', dt)
[t_ode,x] = ode45(@nonlinear_ode_fcn, [t_init t_final], [x0], options);
%
hold on
plot(t_ode, x)
legend('ode');
%
%
%% Backward Difference %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Xt_back = zeros(length_of_loop,1);
Xt_back(1,1) = x0;
%
for k = 2 : 1 : length_of_loop
    Xt_back(k,1) = Xt_back(k-1,1) + dt*(-5)*(Xt_back(k-1, 1)^2);
end
%
hold on
plot(t,Xt_back)
legend('ode', 'Backward Difference');
%
%
%% Forward Difference %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Xt_forward = zeros(length_of_loop, 1);
%
Xt_forward(1,1) = x0;

for k = 1 : 1 : length_of_loop-1
    Xt_forward(k+1,1) = Xt_forward(k,1) + dt*(-5)*(Xt_forward(k, 1)^2);
end
%
hold on
plot(t,Xt_forward)
legend('ode', 'Backward Difference', 'Forward Difference');

%% Centered Difference %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Xt_centered = zeros(length_of_loop, 1);
%
Xt_centered(1,1) = x0;
%Xt_centered(2,1) = x0;
%or
Xt_centered(2,1) = x0 + (-5)*dt*x0/5;
%
for k = 2 : 1 : length_of_loop-1
    Xt_centered(k+1,1) = Xt_centered(k-1,1) + 2*dt*(-5)*(Xt_centered(k-1, 1)^2);
end
%
hold on
plot(t,Xt_centered)
legend('ode', 'Backward Difference', 'Forward Difference', 'Centered Difference');
%
%
%
