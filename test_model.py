from ultralytics import YOLO
from PIL import Image
from verification import verify_order

# Load your newly trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Load test image
img = Image.open("test.jpg")

# Run detection with lower confidence threshold
results = model(img, conf=0.10, save=True)

detected_items = []

for r in results:
    print("\nDetected Objects:")

    for box in r.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])

        item = model.names[cls].lower()

        print(f"{item} | confidence = {conf:.2f}")

        if item not in detected_items:
            detected_items.append(item)

print("\nFinal Detected Items:", detected_items)

# Change this according to what's in test.jpg
expected_order = ["burger", "fries"]

missing, extra = verify_order(
    expected_order,
    detected_items
)

print("\nVerification Result:")

if missing:
    print("Missing:", missing)

if extra:
    print("Extra:", extra)

if not missing and not extra:
    print("✅ Order Verified")