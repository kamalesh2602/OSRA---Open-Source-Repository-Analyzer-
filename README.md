# 🚀 OSRA - Open Source Repository Analyzer

A Machine Learning-powered web application that analyzes public GitHub repositories using repository metadata and unsupervised learning.

OSRA automatically collects repository information through the GitHub REST API, generates meaningful repository features, applies K-Means Clustering, and presents repository insights through an interactive analytics dashboard.

---

## 📖 Problem Statement

GitHub hosts millions of open-source repositories, making it difficult for developers to identify repositories that best suit their needs. While GitHub provides basic metrics such as stars, forks, contributors, and issues, these individual metrics do not provide a comprehensive understanding of a repository's development characteristics, maintenance quality, documentation standards, or community engagement.

As a result, developers often spend significant time manually evaluating repositories before deciding to adopt a library, contribute to an open-source project, or study a codebase. This process is time-consuming and largely depends on subjective interpretation of repository statistics.

---

## 💡 Proposed Solution

**OSRA (Open Source Repository Analyzer)** is a Machine Learning-powered repository analytics platform designed to provide a holistic analysis of GitHub repositories.

The platform automatically retrieves repository metadata using the GitHub REST API, constructs meaningful repository features, and applies **K-Means Clustering** to group repositories with similar development and maintenance characteristics.

Instead of relying solely on isolated metrics such as stars or forks, OSRA presents a consolidated repository profile through visual analytics and structured insights. This enables developers to better understand a repository's activity, community participation, documentation quality, and overall project characteristics before making technical decisions.

The project demonstrates a complete Machine Learning workflow by automatically collecting data, generating a custom dataset, training an unsupervised learning model, and deploying it through an interactive web application.

---

# ✨ Features

- 🔍 Analyze any public GitHub repository
- 📊 Interactive repository analytics dashboard
- 🤖 Machine Learning based repository profiling
- 📈 Automatic metadata extraction using GitHub REST API
- 🧠 K-Means Clustering based repository classification
- 📄 Repository insights generated from cluster characteristics
- 🌐 Modern React + FastAPI architecture

---

# 🏗️ Architecture

```
                 GitHub Repository URL
                          │
                          ▼
                 React Frontend (Vite)
                          │
                          ▼
                    FastAPI Backend
                          │
              GitHub Metadata Extraction
                          │
                          ▼
                  Feature Engineering
                          │
                          ▼
                  K-Means Prediction
                          │
                          ▼
        Repository Profile + Insights + Analytics
```

---

# 🧠 Machine Learning Pipeline

```
GitHub REST API
        │
        ▼
Repository Metadata Collection
        │
        ▼
Dataset Generation
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Scaling & Encoding
        │
        ▼
K-Means Clustering
        │
        ▼
Cluster Analysis
        │
        ▼
Model Serialization
        │
        ▼
Repository Prediction
```

---

# 📊 Repository Features

The clustering model is trained using repository characteristics including:

- Stars
- Forks
- Watchers
- Contributors
- Open Issues
- Repository Size
- README Size
- Branch Count
- Release Count
- Programming Language
- License Information
- Repository Age
- Development Activity
- Additional engineered features

---

# ⚙️ Technology Stack

### Frontend

- React
- TypeScript
- Tailwind CSS
- Vite

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Machine Learning

- Python
- pandas
- NumPy
- scikit-learn
- joblib

### APIs

- GitHub REST API

### Development Tools

- Git
- GitHub
- uv

---

# 📁 Project Structure

```
OSRA
├── client/          # React Frontend
├── server/
│   ├── app/         # FastAPI Backend
│   └── ml/          # ML Pipeline & Models
└── README.md
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/<your-username>/OSRA.git
cd OSRA
```

---

## Frontend

```bash
cd client

npm install

npm run dev
```

Runs on:

```
http://localhost:5173
```

---

## Backend

```bash
cd server

uv sync

uv run uvicorn app.main:app --reload
```

Runs on:

```
http://127.0.0.1:8000
```

Swagger API:

```
http://127.0.0.1:8000/docs
```

---

# 📌 Current Features

- ✅ Automatic GitHub metadata extraction
- ✅ Dataset generation using GitHub API
- ✅ Feature engineering pipeline
- ✅ K-Means clustering model
- ✅ Repository profile prediction
- ✅ Cluster-based repository insights
- ✅ Interactive analytics dashboard

---

# 🔮 Future Scope

- Repository comparison
- Repository health score
- Commit activity visualization
- Contributor analytics
- Organization-level analysis
- AI-generated repository recommendations
- Historical trend analysis
- User authentication and saved reports

---

# 👥 Team

Developed as a collaborative Machine Learning and Full Stack Development project.

---

