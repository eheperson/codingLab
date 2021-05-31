#
#
import numpy as np
# 
#
theta0Deg = 90
theta1Deg = 0
#
theta0Rad = (theta0Deg/180.0)*np.pi
theta1Rad = (theta1Deg/180.0)*np.pi
#
R1_0 = [[np.cos(theta0Rad), -np.sin(theta0Rad), 0],
        [np.sin(theta0Deg),  np.cos(theta0Deg), 0],
        [                0,                  0, 1]]
#
R2_1 = [[np.cos(theta1Rad), -np.sin(theta1Rad), 0],
        [np.sin(theta1Deg),  np.cos(theta1Deg), 0],
        [                0,                  0, 1]]
#
#
R2_0 = np.dot(R1_0, R2_1)
#
print(R2_0)