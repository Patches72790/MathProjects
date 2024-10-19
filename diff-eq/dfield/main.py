import numpy as np
import matplotlib.pyplot as plt


def dfield(nx=0.2, ny=0.2):

    x = np.arange(-3, 3, nx)
    y = np.arange(-3, 3, ny)

    X, Y = np.meshgrid(x, y)

    dy = Y
    dx = np.ones(dy.shape)

    plt.quiver(X, Y, dy, dx, color="green")
    plt.plot(x, np.exp(x), scalex=False, scaley=False)

    plt.show()


def main():

    dfield()


if __name__ == "__main__":
    main()
