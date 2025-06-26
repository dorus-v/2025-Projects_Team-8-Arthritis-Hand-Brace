# mijn_animatie.py



"""class HelloCircle(Scene):
    def construct(self):
        # blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        # We can also create a "plain" circle and add the desired attributes via set methods:
        circle = Circle()
        blue_circle = circle.set_color(BLUE).set_opacity(0.5)
        
        label = Text("A wild circle appears!")
        label.next_to(blue_circle, DOWN, buff=0.5)
        
        self.play(Create(blue_circle), Write(label))
        self.wait()
"""


"""from manim import *

class LineGraphExample(Scene):
    def construct(self):
        plane  = NumberPlane(
            x_range = (1, 7),
            y_range = (1 ,7) , 
            x_lenght = 7, 
            axis_config = {"include_numbers": True}
        )


        plane.centre()
        line_grapgh = plane.plot_line_graph(
            x_values = [0, 1.5, 2, 2.8, 4, 6.25],
            y_values = [1, 3, 2.25, 4, 2.5, 1.75],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,

        )


    self.add(plane , line_grapgh)
"""


from manim import *
import math

class MijnRatioGrafiekEchtNew(Scene):
    def construct(self):
        nieuwe_data = [
            (2, 0.6738163147980806),
            (3, 0.6974220979862596),
            (4, 0.688413993731318),
            (5, 0.6946060678505313),
            (6, 0.7258131054104111),
            (7, 0.7352160093373624),
            (8, 0.7509882011038868),
            (9, 0.7936531053777592),
        ]

        x_values = [d[0] for d in nieuwe_data]
        y_values = [d[1] for d in nieuwe_data]
        
        y_perfect_line_value = 2 / math.pi 

        plane = NumberPlane(
            x_range=(0, max(x_values) + 1, 1),
            y_range=(0.6, 0.9, 0.05),
            x_length=6,
            y_length=5,
            axis_config={ 
                "include_numbers": True,
                "numbers_to_exclude": [0],
                "font_size": 28,
            },
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            }
        )
        plane.center()

        x_axis_label = Tex("Number of cells", font_size=30).next_to(plane.x_axis, DOWN).shift(DOWN * 0.5)
        y_axis_label = Tex("Shrinkage factor", font_size=30).next_to(plane.y_axis, LEFT).rotate(90 * DEGREES).shift(LEFT * 0.5)
        
        self.add(plane, x_axis_label, y_axis_label) 

        graph = plane.plot_line_graph(
            x_values=x_values,
            y_values=y_values,
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3, fill_color=PURPLE),
            stroke_width=4,
            add_vertex_dots=True
        )

        line_start_point = plane.coords_to_point(plane.x_range[0], y_perfect_line_value)
        line_end_point = plane.coords_to_point(plane.x_range[1], y_perfect_line_value)
        
        perfect_line_graph = Line(start=line_start_point, end=line_end_point, color=RED_E, stroke_width=3)
        
        # Aangepast label voor de perfecte lijn: naast elkaar
        perfect_line_label = VGroup(
            Tex("Theoretical Value", font_size=20, color=RED_E), # Tekst eerst
            MathTex(r"\frac{2}{\pi}", font_size=30, color=RED_E) # Dan de wiskundige notatie
        ).arrange(RIGHT, buff=0.2).next_to( # Plaats ze naast elkaar (RIGHT) met een kleine afstand (buff)
            perfect_line_graph.get_right(), # Positioneer het VGroup ten opzichte van het rechteruiteinde van de lijn
            UP, buff=0.1 # En dan ietsje omhoog
        ).shift(RIGHT * 0.5) # Optionele extra verschuiving naar rechts


        self.play(
            Create(graph), 
            Create(perfect_line_graph), 
            Write(perfect_line_label),
            run_time=3 
        )

        self.wait(3)
# manim "Manim/mijn_"

# manim "Manim/mijn_animatie.py" MijnRatioGrafiekLaatste