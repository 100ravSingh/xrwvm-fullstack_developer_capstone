# 🚗 Dealership Full-Stack Application

A full-stack web application built using **Django, React, MongoDB, Kubernetes, and IBM Cloud**, featuring dealer listings, reviews, sentiment analysis, authentication, and CI/CD automation.

---

## 🔧 Tech Stack

- **Frontend:** React
- **Backend:** Django
- **Database:** SQLite (Django), MongoDB (Dealership API)
- **Microservices:** Express + MongoDB, Sentiment Analyzer
- **Containerization:** Docker
- **Orchestration:** Kubernetes
- **CI/CD:** GitHub Actions
- **Cloud:** IBM Skills Network, IBM Code Engine

---

## ✨ Features

- Dealer listing & filtering by state
- Dealer detail page with reviews
- Review submission with sentiment analysis
- Authentication (login / register)
- Admin dashboard
- REST APIs
- CI/CD linting for Python & JavaScript
- Kubernetes-based deployment

---

## 📦 Project Structure

```

server/
├── djangoapp/
├── djangoproj/
├── database/        # Node + MongoDB API
├── frontend/        # React app
├── deployment.yaml

```

---

## 🚀 Getting Started

Follow the complete setup and deployment steps in:

➡️ **[DEPLOYMENT.md](DEPLOYMENT.md)**

---

## 🧪 CI/CD

- Python linting using **flake8**
- JavaScript linting using **JSHint**
- Runs on `push` and `pull_request` to `main`

---

## 📝 License

This project is part of the **IBM Full Stack Developer Capstone**.
```

---

## 📄 `DEPLOYMENT.md`

````md
# 🚀 Deployment & CLI Command Reference

This document lists **all CLI commands** used to develop, build, deploy, and debug the Dealership Full-Stack Application.

---

## 1️⃣ Python & Django Setup

```bash
python3 -m venv djangoenv
source djangoenv/bin/activate
pip install --upgrade pip
pip install django requests python-dotenv
````

Run server:

```bash
python3 manage.py runserver
```

---

## 2️⃣ Database & Migrations

```bash
rm db.sqlite3
rm -rf djangoapp/__pycache__
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
```

Create admin user:

```bash
python3 manage.py createsuperuser
```

---

## 3️⃣ React Frontend Build

```bash
cd server/frontend
npm install
npm run build
```

⚠️ Must be executed **before Docker build**

---

## 4️⃣ MongoDB + Express API

```bash
cd server/database
npm install
node app.js
```

Available APIs:

```
/fetchDealers
/fetchDealer/:id
/fetchReviews/dealer/:id
/insert_review
```

---

## 5️⃣ Sentiment Analyzer (IBM Code Engine)

```bash
docker build -t senti_analyzer .
docker tag senti_analyzer us.icr.io/$SN_ICR_NAMESPACE/senti_analyzer
docker push us.icr.io/$SN_ICR_NAMESPACE/senti_analyzer
```

Deploy:

```bash
ibmcloud ce application create \
  --name sentianalyzer \
  --image us.icr.io/$SN_ICR_NAMESPACE/senti_analyzer \
  --registry-secret icr-secret \
  --port 8080
```

Test:

```bash
curl https://sentianalyzer.<region>.codeengine.appdomain.cloud/analyze/Great%20service
```

---

## 6️⃣ Docker Build (Django + React)

```bash
MY_NAMESPACE=$(ibmcloud cr namespaces | grep sn-labs-)
docker build -t us.icr.io/$MY_NAMESPACE/dealership .
docker push us.icr.io/$MY_NAMESPACE/dealership
```

---

## 7️⃣ Kubernetes Deployment

```bash
kubectl apply -f deployment.yaml
kubectl get pods
kubectl rollout restart deployment dealership
kubectl port-forward deployment.apps/dealership 8000:8000
```

---

## 8️⃣ GitHub Actions

```bash
gh auth login
```

Linting:

* **Python:** flake8
* **JavaScript:** jshint

---

## 9️⃣ Debugging Commands

```bash
kubectl logs <pod-name>
kubectl get svc
netstat -tulnp
```

---

## 🔐 CSRF Fix (Skills Network)

```python
CSRF_TRUSTED_ORIGINS = [
    "https://<your-skill-network-domain>"
]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

---

## ✅ Deployment Complete

Access:

```
http://localhost:8000
/admin
/dealers
```

```

---
