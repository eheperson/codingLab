%%
clc;
clear all;
close all;
% Create symbolic variables x and y.
syms x y
%
%%
clc;
clear all;
close all;
% Create a 1-by-4 symbolic vector a with the 
% automatically generated elements a1...a4
syms 'a%d' [1 4]
%
%%
clc;
clear all;
close all;
% Create a 3-by-4 symbolic matrix with automatically generated elements. 
% The elements are of the form Aij, which generates the elements A11...A34
syms A [3 4]
%
%%
clc;
clear all;
close all;
% You can change the naming format of the generated elements 
% by using a format character vector. 
% syms replaces %d in the format character vector 
% with the index of the element to generate the element names
syms 'p_a%d' 'p_b%d' [4 4]
%
%% clc;
clear all;
close all;
% Create symbolic variables x and y, and assume that they are integers.
syms x y integer
%
% Create symbolic variable z, 
% and assume that it has a positive rational value.
syms z positive rational
%
% Create symbolic variables x and y.
% Check assumptions.
% assumptions(x) >> x is an integer
assumptions
%
% Clear assumptions on x, y, and z.
assume([x y z],'clear')
assumptions
%
%%
clc;
clear all;
close all;
% Create a 1-by-3 symbolic array a and assume that the array elements have real values.
syms a [1 3] real
assumptions
%
%%
clc;
clear all;
close all;
% Create symbolic functions with one and two arguments
syms s(t) f(x,y)
% Both s and f are abstract symbolic functions.
% They do not have symbolic expressions assigned to them, 
% so the bodies of these functions are s(t) and f(x,y), respectively.
%
% Specify the following formula for f.
f(x,y) = x + 2*y;
%
% Compute the function value at the point x = 1 and y = 2.
f(1,2)
%
%%
clc;
clear all;
close all;
% Create a symbolic function and specify its formula by using a symbolic matrix.
syms x 
M = [x x^3; x^2 x^4];
f(x) = M
%
% Compute the function value at the point x = 2:
f(2)
%
% Compute the value of this function for x = [1 2 3; 4 5 6]. 
% The result is a cell array of symbolic matrices.
xVal = [1 2 3; 4 5 6];
y = f(xVal)
%
% Access the contents of a cell in the cell array by using braces.
y{1}
%
%%
clc;
clear all;
close all;
% Create a 2-by-2 symbolic matrix with automatically generated symbolic functions as its elements.
syms f(x,y) 2
f
%
% Assign symbolic expressions to the symbolic functions f1_1(x,y) and f2_2(x,y). 
% These functions are displayed as f11(x,y) and f22(x,y) in the Live Editor. 
% When you assign these expressions, the symbolic matrix f still contains the 
% initial symbolic functions in its elements.
f1_1(x,y) = 2*x;
f2_2(x,y) = x - y;
f
%
% Substitute the expressions assigned to f1_1(x,y) and f2_2(x,y) 
A = subs(f)
%
% Evaluate the value of the symbolic matrix A, which contains the 
% substituted expressions at x = 2 and y = 3.
A(2,3)
% by using the subs function.
%
%%
clc;
clear all;
close all;