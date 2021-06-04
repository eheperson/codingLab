#
#
#
import numpy as np
#
#
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
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
# --- Rotation Matrices -----------------------------------------------------------------------#
R0_1 = [[np.cos(theta1), -np.sin(theta1), 0],
        [np.sin(theta1),  np.cos(theta1), 0],
        [             0,               0, 1]]
#
R1_2 = [[np.cos(theta2), -np.sin(theta2), 0],
        [np.sin(theta2),  np.cos(theta2), 0],
        [             0,               0, 1]]
#
R2_3 = [[np.cos(theta3), -np.sin(theta3), 0],
        [np.sin(theta3),  np.cos(theta3), 0],
        [             0,               0, 1]]
#
R3_4 = [[np.cos(theta4), -np.sin(theta4), 0],
        [np.sin(theta4),  np.cos(theta4), 0],
        [             0,               0, 1]]
#
R4_5 = [[np.cos(theta5), -np.sin(theta5), 0],
        [np.sin(theta5),  np.cos(theta5), 0],
        [             0,               0, 1]]
#
R5_6 = [[np.cos(theta6), -np.sin(theta6), 0],
        [np.sin(theta6),  np.cos(theta6), 0],
        [             0,               0, 1]]
#
R0_2 = np.dot(R0_1, R1_2)
R2_4 = np.dot(R2_3, R3_4)
R4_6 = np.dot(R4_5, R5_6)
#
R0_4 = np.dot(R0_2, R2_4)
R0_6 = np.dot(R0_4, R4_6)
#
#
print("\nR0_1 : ")
print(np.matrix(R0_1))
#
print("\nR1_2 : ")
print(np.matrix(R1_2))
#
print("\nR2_3 : ")
print(np.matrix(R2_3))
#
print("\nR3_4 : ")
print(np.matrix(R3_4))
#
print("\nR4_5 : ")
print(np.matrix(R4_5))
#
print("\nR5_6 : ")
print(np.matrix(R5_6))
#
print("\nR0_6 : ")
print(np.matrix(R0_6))