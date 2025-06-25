from manim import * 

"""class SVGMobject(file_name=None, should_center=True, height=2, width=None, color=None, opacity=None, 
                 fill_color=None, 
                 fill_opacity=None, 
                 stroke_color=None, 
                 stroke_opacity=None, 
                 stroke_width=None, 
                 svg_default=None, 
                 path_string_config=None, 
                 use_svg_cache=True, **kwargs)

"""


# svg als vectoren

from manim import *
import os

class DrawBraceAnimationNew(Scene): # Nieuwe scene naam
    def construct(self):
        # Stel de achtergrondkleur in op wit, als je dat wilt
        self.camera.background_color = WHITE

        # Pad naar je SVG-bestand
        svg_file_path = os.path.join("Manim", "inshallah_laatste_optimaal.svg") 
        print(f"Poging om SVG te laden vanaf: {svg_file_path}")

        try:
            brace_svg = SVGMobject(svg_file_path)

            
            brace_svg.set_fill(opacity=0)       
            brace_svg.set_stroke(BLACK, width=4) 

            brace_svg.scale(4) # Pas de schaal aan zodat het goed zichtbaar is
            brace_svg.center()

            
            self.play(Create(brace_svg, run_time=6))
            self.wait(1)

            """# Je kunt nu ook andere animaties toepassen op de SVGMobject
            self.play(brace_svg.animate.shift(LEFT * 2))
            self.wait(0.5)
            self.play(brace_svg.animate.rotate(PI / 2))
            self.wait(0.5)
            """

            # En je kunt hem weer "ontekenen"
            self.play(FadeOut(brace_svg, run_time=3))
            self.wait(1)

        except FileNotFoundError:
            print(f"Fout: SVG-bestand niet gevonden op {svg_file_path}")
            print("Controleer of het bestand echt in de 'Manim' map staat en de naam exact klopt.")
        except Exception as e:
            print(f"Er is een onverwachte fout opgetreden bij het laden of animeren van de SVG: {e}")


""""
# Test cirkel
class SvgManimScene(Scene):
    def construct(self):
        # Controleer of 'Manim' met een hoofdletter moet (zoals je eerder aangaf)
        svg_file_path = os.path.join("Manim", "test_cirkel.svg")

        try:
            svg_object = SVGMobject(svg_file_path)
            # Optioneel: schaal de cirkel zodat hij goed zichtbaar is
            svg_object.scale(2)
            self.add(svg_object)
            self.wait(2) # Wacht 2 seconden om hem te zien
        except FileNotFoundError:
            print(f"Fout: Test-SVG niet gevonden op {svg_file_path}")
            print("Zorg ervoor dat 'test_cirkel.svg' in de map '/Users/Eladje/Documents/GitHub/Manim/' staat.")
        except Exception as e:
            print(f"Er is een onverwachte fout opgetreden bij het laden van de TEST-SVG: {e}")
            print("Dit duidt op een probleem met de syntax van het SVG-bestand zelf. Dubbelcheck of je de XML exact hebt gekopieerd.")"""