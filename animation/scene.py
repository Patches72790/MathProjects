from manim import *


class PlotParametricFunction(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(
            lambda u: np.array([1.2 * np.cos(u) ** 2,1.2 * np.sin(u) ** 2, 1.2 * np.sin(u) ** 2]),
            color=RED,
            t_range=np.array([-10 * TAU, 10 * TAU, 0.01]),
        ).set_shade_in_3d(True)

        axes = ThreeDAxes()
        self.add(axes, curve1)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.wait()
