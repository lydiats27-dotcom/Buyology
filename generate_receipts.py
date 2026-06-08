import random
from PIL import Image, ImageDraw

menu = [
    "Burger",
    "Fries",
    "Coke"
]

for i in range(1, 51):

    items = random.sample(menu, random.randint(1, 3))

    img = Image.new("RGB", (500, 700), "white")
    draw = ImageDraw.Draw(img)

    y = 40

    draw.text((20, y), "BURGER SINGH", fill="black")
    y += 50

    draw.text((20, y), f"Order #{1000+i}", fill="black")
    y += 60

    draw.text((20, y), "Items:", fill="black")
    y += 50

    for item in items:
        draw.text((40, y), f"1 x {item}", fill="black")
        y += 40

    img.save(f"receipt_{i}.png")

print("50 receipts generated")