from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/summary")
def get_threat_summary():
    return {
        "intrusion": 3,
        "malware": 1,
        "anomaly": 4,
        "phishing": 0
    }

@router.get("/chart-data")
def get_chart_data():
    today = datetime.today()
    data = []

    for i in range(5):
        day = today - timedelta(days=i)
        data.append({
            "date": day.strftime("%Y-%m-%d"),
            "intrusion": (i + 1) % 5,
            "malware": (i * 2) % 5
        })

    return list(reversed(data))

@router.get("/alerts")
def get_recent_alerts():
    return [
        {
            "type": "intrusion",
            "message": "Suspicious login pattern detected.",
            "time": (datetime.utcnow()).isoformat()
        },
        {
            "type": "malware",
            "message": "Malware signature matched in executable.",
            "time": (datetime.utcnow() - timedelta(minutes=5)).isoformat()
        },
        {
            "type": "anomaly",
            "message": "Unusual data flow to unknown IP.",
            "time": (datetime.utcnow() - timedelta(minutes=10)).isoformat()
        },
        {
            "type": "phishing",
            "message": "Fake email detected and blocked.",
            "time": (datetime.utcnow() - timedelta(minutes=15)).isoformat()
        }
    ]