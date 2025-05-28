from fastapi import APIRouter

router = APIRouter()

# Dummy alerts - آپ چاہیں تو یہ DB سے dynamic بنا سکتے ہیں
recent_alerts = [
    {"type": "intrusion", "message": "Suspicious login pattern detected.", "time": "Just now"},
    {"type": "malware", "message": "Malware signature matched in executable.", "time": "5 min ago"},
    {"type": "anomaly", "message": "Unusual data flow to unknown IP.", "time": "10 min ago"},
    {"type": "phishing", "message": "Fake email detected and blocked.", "time": "15 min ago"},
]

@router.get("/recent-alerts")
def get_recent_alerts():
    return {"alerts": recent_alerts}