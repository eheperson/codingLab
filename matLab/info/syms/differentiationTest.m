%% Differentiate Function
clc;
close all;
clear all;
% Find the derivative of the function sin(x^2).
syms f(x)
f(x) = sin(x^2);
Df = diff(f,x)
%
% Find the value of the derivative at x = 2.
Df2 = Df(2)
%
% Convert the value to double.
double(Df2)
%
%% Differentiation with Respect to Particular Variable
clc;
close all;
clear all;
