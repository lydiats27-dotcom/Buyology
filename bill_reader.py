import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\tesseract.exe"
)

MENU_ITEMS = [
    "burger",
    "fries",
    "coke",
    "pizza",
    "pepsi",
    "sprite",
    "nuggets",
    "garlic_bread",
    "cold_coffee",
    "wrap"
]


def read_receipt(image_path):

    img = Image.open(image_path)

    text = pytesseract.image_to_string(
        img
    ).lower()

    expected_order = []

    for item in MENU_ITEMS:

        if item in text:

            expected_order.append(item)

    return expected_order

