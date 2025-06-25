"""from manim import *
import os

class BraceAnimation(Scene): # Verander de scene naam naar iets relevants
    def construct(self):
        # Pad naar je PNG-bestand
        # Zorg ervoor dat de bestandsnaam exact klopt
        png_file_path = os.path.join("Manim", "V5_brace(3).png")
        # Of, als je het korter hebt genoemd:
        # png_file_path = os.path.join("Manim", "brace.png")

        try:
            # Laad de PNG als een ImageMobject
            brace_image = ImageMobject(png_file_path)
            brace_image.invert(True)

            # Schaal en centreer de afbeelding zodat hij goed zichtbaar is
            brace_image.scale(0.5) # Of een andere schaal die past
            brace_image.center()

            # Voeg de afbeelding toe aan de scene
            self.add(brace_image)
            self.wait(1)

            # Voorbeeldanimaties voor de ImageMobject
            self.play(brace_image.animate.shift(LEFT * 2)) # Verplaats naar links
            self.wait(0.5)
            self.play(brace_image.animate.rotate(PI / 2)) # Roteer 90 graden
            self.wait(0.5)
            self.play(FadeOut(brace_image)) # Laat hem verdwijnen
            self.wait(0.5)
            self.play(FadeIn(brace_image)) # Laat hem weer verschijnen
            self.wait(1)

            # Als je de lijnen wilt "tekenen" (zoals met Write()),
            # dan moet je de PNG eerst vectoriseren (zie Optie 1 in mijn vorige antwoord)
            # en dan als SVG laden. Met ImageMobject kun je dit niet direct.

        except FileNotFoundError:
            print(f"Fout: PNG-bestand niet gevonden op {png_file_path}")
            print("Controleer of het bestand echt in de 'Manim' map staat en de naam exact klopt.")
        except Exception as e:
            print(f"Er is een onverwachte fout opgetreden bij het laden of animeren van de PNG: {e}")

"""

from manim import *
import os

class BraceAnimation(Scene):
    def construct(self):
        # --- ADD THIS LINE FOR TESTING ---
        self.camera.background_color = WHITE # Try WHITE, or BLUE, or RED

        png_file_path = os.path.join("Manim", "V5_brace(3).png")
        print(f"Attempting to load image from: {png_file_path}")

        try:
            brace_image = ImageMobject(png_file_path)
            

            
            brace_image.scale(2)
            brace_image.center()

            self.add(brace_image)
            self.wait(1)

            self.play(brace_image.animate.shift(LEFT * 2))
            self.wait(0.5)
            self.play(brace_image.animate.rotate(PI / 2))
            self.wait(0.5)
            self.play(FadeOut(brace_image))
            self.wait(0.5)
            self.play(FadeIn(brace_image))
            self.wait(1)

        except FileNotFoundError:
            print(f"Fout: PNG-bestand niet gevonden op {png_file_path}")
            print("Controleer of het bestand echt in de 'Manim' map staat en de naam exact klopt.")
        except Exception as e:
            print(f"Er is een onverwachte fout opgetreden bij het laden of animeren van de PNG: {e}")