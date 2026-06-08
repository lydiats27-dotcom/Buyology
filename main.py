from verification import verify_order

expected_order = [
    "burger",
    "fries",
    "coke"
]

detected_items = [
    "burger",
    "fries",
    "coke"
]

missing, extra = verify_order(
    expected_order,
    detected_items
)

if missing:
    print("Missing:", missing)

if extra:
    print("Extra:", extra)

if not missing and not extra:
    print("Order Verified")