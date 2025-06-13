from PIL import Image, ImageDraw, ImageFont

# Create a simple sketch of a geometry nodes setup for a generative arthritis hand brace
# This will be a conceptual node graph, not Blender-executable code

# Create image canvas
img = Image.new("RGB", (1200, 800), color="white")
draw = ImageDraw.Draw(img)

# Define font
try:
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 20)
except IOError:
    font = ImageFont.load_default()

# Node box drawing helper
def draw_node(x, y, title):
    width, height = 220, 80
    draw.rectangle([x, y, x + width, y + height], fill="#d8eaff", outline="black")
    draw.text((x + 10, y + 10), title, fill="black", font=font)

# Draw nodes
nodes = [
    (50, 50, "Hand Mesh (Input)"),
    (50, 180, "Brace Mask Generator"),
    (300, 50, "Sample Nearest Surface"),
    (300, 180, "Geometry Proximity"),
    (550, 50, "Curve to Mesh (Bands)"),
    (550, 180, "Instance on Points (Vents)"),
    (800, 100, "Join Geometry"),
    (1000, 100, "Solidify + Subdivision"),
]

for x, y, title in nodes:
    draw_node(x, y, title)

# Draw arrows between nodes
connections = [
    ((270, 90), (300, 90)),
    ((270, 220), (300, 220)),
    ((520, 90), (550, 90)),
    ((520, 220), (550, 220)),
    ((770, 120), (800, 120)),
    ((980, 120), (1000, 120)),
]

for start, end in connections:
    draw.line([start, end], fill="black", width=3)
    draw.polygon([end, (end[0]-10, end[1]-5), (end[0]-10, end[1]+5)], fill="black")

img.show()
