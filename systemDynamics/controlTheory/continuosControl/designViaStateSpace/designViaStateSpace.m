clc;
close all;
clear all;
%
%% ------------------------------------------------------------------------
% Obtain all equation
%
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
%% State-Space Model Controllability Cntrol
%
Cm = ctrb(A,B); %ctrb_motor
%
rankCm = rank(Cm);
rankA = rank(A);
%
if rankCm - rankA == 0
   fprintf("State-Space Model is Controllable !!\n"); 
else
   fprintf("State-Space Model is not Controllable !!\n"); 
end
%
%% Roots of State-Space model in s-plane
fprintf("State-Space Model S-plane roots :"); 
eig(A)
%
%% Place Function - set s1 and s2 to desired locations
%
p = [-4, -5]; %desired pole locations
%
K = place(A, B, p); % required K matrix to set poles to desired locations
% K matrix : sets the locations of poles of characteristic equation in
% s-plane
%
Aclosedloop = (A-B*K); %Calculate new A matrix
%
eig(Aclosedloop) % check if new poles are same with 'p'


