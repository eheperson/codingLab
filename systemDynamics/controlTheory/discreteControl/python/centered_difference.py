import numpy as np 
import matplotlib
import matplotlib.pyplot as plt

dt = 0.001

t_initial = 0.0
t_final = 1.0

x0 = 10

# Data for plotting
t = np.arange(t_initial, t_final, dt)
x = np.arange(t_initial, t_final, dt)

x[0] = x0
x[1] = x0 + (-5)*dt*x0/5

# Backward difference
for k in range(1, int((t_final - t_initial)/dt) - 1):
    x[k + 1] = x[k - 1] + 2*dt*(-5)*x[k - 1]
    print("x = {0}".format(x[k]))


plt.figure()

plt.plot(t, x, 'r')
plt.ylabel('Meter (m)')
plt.xlabel('Time (sec)')
plt.grid(True)
plt.title('Backward Difference Method')

plt.show()