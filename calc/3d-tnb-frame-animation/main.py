import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def helix(t):
    return np.array([np.cos(t), np.sin(t), t])


def f_helix():
    return lambda t: helix(t)


def helix_prime(t):
    return np.array([-np.sin(t), np.cos(t), 1])


def f_prime_helix():
    return lambda t: helix_prime(t)


def unit_tangent(t):
    f = helix_prime(t)
    return f / np.linalg.norm(f)


def f_unit_tangent():
    return lambda t: unit_tangent(t)


def unit_normal(t):
    tan_prime = np.array([-np.cos(t) / np.sqrt(2), -np.sin(t) / np.sqrt(2), 0])
    return tan_prime / np.linalg.norm(tan_prime)


def f_unit_normal():
    return lambda t: unit_normal(t)


def unit_binorm(t, n):
    return np.cross(t, n)


def f_unit_binorm():
    return lambda u, v: unit_binorm(u, v)


def make_vector(f, t):
    return [*helix(t), *f(t)]


q1 = None
q2 = None
q3 = None


def update_vectors(t, ax, *vectors):
    x, y, z = helix(t)

    # unit tangent vector
    tan_vec = unit_tangent(t)

    # unit normal vector
    norm_vec = unit_normal(t)

    # unit  binormal vector
    binorm_vec = unit_binorm(tan_vec, norm_vec)

    # Can't redraw vector with new starting position, so delete old global references
    global q1
    global q2
    global q3

    if q1:
        q1.remove()
    if q2:
        q2.remove()
    if q3:
        q3.remove()

    q1 = ax.quiver(
        *make_vector(f_unit_tangent(), t), length=1, color="r", arrow_length_ratio=0.1
    )
    q2 = ax.quiver(
        *make_vector(f_unit_normal(), t), length=1, color="b", arrow_length_ratio=0.1
    )
    q3 = ax.quiver(
        x,
        y,
        z,
        *binorm_vec,
        length=1,
        color="g",
        arrow_length_ratio=0.1,
    )


def main():
    figure = plt.figure()
    ax = figure.add_subplot(projection="3d")

    # function
    t = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    x = np.cos(t)
    y = np.sin(t)
    z = t

    ax.plot(x, y, z)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.set_xlim([-2 * np.pi, 2 * np.pi])
    ax.set_ylim([-2 * np.pi, 2 * np.pi])
    ax.set_zlim([-2 * np.pi, 2 * np.pi])

    # animation
    ani = animation.FuncAnimation(
        figure,
        update_vectors,
        frames=np.linspace(-2 * np.pi, 2 * np.pi, 100),
        fargs=(ax, [q1, q2, q3]),
        interval=50,
    )

    # ani.save("bnf_animate.mp4")

    plt.show()


if __name__ == "__main__":
    main()
