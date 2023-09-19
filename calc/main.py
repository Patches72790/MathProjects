import numpy as np
import matplotlib.pyplot as plt


def main():
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


if __name__ == "__main__":
    main()
