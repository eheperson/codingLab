#
#
import numpy as np
# import os
# #
# os.system('cmd /k "cls"') 
#
#
a1 = 5 # length of link a1 in cm
a2 = 6 # length of link a2 in cm
a3 = 5.5 # length of link a3 in cm
a4 = 5 # length of link a4 in cm
#
theta1deg = 10 # Theta 1 angle in degrees
theta2deg = 70 # Theta 2 angle in degrees
#
theta1 = (theta1deg/180.0)*np.pi # Theta 1 angle in radians
theta2 = (theta2deg/180.0)*np.pi # Theta 2 angle in radians
#
#
# --- Rotation Matrices -----------------------------------------------------------------------#
R0_1 = [[np.cos(theta1), -np.sin(theta1), 0],
        [np.sin(theta1),  np.cos(theta1), 0],
        [             0,               0, 1]]
#
R1_2 = [[np.cos(theta2), -np.sin(theta2), 0],
        [np.sin(theta2),  np.cos(theta2), 0],
        [             0,               0, 1]]
#
R0_2 = np.dot(R0_1, R1_2)
#
print("\n")
print("R0_2 : \n",R0_2, "\n")
#
#
# --- Displacement Vectors -----------------------------------------------------------------------#
d0_1 = [[a2*np.cos(theta1)],
        [a2*np.sin(theta1)],
        [a1]]
#
d1_2 = [[a4*np.cos(theta2)],
        [a4*np.sin(theta2)],
        [a3]]
#
print("\n")
print("d0_1 : \n", np.matrix(d0_1), "\n")
print("d1_2 : \n", np.matrix(d1_2), "\n")
#
#
