clc;
close all;
clear all;
%%
% System Constants
R = 0.55;
J = 0.09;
Kt = 85*10^-3;
L = 25*10^-3;
b = 0.05;
%
%% State Space Matrix
%
a00 = -R/L;
a01 = -Kt/L;
a10 = Kt/J;
a11 = -b/J;
%
b00 = 1/L;
b10 = 0;
%
A = [a00, a01;
     a10, a11];
% 
B = [b00; b10];
%
%% Reference Tracking 
Anew = [A, zeros(2,1);
        0, 1, 0 ];
%
Bnew = [B; 0];
%
%% LQR Controller
%
Q = 1*diag(ones(3,1));
%
%Q(3,3) = 1e2; 
Q(3,3) = 1e3;
%
R = 1e1;
%
%% Matlab LQR Controller function
[K,S,e] = lqr(Anew, Bnew, Q, R);
%
%% Roots of the system 
eig(Anew - Bnew*K)
