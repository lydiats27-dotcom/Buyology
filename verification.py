def verify_order(expected, detected):

    missing = set(expected) - set(detected)
    extra = set(detected) - set(expected)

    return missing, extra