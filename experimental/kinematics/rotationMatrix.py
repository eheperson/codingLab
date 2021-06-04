#
#
import numpy as np
# 
#
theta0Deg = 90 # Theta 1 angle in degrees
theta1Deg = 0 # Theta 2 angle in degrees
#
theta0 = (theta0Deg/180.0)*np.pi # Theta 1 angle in radians
theta1 = (theta1Deg/180.0)*np.pi # Theta 2 angle in radians
#
R1_0 = [[np.cos(theta0), -np.sin(theta0), 0],
        [np.sin(theta0),  np.cos(theta0), 0],
        [             0,               0, 1]]
#
R2_1 = [[np.cos(theta1), -np.sin(theta1), 0],
        [np.sin(theta1),  np.cos(theta1), 0],
        [             0,               0, 1]]
#
#
R2_0 = np.dot(R1_0, R2_1)
#
print(R2_0)