import csv
import os
from datetime import datetime

LOG_FILE = "logs.csv"

def log_detection(expected, detected, status, missing, extra):

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Timestamp",
                "Expected Order",
                "Detected Order",
                "Status",
                "Missing Items",
                "Extra Items"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ", ".join(expected),
            ", ".join(detected),
            status,
            ", ".join(missing),
            ", ".join(extra)
        ])