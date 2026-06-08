import streamlit as st
from ultralytics import YOLO
from PIL import Image
from verification import verify_order

# Load model
model = YOLO("runs/detect/train-3/weights/best.pt")

st.title("🍔 AI Order Verification System")

# Expected Order
expected_order = ["burger", "fries", "coke"]

st.subheader("Expected Order")
st.write(expected_order)

uploaded_file = st.file_uploader(
    "Upload Order Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    results = model(image)

    detected_items = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            item = model.names[cls]

            if item not in detected_items:
                detected_items.append(item)

    st.subheader("Detected Items")
    st.write(detected_items)

    missing, extra = verify_order(
        expected_order,
        detected_items
    )

    st.subheader("Verification Result")

    if not missing and not extra:
        st.success("✅ Order Verified")

    else:

        if missing:
            st.error(
                f"❌ Missing Items: {list(missing)}"
            )

        if extra:
            st.warning(
                f"⚠ Extra Items: {list(extra)}"
            )