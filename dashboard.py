import streamlit as st
from ultralytics import YOLO
from PIL import Image

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
    page_title="Food Detection Dashboard",
    layout="wide"
)

st.title("🍔 AI Food Detection Dashboard")

st.markdown(
    "Upload a food image to detect menu items using the trained YOLO model."
)

# --------------------------------
# IMAGE UPLOAD
# --------------------------------

uploaded_file = st.file_uploader(
    "Upload Food Image",
    type=["jpg", "jpeg", "png"]
)

# --------------------------------
# DETECTION
# --------------------------------

if uploaded_file:

    image = Image.open(uploaded_file)

    st.subheader("Uploaded Image")

    st.image(
        image,
        width="stretch"
    )

    results = model(
        image,
        conf=0.25
    )

    detected_items = []

    confidence_data = []

    for r in results:

        plotted_image = r.plot()

        st.subheader("Detection Results")

        st.image(
            plotted_image,
            channels="BGR",
            width="stretch"
        )

        for box in r.boxes:

            cls = int(box.cls[0])

            confidence = float(box.conf[0])

            item = model.names[cls].lower()

            if item not in detected_items:

                detected_items.append(item)

                confidence_data.append({
                    "Item": item,
                    "Confidence": f"{confidence:.2%}"
                })

    st.subheader("Detected Items")

    st.write(detected_items)

    st.subheader("Detection Confidence")

    st.table(confidence_data)

    st.success(
        f"Detected {len(detected_items)} item(s)"
    )

