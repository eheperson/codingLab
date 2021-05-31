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

# Forward difference
for k in range(0, int((t_final - t_initial)/dt) - 1):
    x[k + 1] = x[k] + dt*(-5*x[k])
    print("x = {0}".format(x[k]))


plt.figure()

plt.plot(t, x, 'r')
plt.ylabel('Meter (m)')
plt.xlabel('Time (sec)')
plt.grid(True)
plt.title('Forward Difference Method')

plt.show()