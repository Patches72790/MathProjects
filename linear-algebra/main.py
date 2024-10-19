import numpy as np
from numpy.linalg import inv
from scipy import linalg
from numpy._typing import NDArray


def hilbert(n: int):
    m = np.zeros((n, n))

    for i, row in enumerate(m):
        for j, col in enumerate(row):

            m[i, j] = 1 / (i + j + 1)

    return m


def describe(a: NDArray[np.float64]):
    print(f"Rank: {np.linalg.matrix_rank(a)}")
    print(f"Shape: {a.shape}")


def least_squares(A: NDArray[np.float64], b: NDArray[np.float64]):

    # A = linalg.orth(A)

    A_t = A.T

    print(f"A^T: \n{A_t}\n")

    A_t_A = np.matmul(A_t, A)

    print(f"A^T A: \n{A_t_A}\n")

    A_t_b = np.matmul(A_t, b)

    print(f"A^T b: \n{A_t_b}\n")

    P = np.matmul(np.matmul(A, inv(A_t_A)), A_t)
    print(f"P = \n{np.matmul(np.matmul(A, inv(A_t_A)), A_t)}\n")

    x = np.matmul(inv(A_t_A), A_t_b)

    print(f"x = \n{x}\n")

    p = np.matmul(P, b)

    e = b - p

    print(f"p = Pb = \n{p}\n")
    print(f"e = b - p = \n{e}\n")
    print(f"b = p + e = \n{p + e}\n")

    print(np.dot(p.T, e))


def least_squares_orthogonal(A: NDArray[np.float64], b: NDArray[np.float64]):

    q, r = linalg.qr(A)

    print("Q = \n", q)
    print("R = \n", r)

    q_t_b = np.matmul(q.T, b)
    print("Qt b = \n", q_t_b)

    r_t_r = np.matmul(r.T, r)

    print("RtR = \n", r_t_r)

    s = linalg.solve(r_t_r, q_t_b[:2])
    print(s)


def main():

    A = np.array([4, 5, 7])
    b = np.array([1, 2, 3])

    least_squares(
        np.array([[1, 1], [1, 5], [1, 11], [1, 12]]), np.array([[1], [3], [5], [7]])
    )

    least_squares_orthogonal(
        np.array([[1, 1], [1, 5], [1, 11], [1, 12]]),
        np.array([[1], [3], [5], [7]]),
    )


if __name__ == "__main__":
    main()
