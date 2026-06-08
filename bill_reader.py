import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\tesseract.exe"
)

menu_items = [
    "burger",
    "fries",
    "coke"
]

img = Image.open("receipt_1.png")

text = pytesseract.image_to_string(img).lower()

print("OCR TEXT:")
print(text)

expected_order = []

for item in menu_items:
    if item in text:
        expected_order.append(item)

print("\nExpected Order:")
print(expected_order)