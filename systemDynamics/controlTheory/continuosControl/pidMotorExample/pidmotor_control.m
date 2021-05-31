clc;
close all;
clear all;
%%
% Design system for :
%   t_rising = 0.1s
%   max_overshoot = 0.01 (%1)
% DESIGN IS IN SIMULINK
%%
syms K R L J b s Kp Kd KI;

G = K/((J*L)*s^2 + (J*R + L*b)*s + (R*b + K^2));


Gc = Kp + Kd*s;
Wd = 1/s;

Ts = (G*Gc)/(1 + G*Gc);
pretty(simplify(Ts))

%% Real System Parameter Assigment

J = 0.09;
K = 85*10^-3;
R = 0.55;
b = 0.05;
L = 25*10^-3;

Gv = K/((J*L)*s^2 + (J*R + L*b)*s + (R*b + K^2));
pretty(collect(Gv, s))

Gc_v = Kp + Kd*s;
Wd_v = 1/s;
%%
