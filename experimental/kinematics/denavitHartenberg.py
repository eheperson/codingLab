#
#
#
import numpy as np
#
#
#
# Parameter Table of "Denavit Hartenberg Method"
PT = [[0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]]
#
# Filling Homogenity Transformation Matrix from parameter table above
H0_1 = [[np.cos(PT[0][0]), -np.sin(PT[0][0])*np.cos(PT[0][1]),  np.sin(PT[0][0])*np.sin(PT[0][1]), PT[0][2]*np.cos(PT[0][0])],
        [np.sin(PT[0][0]),  np.cos(PT[0][0])*np.cos(PT[0][1]), -np.cos(PT[0][0])*np.sin(PT[0][1]), PT[0][2]*np.sin(PT[0][0])],
        [               0,                   np.sin(PT[0][1]),                   np.cos(PT[0][1]),                  PT[0][3]],
        [               0,                                  0,                                  0,                         1]]
# --- Rotation Matrices -----------------------------------------------------------------------#
