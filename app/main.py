from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import intrusion, malware, anomaly, phishing, dashboard, history, alerts

app = FastAPI()

# ✅ Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific domains e.g. ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Health check endpoint
@app.get("/")
def read_root():
    return {"message": "API Running"}

# ✅ Include all routers with proper prefixes
app.include_router(intrusion.router, prefix="/intrusion", tags=["Intrusion"])
app.include_router(malware.router, prefix="/malware", tags=["Malware"])
app.include_router(anomaly.router, prefix="/anomaly", tags=["Anomaly"])
app.include_router(phishing.router, prefix="/phishing", tags=["Phishing"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(history.router, prefix="/export", tags=["Export"])
app.include_router(alerts.router, prefix="/dashboard", tags=["Dashboard"])