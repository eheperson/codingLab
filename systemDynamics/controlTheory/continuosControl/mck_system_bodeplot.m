clc;
clear all;
close all;
%%

m = 2;
c = 14;
k = 20;

t1 = tf([1], [m c k]);
t1

bode(t1)