# app/routers/history.py

from fastapi import APIRouter, Response
import csv
import io
import json

router = APIRouter()

# Sample data (آپ اپنی real prediction history یہاں رکھ سکتے ہیں)
history_data = [
    {"module": "Intrusion", "input": [0.1, 0.2, 0.3], "prediction": 1},
    {"module": "Malware", "input": [0.4, 0.5, 0.6], "prediction": 0},
]

# ✅ Old endpoints (ابھی بھی useful ہو سکتے ہیں)
@router.get("/history/json")
def get_history_json():
    return {"history": history_data}

@router.get("/history/csv")
def get_history_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["module", "input", "prediction"])
    for record in history_data:
        writer.writerow([record["module"], record["input"], record["prediction"]])
    response = Response(content=output.getvalue(), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=history.csv"
    return response

# ✅ New endpoints for frontend download button support
@router.get("/download-json")
def download_json():
    return Response(
        content=json.dumps(history_data),
        media_type="application/json",
        headers={"Content-Disposition": "attachment; filename=cyber_data.json"}
    )

@router.get("/download-csv")
def download_csv():
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["module", "input", "prediction"])
    writer.writeheader()
    writer.writerows(history_data)
    return Response(
        content=output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=cyber_data.csv"}
    )