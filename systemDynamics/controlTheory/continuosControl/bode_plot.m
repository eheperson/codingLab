clc;
clear all;
close all;
%%


H1 = tf([1], [0.2 2]);

H1

bode(H1)


H2 = tf([1], [0.2 1]);

H2

hold on

bode(H2)

H3 = H1*H2;

H3

hold on

bode(H3)