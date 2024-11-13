import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0, 4*np.pi, 50)
y1 = np.cos(x)
y2 = np.sin(x)

plt.figure()

# plt.title("HyperBolic Functions")
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.xlabel('Time')
# plt.ylabel('rad')
# plt.legend(['Cos', 'Sin'])

plt.subplot(2, 1, 1)
plt.title("HyperBolic Functions")
plt.plot(x, y1)
plt.xlabel('Time')
plt.ylabel('rad')

plt.subplot(2, 1, 2)
plt.title("HyperBolic Functions")
plt.plot(x, y2)
plt.xlabel('Time')
plt.ylabel('rad')

plt.show()



