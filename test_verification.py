from backend.verification import verify_order

print("=" * 50)
print("TEST CASE 1 - PERFECT MATCH")
print("=" * 50)

result = verify_order(
    ["burger", "fries", "coke"],
    ["burger", "fries", "coke"]
)

print(result)

print("\n" + "=" * 50)
print("TEST CASE 2 - MISSING ITEM")
print("=" * 50)

result = verify_order(
    ["burger", "fries", "coke"],
    ["burger", "fries"]
)

print(result)

print("\n" + "=" * 50)
print("TEST CASE 3 - EXTRA ITEM")
print("=" * 50)

result = verify_order(
    ["burger", "fries"],
    ["burger", "fries", "coke"]
)

print(result)

print("\n" + "=" * 50)
print("TEST CASE 4 - COMPLEX ORDER")
print("=" * 50)

result = verify_order(
    [
        "burger",
        "fries",
        "pizza",
        "sprite",
        "garlic_bread"
    ],
    [
        "burger",
        "pizza",
        "sprite",
        "pepsi"
    ]
)

print(result)