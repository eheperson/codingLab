%
clc;
close all;
clear all;
%
%%
syms Ra La z1 z2 J B Kt Kb s
%
%%
J = 0.09;   
B = 0.05;
%
K = 85*10^-3;
Kt = K;
Kb = K;
%
Ra = 0.55;
La = 25*10^-3;
%
z1 = 1;
z2 = 10;
%
%%
TF = Kt*z1/((J*La*z1)*s^3 + (J*Ra*z1 + La*B*z1)*s^2 + (Ra*B*z1 + Kb*Kt*z2)*s);
%
%%
pretty(collect(TF, s))