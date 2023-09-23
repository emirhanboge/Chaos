import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio

alpha = 0.05
dx = 0.05 # Using a smaller dx for 3D simulation
dt = 0.5 * dx**2 / alpha
time_steps = 100

def initial_condition_1d(x):
    return np.exp(-40*(x-0.5)**2)

def initial_condition_2d(x, y):
    return np.sin(np.pi * x) * np.sin(np.pi * y)

def initial_condition_3d(x, y, z):
    return np.sin(np.pi * x) * np.sin(np.pi * y) * np.sin(np.pi * z)

def evolve_1d(u, alpha, dx, dt):
    """Evolve the 1D heat equation one time step."""
    u_new = np.copy(u)
    for i in range(1, len(u) - 1):
        u_new[i] = u[i] + alpha * dt / dx**2 * (u[i-1] - 2*u[i] + u[i+1])
    return u_new

def evolve_2d(u, alpha, dx, dt):
    """Evolve the 2D heat equation one time step."""
    u_new = np.copy(u)
    for i in range(1, u.shape[0] - 1):
        for j in range(1, u.shape[1] - 1):
            laplacian = u[i-1, j] + u[i+1, j] + u[i, j-1] + u[i, j+1] - 4*u[i, j]
            u_new[i, j] = u[i, j] + alpha * dt / dx**2 * laplacian
    return u_new

def evolve_3d(u, alpha, dx, dt):
    """Evolve the 3D heat equation one time step."""
    alpha = 0.01
    dx = 0.01
    u_new = np.copy(u)
    for i in range(1, u.shape[0] - 1):
        for j in range(1, u.shape[1] - 1):
            for k in range(1, u.shape[2] - 1):
                laplacian = u[i-1, j, k] + u[i+1, j, k] + u[i, j-1, k] + u[i, j+1, k] + u[i, j, k-1] + u[i, j, k+1] - 6*u[i, j, k]
                u_new[i, j, k] = u[i, j, k] + alpha * dt / dx**2 * laplacian
    return u_new

def create_gif(images, filename):
    with imageio.get_writer(filename, mode='I') as writer:
        for img in images:
            writer.append_data(img)

def remove_temp_files():
    import os
    for filename in os.listdir():
        if filename.startswith('temp_'):
            os.remove(filename)

def run_simulation_1d():
    x = np.arange(0, 1+dx, dx)
    u = initial_condition_1d(x)
    images = []

    for t in range(time_steps):
        plt.figure()
        plt.fill_between(x, u, color='r', alpha=0.4)  # Fill the area under the curve
        plt.plot(x, u, 'b')
        plt.title(f'1D Heat Equation at t={t*dt:.2f}')
        plt.ylim(0, 1)
        filename = f"temp_1d_{t}.png"
        plt.savefig(filename)
        images.append(imageio.imread(filename))
        plt.close()
        u = evolve_1d(u, alpha, dx, dt)

    create_gif(images, 'assets/heat_1d.gif')
    remove_temp_files()

def run_simulation_2d():
    x = np.arange(0, 1+dx, dx)
    y = np.arange(0, 1+dx, dx)
    X, Y = np.meshgrid(x, y)
    u = initial_condition_2d(X, Y)
    images = []

    for t in range(time_steps):
        plt.figure()
        plt.imshow(u, extent=[0, 1, 0, 1])
        plt.colorbar()
        plt.title(f'2D Heat Equation at t={t*dt:.2f}')
        filename = f"temp_2d_{t}.png"
        plt.savefig(filename)
        images.append(imageio.imread(filename))
        plt.close()
        u = evolve_2d(u, alpha, dx, dt)

    create_gif(images, 'assets/heat_2d.gif')
    remove_temp_files()

def run_simulation_3d():
    alpha = 0.01
    dx = 0.01
    x = np.arange(0, 1+dx, dx)
    y = np.arange(0, 1+dx, dx)
    z = np.arange(0, 1+dx, dx)
    X, Y, Z = np.meshgrid(x, y, z)
    u = initial_condition_3d(X, Y, Z)
    images = []

    slices = [int(0.2/dx), int(0.5/dx), int(0.8/dx)]  # slices of the domain

    for t in range(time_steps):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for s in slices:
            ax.scatter(X[:,:,s], Y[:,:,s], u[:,:,s], c=u[:,:,s].ravel(), cmap='viridis')
        ax.set_title(f'3D Heat Equation at t={t*dt:.2f}')
        filename = f"temp_3d_{t}.png"
        plt.savefig(filename)
        images.append(imageio.imread(filename))
        plt.close(fig)
        u = evolve_3d(u, alpha, dx, dt)

    create_gif(images, 'assets/heat_3d.gif')
    remove_temp_files()

if __name__ == "__main__":
    run_simulation_1d()
    run_simulation_2d()
    run_simulation_3d()

