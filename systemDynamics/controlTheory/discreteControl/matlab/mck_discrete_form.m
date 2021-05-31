%% MCK System In Discrete Form 
%-----------------------------------------------------------------------
clear all;
close all;
clc;
%% Initial Values
%
x0 = 0;
v0 = 0;
%
syms s;
%
m = 1;
c = 2;
k = 1;
%
Fs = 10*1/s;
%
Xs = Fs*1/(m*s^2 + c*s + k);
%
Xt_cont = ilaplace(Xs);
%
fplot([Xt_cont])
xlim([0 15])
ylim([0 20])
grid on
xlabel('Time (sec)')
ylabel('Position (m)')
%
%% Numerical Solution
dt = 0.001;
%
t_initial = 0;
t_final = 15;
%
t = [t_initial : dt : t_final - dt];
%
N = (t_final - t_initial)/dt; %How moany points are utilized in loop
%
%% Forward Difference
%
Xt_forward = zeros(N,1);
Vt_forward = zeros(N,1);
%
% input
F = 10*ones(N, 1);
 %F = cos(2*t);
%
% initial conditions
Xt_forward = x0;
Vt_forward = v0;
%
for i = 1 : 1 : N - 1
    Xt_forward(i+1, 1) = Xt_forward(i,1) + dt*Vt_forward(i,1);
    Vt_forward(i+1, 1) = Vt_forward(i,1) + dt*(F(i)/m - c/m*Vt_forward(i,1) - k/m*Xt_forward(i,1));
end

hold on 
plot(t, Xt_forward)
legend('Real', 'Forward Difference');

