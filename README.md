# AI-Based Cybersecurity Threat Detection and Prevention System (Backend)

It uses Machine Learning models to detect and prevent various types of cyber threats.

## 🧠 Modules Included
- *Intrusion Detection* (UNSW-NB15 dataset)
- *Malware Detection*
- *Anomaly Detection*
- *Phishing Detection*

## ⚙️ Technology Stack
- *Framework*: FastAPI
- *Language*: Python
- *ML Models*: Scikit-learn, Pandas, Joblib
- *API Docs*: Auto-generated Swagger UI at /docs



## 📂 Folder Structure

AI_Cybersecurity_Project/
├── app/
│   ├── models/-Trained ML models (.pkl)
│   ├── routers/ -FastAPI endpoints
│   ├── _init_.py
│   └── main.py/ -FastAPI app entry point
├── requirements.txt/ -All dependencies
├── README.md/ -Project documentation
└── .gitignore


 Technologies Used

| Category           | Stack                                     |
|--------------------|-------------------------------------------|
| Language           | Python                                    |
| ML Libraries       | Scikit-learn, Joblib                      |
| Backend Framework  | FastAPI                                   |
| Deployment         | Uvicorn, Docker (optional)                |
| Mobile/Desktop App | Flutter                                   |
| Frontend (Web)     | React.js (Planned)                        |
| Database (Planned) | MongoDB / Firebase                        |





 API Endpoints

| Endpoint              | Description                  |
|-----------------------|------------------------------|
| /predict_intrusion  | Intrusion Detection          |
| /predict_malware    | Malware Detection            |
| /predict_anomaly    | Anomaly Detection            |
| /predict_phishing   | Phishing Detection           |

> All endpoints expect a JSON payload like:
 json
{
  "features": [feature1, feature2, ..., featureN]
}


## 🚀 How to Run

```bash
cd AI_Cybersecurity_Project
uvicorn app.main:app --reload
🧪 Testing

All endpoints can be tested from: 
http://127.0.0.1:8000/docs

✨ Author

Imaduddin003

```bash
notepad README.md



Future Scope

Full-featured Flutter Mobile/Desktop App

Web Dashboard in React.js

Real-time threat alerting via WebSockets

Cloud deployment with Docker & Nginx

Threat intelligence feeds (e.g., VirusTotal)



Submitted To Project Supervised

Prof.Dr Syed Hammad Sherazi
Email:syedhamad@hu.edu.pk


Final Year Project by:
Mr.Imad Ud Din
Mr.Sayed Salar Ahmad

Department of CS & IT
HAZARA UNIVERSITY MANSEHRA,PAKISTAN



License

MIT License
