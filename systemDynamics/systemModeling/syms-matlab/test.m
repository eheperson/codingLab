% clc;
% close all;
% clear all;
% %% 
% syms t
% syms T T1 T2 T3
% syms m1 m2 m4 m4 mTotal
% syms I2 I3
% syms theta thetaF(t) beta betaF(t)
% syms r L2 
% 
% theta = thetaF(t)
% 
% thetaDot = diff(theta, thetaF)
% 
% syms f(x) y
% y = f(x)^2*diff(f(x),x);
% Dy = diff(y,f(x))
%%
% clc;
% close all;
% clear all;
% 
% 
% syms dt t T f A theta 
% syms m integer
% 
% mode =  t - T*floor(t/T);
% 
% theta = ( mode*(360/T));
% 
% pretty(simplify(theta))
% 
% 
% dt = 0.001;
% T = 360;
% 
% t = 0:dt:360;
% mode =  t - T*floor(t/T);
% 
% theta = ( mode*(360/T));
% 
% 
% thetaDot = diff(theta);
% thetaDotDot = diff(thetaDot);
%%
clear all;
close all;
clc;
%% System Parameters Symbolic definition
syms theta2(t) theta(t) x(t) thetaDot(t) theta2Dot(t) xDot(t) t
syms L2 L3
syms I2 I3 
syms m1 m2 m4
syms T1 T2 T3
syms V1 V2 V3
%
%% System variables calculations
x = L2*cos(theta) + sqrt(L3^2 - (L2^2)*(sin(theta)^2));
xDot = diff(x);
%
theta2 = asin((L2/L3)*sin(theta));
theta2Dot = diff(theta2);
% pretty(theta2Dot)
%
thetaDot = diff(theta);
%% Kinetic Energy Calculations
T1 = (I2*thetaDot^2)/2;
T2 = (I3*theta2Dot^2)/2;
T3 = m4*xDot/2;
%
T = T1 + T2 + T3;
%pretty(collect(T, theta))
%
%% Potential Energy Calculations
% V1 = 0;
% V2 = 0;
% V3 = 0;
%
% V = V1 + V2 + V3
%
%% Euler-Lagrange Method Implementation
L = T;


A =  diff(L,thetaDot(t));
B = diff(A);
pretty(B);





% t = 1/T;
% figure
% plot(time,theta)
% 
% sineW = A*sin(2*pi*f*time + phi)

% hold on
% plot(time,sineW)