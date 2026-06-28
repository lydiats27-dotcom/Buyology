
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import pytesseract
import pandas as pd

from verification import verify_order
from logger import log_detection

# --------------------------------
# CONFIGURATION
# --------------------------------

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

# --------------------------------
# LOAD MODEL
# --------------------------------

model = YOLO(
    "runs/detect/train/weights/best.pt"
)

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="AI Order Verification System",
    layout="wide"
)

st.title("🍔 AI Order Verification System")

st.markdown(
    "Upload a receipt and a food image to verify the order."
)

# --------------------------------
# RECEIPT UPLOAD
# --------------------------------

receipt_file = st.file_uploader(
    "Upload Receipt Image",
    type=["png", "jpg", "jpeg"],
    key="receipt"
)

expected_order = []

if receipt_file:

    receipt_img = Image.open(receipt_file)

    st.subheader("Receipt")

    st.image(
        receipt_img,
        width="stretch"
    )

    ocr_text = pytesseract.image_to_string(
        receipt_img
    ).lower()

    st.subheader("OCR Output")

    st.text(ocr_text)

    for item in MENU_ITEMS:

        if item in ocr_text:

            expected_order.append(item)

# --------------------------------
# FOOD IMAGE UPLOAD
# --------------------------------

food_file = st.file_uploader(
    "Upload Food Image",
    type=["png", "jpg", "jpeg"],
    key="food"
)

detected_items = []

if food_file:

    food_img = Image.open(food_file)

    results = model(
        food_img,
        conf=0.25
    )

    for r in results:

        plotted_image = r.plot()

        st.subheader("Detected Objects")

        st.image(
            plotted_image,
            channels="BGR",
            width="stretch"
        )

        for box in r.boxes:

            cls = int(box.cls[0])

            item = model.names[cls].lower()

            if item not in detected_items:

                detected_items.append(item)

# --------------------------------
# VERIFICATION
# --------------------------------

if receipt_file and food_file:

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Expected Order")

        st.write(expected_order)

    with col2:

        st.subheader("Detected Items")

        st.write(detected_items)

    # Verify Order
    result = verify_order(
        expected_order,
        detected_items
    )

    status = result["status"]
    missing = result["missing"]
    extra = result["extra"]

    # Save Detection Log
    log_detection(
        expected_order,
        detected_items,
        status,
        missing,
        extra
    )

    st.subheader("Verification Result")

    if status == "Verified":

        st.success(
            "✅ Order Verified Successfully!"
        )

    else:

        if missing:

            st.error(
                f"❌ Missing Items: {missing}"
            )

        if extra:

            st.warning(
                f"⚠️ Extra Items: {extra}"
            )

    # --------------------------------
    # SUMMARY
    # --------------------------------

    st.divider()

    st.subheader("Verification Summary")

    st.write(f"**Status:** {status}")

    st.write(f"**Expected Items:** {len(expected_order)}")

    st.write(f"**Detected Items:** {len(detected_items)}")

# --------------------------------
# DETECTION HISTORY
# --------------------------------

st.divider()

st.subheader("📜 Detection History")

try:

    history = pd.read_csv("logs.csv")

    st.dataframe(
        history,
        width="stretch"
    )

except FileNotFoundError:

    st.info(
        "No detection history available yet."
    )



