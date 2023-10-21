import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
from scipy import optimize

names = [ "l", "b", "r", "feh", "vr" ]

df = pd.read_csv("data.csv", skiprows=1, delimiter=',', names=names)

X, Y = df["l"], df["vr"]

plt.plot(X, Y, '.b')

z = np.polyfit(X, Y, 3)
f = np.poly1d(z)

plt.plot(X, f(X), '.r')

vo = f(0) # kmps
v = f(0) * np.pi/2 # kmps

Msun = 1.9891 * 10e30 #kg
Mregion = 10e11 * Msun # kg
G = 6.674e-11 # N m^2/kg^2

R = G * Mregion/(v * 10e3)**2 # m
d = R * 3.24078e-14 / 1000 # in kpc
R = R * 10e-3 # km
T = 2 * np.pi * R / v # s
print("Residue velocity v0 (kmps) = ", vo)
print("Orbital velocity (kmps) = ", v)
print("Distance of sun from the center (km) = ", R) # km
print("Distance of sun from center (kpc) = ", d)
print("Orbital period (s) = ", T)
print("Orbital period (yr) = ", T/(365 * 24 * 60 * 60))
print("Orbital period (million yr) = ", T/(365 * 24 * 60 * 60)/10e6)

plt.grid()
plt.show()
