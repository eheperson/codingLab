#
#
#
import numpy as np
#
#
a1 = 1
a2 = 1
a3 = 1
a4 = 1
#
d1 = 1
d2 = 1
d3 = 1
#
theta1deg = 0 # Theta 1 angle in degrees
theta2deg = 0 # Theta 2 angle in degrees
theta3deg = 0 # Theta 3 angle in degrees
theta4deg = 0 # Theta 4 angle in degrees
theta5deg = 0 # Theta 5 angle in degrees
theta6deg = 0 # Theta 6 angle in degrees
#
theta1 = (theta1deg/180.0)*np.pi # Theta 1 angle in radians
theta2 = (theta2deg/180.0)*np.pi # Theta 2 angle in radians
theta3 = (theta3deg/180.0)*np.pi # Theta 3 angle in radians
theta4 = (theta4deg/180.0)*np.pi # Theta 4 angle in radians
theta5 = (theta5deg/180.0)*np.pi # Theta 5 angle in radians
theta6 = (theta6deg/180.0)*np.pi # Theta 6 angle in radians
#
#
# Parameter Table of "Denavit Hartenberg Method"
# Parameter table filled from  general cartesian manipulator example
# angles converted from degre to radian : (degree/180.0)*np.pi
PT = [[(90.0/180.0)*np.pi,  (90.0/180.0)*np.pi,  0, a1 + d1],
      [(90.0/180.0)*np.pi, (-90.0/180.0)*np.pi,  0, a2 + d2],
      [                 0,                   0,  0, a3 + d3]]
#
# Filling Homogenity Transformation Matricies for each frame from parameter table above
H0_1 = [[np.cos(PT[0][0]), -np.sin(PT[0][0])*np.cos(PT[0][1]),  np.sin(PT[0][0])*np.sin(PT[0][1]), PT[0][2]*np.cos(PT[0][0])],
        [np.sin(PT[0][0]),  np.cos(PT[0][0])*np.cos(PT[0][1]), -np.cos(PT[0][0])*np.sin(PT[0][1]), PT[0][2]*np.sin(PT[0][0])],
        [               0,                   np.sin(PT[0][1]),                   np.cos(PT[0][1]),                  PT[0][3]],
        [               0,                                  0,                                  0,                         1]]
#
H1_2 = [[np.cos(PT[1][0]), -np.sin(PT[1][0])*np.cos(PT[1][1]),  np.sin(PT[1][0])*np.sin(PT[1][1]), PT[1][2]*np.cos(PT[1][0])],
        [np.sin(PT[1][0]),  np.cos(PT[1][0])*np.cos(PT[1][1]), -np.cos(PT[1][0])*np.sin(PT[1][1]), PT[1][2]*np.sin(PT[1][0])],
        [               0,                   np.sin(PT[1][1]),                   np.cos(PT[1][1]),                  PT[1][3]],
        [               0,                                  0,                                  0,                         1]]
#
H2_3 = [[np.cos(PT[2][0]), -np.sin(PT[2][0])*np.cos(PT[2][1]),  np.sin(PT[2][0])*np.sin(PT[2][1]), PT[2][2]*np.cos(PT[2][0])],
        [np.sin(PT[2][0]),  np.cos(PT[2][0])*np.cos(PT[2][1]), -np.cos(PT[2][0])*np.sin(PT[2][1]), PT[2][2]*np.sin(PT[2][0])],
        [               0,                   np.sin(PT[2][1]),                   np.cos(PT[2][1]),                  PT[2][3]],
        [               0,                                  0,                                  0,                         1]]
#------------------------------------------------------------------------------------------------------------------------------------------------
# that lines of codes for copy and paste purpose
# it could be used in any loop algorthm also
# i = 0
# H2_3 = [[np.cos(PT[i][0]), -np.sin(PT[i][0])*np.cos(PT[i][1]),  np.sin(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.cos(PT[i][0])],
#         [np.sin(PT[i][0]),  np.cos(PT[i][0])*np.cos(PT[i][1]), -np.cos(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.sin(PT[i][0])],
#         [               0,                   np.sin(PT[i][1]),                   np.cos(PT[i][1]),                  PT[i][3]],
#         [               0,                                  0,                                  0,                         1]]
#------------------------------------------------------------------------------------------------------------------------------------------------
#
print("\nH0_1 : ")
print(np.matrix(H0_1))
#
print("\nH1_2 : ")
print(np.matrix(H1_2))
#
print("\nH2_3 : ")
print(np.matrix(H2_3))
#
#
H0_2 = np.dot(H0_1, H1_2)
H0_3 = np.dot(H0_2, H2_3)
#
print("\nH0_3 : ")
print(np.matrix(H0_3))