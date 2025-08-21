import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# ==============================
# Condiciones iniciales
# ==============================
G = 1.0  # Constante gravitacional

m1, m2, m3 = 1.0, 1.0, 0.5

# Posiciones iniciales (x,y,z)
r1 = np.array([0.0, 0.0, 0.0])
r2 = np.array([0.5, 0.0, 0.0])
r3 = np.array([-0.5, 0.5, 1.0])

# Velocidades iniciales (vx,vy,vz)
v1 = np.array([0.0, 0.3, 0.0])
v2 = np.array([-0.3, 0.3, 0.0])
v3 = np.array([0.1, -0.1, -0.2])

# ==============================
# Funciones de dinámica
# ==============================
def acceleration(r, masses):
    """ Calcula aceleraciones de cada cuerpo en 3D """
    a = [np.zeros(3) for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i != j:
                rij = r[j] - r[i]
                dist = np.linalg.norm(rij)
                a[i] += G * masses[j] * rij / dist**3
    return a

# ==============================
# Simulación Leapfrog
# ==============================
dt = 0.01
steps = 2000

r = [r1.copy(), r2.copy(), r3.copy()]
v = [v1.copy(), v2.copy(), v3.copy()]
m = [m1, m2, m3]

traj = [[], [], []]

for step in range(steps):
    for i in range(3):
        traj[i].append(r[i].copy())
    
    a = acceleration(r, m)
    for i in range(3):
        v[i] += 0.5 * dt * a[i]
    for i in range(3):
        r[i] += dt * v[i]
    a = acceleration(r, m)
    for i in range(3):
        v[i] += 0.5 * dt * a[i]

traj = [np.array(t) for t in traj]

# ==============================
# Animación 3D
# ==============================
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection="3d")

colors = ['blue', 'red', 'orange']
labels = ['Star 1', 'Star 2', 'Star 3']

lines = [ax.plot([], [], [], color=colors[i], label=labels[i])[0] for i in range(3)]
points = [ax.plot([], [], [], 'o', color=colors[i])[0] for i in range(3)]

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_xlabel("x-coordinate")
ax.set_ylabel("y-coordinate")
ax.set_zlabel("z-coordinate")
ax.set_title("Three-Body Problem Animation")
ax.legend()

def init():
    for line, point in zip(lines, points):
        line.set_data([], [])
        line.set_3d_properties([])
        point.set_data([], [])
        point.set_3d_properties([])
    return lines + points

def update(frame):
    for i in range(3):
        lines[i].set_data(traj[i][:frame,0], traj[i][:frame,1])
        lines[i].set_3d_properties(traj[i][:frame,2])
        point = traj[i][frame]
        points[i].set_data([point[0]], [point[1]])
        points[i].set_3d_properties([point[2]])
    return lines + points

ani = FuncAnimation(fig, update, frames=steps, init_func=init, blit=False, interval=20)

plt.show()