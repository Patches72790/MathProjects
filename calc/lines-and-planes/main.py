import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def plane_curve():
    figure = plt.figure()
    ax = figure.add_subplot(projection="3d")

    def f(x, y):
        return x**2 + y**2

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    ax.plot_surface(X, Y, Z, color="gray", alpha=0.6)

    Z2 = Z * 0 + 10
    ax.plot_surface(X, Y, Z2, color="gray", alpha=0.3)

    plt.show()


def plane_intersection():
    ax = plt.figure().add_subplot(projection="3d")

    # plot axes
    x = np.linspace(-25, 25, 100)
    y = z = x * 0

    ax.plot(x, y, z, alpha=1, color="black")
    ax.plot(y, x, z, alpha=1, color="black")
    ax.plot(y, z, x, alpha=1, color="black")

    # plot point
    point = np.array([1, 2, 3])

    ax.scatter(*point, color="green", label="P(1, 2, 3)")

    # plot line through x axis and point
    x = np.ones(100)
    y = np.linspace(-15, 15, 100) * 2
    z = np.linspace(-15, 15, 100) * 3
    ax.plot(x, y, z, alpha=1, color="green")

    # plot plane
    f = lambda x, y: (3 / 2) * y + 0 * x

    X = np.linspace(-25, 25, 100)
    Y = np.linspace(-25, 25, 100)

    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    ax.plot_surface(X, Y, Z, color="red", alpha=0.3, label="plane")

    plt.show()


def sphere_with_sinusoidal_parametric():
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    # plot axes
    x = np.linspace(-2, 2, 100)
    y = z = x * 0

    ax.plot(x, y, z, alpha=1, color="black")
    ax.plot(y, x, z, alpha=1, color="black")
    ax.plot(y, z, x, alpha=1, color="black")

    t = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    x = np.sin(2 * t) / 2
    y = (1 - np.cos(2 * t)) / 2
    z = np.cos(t)

    ax.plot(x, y, z, label="parametric")

    # sphere
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 100), np.linspace(0, np.pi, 100))
    X = np.cos(u) * np.sin(v)
    Y = np.sin(u) * np.sin(v)
    Z = np.cos(v)

    ax.plot_surface(X, Y, Z, color="blue", alpha=0.3)

    plt.show()


def main():
    # plane_curve()
    # plane_intersection()
    sphere_with_sinusoidal_parametric()


if __name__ == "__main__":
    main()
