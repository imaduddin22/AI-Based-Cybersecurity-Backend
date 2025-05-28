def predict_threat(features: dict):
    # یہ dummy logic ہے جو صرف values کو چیک کر کے result دے رہا ہے
    result = {}

    if features.get("network_traffic") > 1000:
        result["intrusion"] = "Detected"
    else:
        result["intrusion"] = "Not Detected"

    if features.get("suspicious_emails") > 5:
        result["phishing"] = "Detected"
    else:
        result["phishing"] = "Not Detected"

    if features.get("file_changes") > 10:
        result["malware"] = "Detected"
    else:
        result["malware"] = "Not Detected"

    return result