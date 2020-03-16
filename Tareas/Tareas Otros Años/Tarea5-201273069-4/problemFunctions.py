import numpy as np

R1 = 100
dx1 = 0.1
dy1 = 0.1
dt1 = 0.01
a = c = 0
b = d = 1
T1 = 2
R2 = 1000
#####P1
p1u_real = lambda x, y, t: (3 / 4) - 1 / (4 * (1 + np.exp((-4 * x + 4 * y - t) * R1 / 32)))
p1v_real = lambda x, y, t: (3 / 4) + 1 / (4 * (1 + np.exp((-4 * x + 4 * y - t) * R1 / 32)))

p1u_t_0 = lambda x, y: (3 / 4) - 1 / (4 * (1 + np.exp((-4 * x + 4 * y) * R1 / 32)))
p1v_t_0 = lambda x, y: (3 / 4) + 1 / (4 * (1 + np.exp((-4 * x + 4 * y) * R1 / 32)))

p1u_x_a = lambda y, t: (3 / 4) - 1 / (4 * (1 + np.exp((-4 * a + 4 * y - t) * R1 / 32)))
p1u_x_b = lambda y, t: (3 / 4) - 1 / (4 * (1 + np.exp((-4 * b + 4 * y - t) * R1 / 32)))
p1u_y_c = lambda x, t: (3 / 4) - 1 / (4 * (1 + np.exp((-4 * x + 4 * c - t) * R1 / 32)))
p1u_y_d = lambda x, t: (3 / 4) - 1 / (4 * (1 + np.exp((-4 * x + 4 * d - t) * R1 / 32)))

p1v_x_a = lambda y, t: (3 / 4) + 1 / (4 * (1 + np.exp((-4 * a + 4 * y - t) * R1 / 32)))
p1v_x_b = lambda y, t: (3 / 4) + 1 / (4 * (1 + np.exp((-4 * b + 4 * y - t) * R1 / 32)))
p1v_y_c = lambda x, t: (3 / 4) + 1 / (4 * (1 + np.exp((-4 * x + 4 * c - t) * R1 / 32)))
p1v_y_d = lambda x, t: (3 / 4) + 1 / (4 * (1 + np.exp((-4 * x + 4 * d - t) * R1 / 32)))

####P2
p2u_real = lambda x, y, t: -4 * np.pi * np.exp((-5 * (np.pi ** 2) * t) / R2) * np.cos(2 * np.pi * x) * np.sin(
    np.pi * y) / (R2 * (2 + np.exp((-5 * (np.pi ** 2) * t) / R2) * np.sin(2 * np.pi * x) * np.sin(np.pi * y)))
p2v_real = lambda x, y, t: -2 * np.pi * np.exp((-5 * (np.pi ** 2) * t) / R2) * np.sin(2 * np.pi * x) * np.cos(
    np.pi * y) / (R2 * (2 + np.exp((-5 * (np.pi ** 2) * t) / R2) * np.sin(2 * np.pi * x) * np.sin(np.pi * y)))

p2u_t_0 = lambda x, y: -4 * np.pi * np.exp((-5 * (np.pi ** 2) * 0) / R2) * np.cos(2 * np.pi * x) * np.sin(np.pi * y) / (
        R2 * (2 + np.exp((-5 * (np.pi ** 2) * 0) / R2) * np.sin(2 * np.pi * x) * np.sin(np.pi * y)))
p2v_t_0 = lambda x, y: -2 * np.pi * np.exp((-5 * (np.pi ** 2) * 0) / R2) * np.sin(2 * np.pi * x) * np.cos(np.pi * y) / (
        R2 * (2 + np.exp((-5 * (np.pi ** 2) * 0) / R2) * np.sin(2 * np.pi * x) * np.sin(np.pi * y)))

p2u_x_a = lambda y,t :(-2*np.pi*np.exp(-5*((np.pi)**2)*t)*np.sin(np.pi*y)/R2)
p2u_x_b = lambda y,t: (-2*np.pi*np.exp(-5*((np.pi)**2)*t)*np.sin(np.pi*y)/R2)
p2u_y_c = lambda x,t: 0
p2u_y_d = lambda x,t: 0

p2v_x_a = lambda y,t: 0
p2v_x_b = lambda y,t: 0
p2v_y_c = lambda x, t: (-np.pi*np.exp(-5*((np.pi)**2)*t)*np.sin(2*np.pi*x)/R2)
p2v_y_d = lambda x, t: (np.pi*np.exp(-5*((np.pi)**2)*t)*np.sin(2*np.pi*x)/R2)
