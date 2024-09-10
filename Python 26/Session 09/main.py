# def sayHi(name):
#     print(f'hi {name}')
    
# sayHi('Morteza')
# sayHi('Nima')

import matplotlib.pyplot as plt
import numpy as np

# x = []
# y = []

# for i in range(100):
#     x.append(i/10)
#     y.append(np.sin(i/10))

# x = np.linspace(0, 2*np.pi, 100)

# y = np.sin(x)

# # print(x, y)

# plt.figure()
# plt.style.use('_mpl-gallery')

# plt.plot(x, y)
# plt.title('Sin(x)')
# plt.xlabel('time')
# plt.ylabel('sin')

# plt.show()

# x = np.random.normal(0, 2, 1000)

# plt.figure()

# plt.hist(x, 100)

# plt.show()
    
    
# x = np.linspace(0, 2*np.pi, 100)
# y = np.sin(x)
# f = np.fft.fft(y, 100)

# print(f)

# plt.figure()
# plt.plot(np.abs(f))
# plt.show()


# from matplotlib import cm

# plt.style.use('_mpl-gallery')

# n_radii = 8
# n_angles = 36

# # Make radii and angles spaces
# radii = np.linspace(0.125, 1.0, n_radii)
# angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]

# # Convert polar (radii, angles) coords to cartesian (x, y) coords.
# x = np.append(0, (radii*np.cos(angles)).flatten())
# y = np.append(0, (radii*np.sin(angles)).flatten())
# z = np.sin(-x*y)

# # Plot
# fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
# ax.plot_trisurf(x, y, z, vmin=z.min() * 2, cmap=cm.Blues)

# ax.set(xticklabels=[],
#        yticklabels=[],
#        zticklabels=[])

# plt.show()

# names = open('./names.txt', 'r')

# for i in names:
#     print(i)
    
import pyautogui as pag
import time

time.sleep(1)

# print(pag.position())

# pag.moveTo(333, 1005, 1)
pag.click(333, 1005, 1)
time.sleep(20)

pag.write('www.google.com')

pag.press('enter')
time.sleep(3)
pag.write('MortezaGhoddousi Github')
pag.press('enter')
time.sleep(3)

