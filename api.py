
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from PIL import Image
import io
import json
import os
import pandas as pd

from verification import verify_order
from logger import log_detection

# ==========================================================
# FASTAPI APP
# ==========================================================

app = FastAPI(
    title="SmartQSR API",
    version="1.0"
)

# -----------------------------
# Current Order
# -----------------------------

current_order = []

# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================================
# LOAD MODEL
# ==========================================================

MODEL_PATH = "../runs/detect/train/weights/best.pt"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model not found: {MODEL_PATH}"
    )

model = YOLO(MODEL_PATH)

print("✅ SmartQSR Model Loaded")

# ==========================================================
# HOME
# ==========================================================

@app.get("/")
def home():

    return {
        "message": "SmartQSR Backend Running"
    }

# ==========================================================
# STATUS
# ==========================================================

@app.get("/status")
def status():

    return {

        "backend": "Running",

        "model": "Loaded",

        "camera": "Connected"

    }

# ==========================================================
# VERIFY ORDER
# ==========================================================

@app.post("/verify-order")
async def verify_order_api(
    expected_order: str = Form(...),
    file: UploadFile = File(...)
):
    try:

        # ---------------------------------
        # Parse expected order
        # ---------------------------------

        try:
            expected_order = json.loads(expected_order)

            if isinstance(expected_order, str):
                expected_order = [expected_order]

        except json.JSONDecodeError:

            expected_order = [
                item.strip().lower()
                for item in expected_order.split(",")
                if item.strip()
            ]

        print("\n==============================")
        print("EXPECTED ORDER:", expected_order)

        # ---------------------------------
        # Read uploaded image
        # ---------------------------------

        contents = await file.read()

        image = Image.open(io.BytesIO(contents))

        print("Image Loaded Successfully")

        # ---------------------------------
        # YOLO Detection
        # ---------------------------------

        results = model(image, conf=0.25)[0]

        print("Number of detections:", len(results.boxes))

        detected_items = []
        detections = []

        for box in results.boxes:

            cls = int(box.cls[0])

            label = results.names[cls].lower()

            confidence = float(box.conf[0])

            bbox = [
                int(x)
                for x in box.xyxy[0].tolist()
            ]

            print(f"Detected: {label} ({confidence:.2f})")

            detections.append({
                "label": label,
                "confidence": round(confidence, 2),
                "bbox": bbox
            })

            if label not in detected_items:
                detected_items.append(label)

        print("Detected Items:", detected_items)

        # ---------------------------------
        # Verification
        # ---------------------------------

        verification = verify_order(
            expected_order,
            detected_items
        )

        print("Verification:", verification)

        # ---------------------------------
        # Logging
        # ---------------------------------

        log_detection(
            expected_order,
            detected_items,
            verification["status"],
            verification["missing"],
            verification["extra"]
        )

        print("Detection Logged")

        # ---------------------------------
        # Response
        # ---------------------------------

        return {

            "status": verification["status"],

            "expected_order": expected_order,

            "detected_items": detected_items,

            "missing": verification["missing"],

            "extra": verification["extra"],

            "detections": detections,

            "processing_time": results.speed

        }

    except Exception as e:

        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# ==========================================================
# DETECTION HISTORY
# ==========================================================

from pathlib import Path

import csv

@app.get("/logs")
def get_logs():

    logs = []

    try:

        with open("logs.csv", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:
                logs.append(row)

        return logs

    except Exception as e:

        return {
            "error": str(e)
        }
# ==========================================================
# RUN SERVER
# ==========================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(

        "api:app",

        host="0.0.0.0",

        port=8000,

        reload=True

    )

from pydantic import BaseModel

class OrderRequest(BaseModel):
    expected_order: list[str]


@app.post("/set-order")
def set_order(order: OrderRequest):

    global current_order

    current_order = order.expected_order

    return {
        "message": "Order Stored Successfully",
        "expected_order": current_order
    }

class DetectionRequest(BaseModel):
    detected_items: list[str]


@app.post("/pi-verify")
def pi_verify(data: DetectionRequest):

    global current_order

    if not current_order:

        return {
            "status": "No Active Order"
        }

    verification = verify_order(
        current_order,
        data.detected_items
    )

    log_detection(
        current_order,
        data.detected_items,
        verification["status"],
        verification["missing"],
        verification["extra"]
    )

    return {

        "status": verification["status"],

        "expected_order": current_order,

        "detected_items": data.detected_items,

        "missing": verification["missing"],

        "extra": verification["extra"]

    }


