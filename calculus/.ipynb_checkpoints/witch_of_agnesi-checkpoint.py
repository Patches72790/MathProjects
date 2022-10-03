import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax = plt.axes(xlim=(-5, 5), ylim=(-1, 4))
line, = ax.plot([], [], lw=2)

circle, = ax.plot([], [], lw=2)

diagonal, = ax.plot([], [], lw=2)

horizontal, = ax.plot([], [], lw=2)
vertical, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    circle.set_data([], [])
    diagonal.set_data([], [])
    horizontal.set_data([], [])
    vertical.set_data([], [])
    return line, circle, diagonal, horizontal, vertical

def witch_of_agnesi_fn(x, a):
    return (a ** 3) / (x**2 + a**2)

def diagonal_line_fn(x, a):
    agnesi_val = witch_of_agnesi_fn(x, a)
    return ((agnesi_val * a) / np.sqrt((2*agnesi_val) - (agnesi_val**2)))

def animate(i):
    x = np.linspace(-10, 10, 1000)
    y = witch_of_agnesi_fn(x, 2)
    line.set_data(x, y)
    
    radius = 1
    angle = np.linspace(0, 2 * np.pi, 150)
    c_x = radius * np.cos(angle)
    c_y = radius * (np.sin(angle) + 1)
    circle.set_data(c_x, c_y)

    diag_y = diagonal_line_fn(x, 2)
    diagonal.set_data(x, diag_y)

    #horizontal.set_data(y, 0)
    #vertical.set_data(0, y)

    return line, circle, diagonal, horizontal, vertical


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

#anim.save('basic.gif', fps=30)

plt.grid()
plt.show()
