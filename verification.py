from collections import Counter

def verify_order(expected, detected):

    expected_counter = Counter(expected)
    detected_counter = Counter(detected)

    missing = []
    extra = []

    # Missing items
    for item in expected_counter:

        if expected_counter[item] > detected_counter[item]:

            diff = expected_counter[item] - detected_counter[item]

            missing.extend([item] * diff)

    # Extra items
    for item in detected_counter:

        if detected_counter[item] > expected_counter[item]:

            diff = detected_counter[item] - expected_counter[item]

            extra.extend([item] * diff)

    status = "Verified"

    if missing or extra:

        status = "Failed"

    return {

        "status": status,

        "missing": missing,

        "extra": extra

    }