from anaconda_navigator.utils.url_utils import file_name
from manim import *
class DefaultTemplate(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.flip(RIGHT)  # flip horizontally
        square.rotate(-3 * TAU / 8)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class SVGTest(Scene):
    def construct(self):
        circle_svg = SVGMobject("./assets/circle.svg")
        path = circle_svg.family_members_with_points()[0]

        path.set_fill(opacity=0)
        path.set_stroke(GREEN, 2)
        path.set_height(6)
        path.shift(0.5 * RIGHT)
        path2 = path.get_end_anchors()
        xy_data = path2[0:len(path2) - 1, 0:2]

class TraceSVGPath(Scene):
    def construct(self):
        # Load the SVG (place it in the same folder or give full path)
        svg = SVGMobject("./assets/brace folded out paths.svg")
        svg.set_color(WHITE)
        svg.scale(1)
        self.add(svg)

        # Choose a subpath to trace – e.g., the first one
        path_to_trace = svg[0]

        # Create a dot to trace along the path
        dot = Dot(color=YELLOW).move_to(path_to_trace.point_from_proportion(0))

        # Show dot tracing the path
        self.play(MoveAlongPath(dot, path_to_trace), run_time=5, rate_func=linear)

        # Optionally leave a trace behind
        traced_path = TracedPath(dot.get_center, stroke_color=YELLOW, stroke_width=2)
        self.add(traced_path)

        # Replay tracing with trace visible
        self.play(MoveAlongPath(dot, path_to_trace), run_time=5, rate_func=linear)


class FadeInSVGFromCorner(Scene):
    def construct(self):
        # Load and scale the SVG
        svg = SVGMobject("./assets/brace folded out paths.svg")  # Replace with your file
        svg.scale(1)
        svg.set_color(WHITE)

        # Sort submobjects from top-left (low y, low x) to bottom-right
        sorted_submobjects = sorted(
            svg.submobjects,
            key=lambda m: (-(m.get_center()[1]), m.get_center()[0])  # top to bottom, then left to right
        )

        # Add them one by one with a fade-in
        for submob in sorted_submobjects:
            self.play(FadeIn(submob), run_time=0.2)

        # Optional: wait a moment at the end
        self.wait()
