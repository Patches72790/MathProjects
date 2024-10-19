import numpy as np
from sympy import Matrix
import functools

from operator import lt


class LinearProgram:
    """
    Pass coefficients of objective function for xs
    Pass n-tuple of constraints with decision variables and operator function
    """

    def __init__(self, xs=[], constraints=[]) -> None:
        pass


class Simplex:
    def __init__(self, xs=[], constraints=[]) -> None:
        self.xs = np.array(xs)
        self.constraints = np.array(constraints)

        I = np.identity(len(constraints))
        RHS = self.constraints[:, -1]

        self.matrix = np.c_[self.constraints[:, 0:2], I, RHS]

    def __repr__(self):
        return f"Simplex(\n{self.matrix}\n)"

    # Pseudo-code:
    #   First, find col index for greatest magnitude of negative var
    #   Then, find smallest ratio of RHS to row var to find pivot
    #   Then, reduce column
    #   Then, repeat until no negative decision vars remain
    def solve(self):

        m = Matrix(self.matrix)

        decision_var_col_idx = 0
        decision_var_row_idx = 0

        idx, _ = functools.reduce(
            lambda acc, next: next if abs(next[1]) > abs(acc[1]) else acc,
            list(enumerate(self.matrix[-1, 0 : len(self.xs)])),
        )

        decision_var_col_idx = idx

        col = self.matrix[0 : len(self.xs), decision_var_col_idx]
        rhs = self.matrix[0 : len(self.xs), -1]
        print(min(map(lambda x: x[1] / x[0], zip(col, rhs))))


def main():
    xs = [20, 30]
    constraints = [[2, 2, lt, 25], [3, 4, lt, 10], [-20, -30, lt, 0]]

    s = Simplex(xs, constraints)
    print(s)
    s.solve()


if __name__ == "__main__":
    main()
