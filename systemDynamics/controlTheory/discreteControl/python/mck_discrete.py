import numpy as np
import matplotlib.pyplot as plt

# Define Sampling Period
dt = 0.001

t_initial = 0.0
t_final = 15.0
#
# Initial Conditions 
x0 = 0
v0 = 0
#
# Creating array for variables
t = np.arange(t_initial, t_final, dt)
Xt_final = np.arange(t_initial, t_final, dt)
Vt_final = np.arange(t_initial, t_final, dt)
#
# Define input variable
u = np.arange(t_initial, t_final, dt)
#
for i in range(0, int((t_final - t_initial)/dt)):
    u[i] = 10
    #u[i] = i
    #u[i] = np.sin(2*np.pi*1*t[i])
#
# System Parameters 
m = 1
c = 2
k = 1
#
# Implement of forward difference for mck system
for i in range(0, int((t_final - t_initial)/dt) - 1):
    Xt_final[i+1] = Xt_final[i] + dt*(Vt_final[i])
    Vt_final[i+1] = Vt_final[i] + dt*(-k/m*Xt_final[i] - c/m*Vt_final[i] + u[i]/m)
    #print('X = {0}'.format(Xt_final[i]))
#
# Showing graph related to mck system
plt.figure()
#
plt.subplot(311)
plt.plot(t, Xt_final, 'r')
plt.ylabel("Position (m)")
plt.grid(True)
plt.title("MCK System")
#
plt.subplot(312)
plt.plot(t, Vt_final, 'r')
plt.ylabel("Velocity (m/s)")
plt.grid(True)
#
plt.subplot(313)
plt.plot(t, u, 'r')
plt.ylabel("Input (N)")
plt.grid(True)
#
plt.xlabel("Time (s)")
#
plt.show()