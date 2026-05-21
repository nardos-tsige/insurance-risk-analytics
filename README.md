# 🏦 AlphaCare Insurance Solutions - Risk Analytics Platform 
 
## 📋 Project Overview 
 
AlphaCare Insurance Solutions (ACIS) requires evidence-driven strategies to optimize marketing investments and refine pricing models for the South African auto-insurance market. 
 
This project delivers a complete end-to-end insurance risk analytics solution including: 
 
- ✅ **Exploratory Data Analysis** - Risk patterns across provinces, vehicle types, and demographics 
- ✅ **Data Version Control** - Reproducible DVC pipeline for audit compliance 
- ✅ **A/B Hypothesis Testing** - Statistical validation of key risk drivers 
- ✅ **Predictive Modeling** - Claim severity and frequency prediction 
- ✅ **Risk-Based Pricing** - Dynamic premium optimization formula 
 
--- 
 
## 📊 Key Results 
 
 
--- 
 
## 🗂️ Repository Structure 
 
``` 
insurance-risk-analytics/ 
├── .github/workflows/    # CI/CD pipeline (disabled for submission) 
├── data/                 # Dataset (tracked by DVC) 
├── notebooks/            # Jupyter notebooks for each task 
│   ├── 01_eda.ipynb      # Task 1: EDA 
│   ├── 02_dvc_setup.ipynb # Task 2: DVC setup 
│   ├── 03_hypothesis_testing.ipynb # Task 3: Hypothesis tests 
│   └── 04_modeling.ipynb # Task 4: ML models 
├── src/                  # Reusable Python modules 
├── reports/              # Interim and final reports 
├── tests/                # Unit tests 
├── requirements.txt      # Python dependencies 
└── README.md             # This file 
``` 
 
--- 
 
## 🔬 Task Breakdown 
 
### Task 1: Exploratory Data Analysis 
- Analyzed loss ratio and margin across provinces, vehicle types, and gender 
- Detected outliers and temporal trends in claim frequency 
- Created 3 creative visualizations for business insights 
 
### Task 2: Data Version Control (DVC) 
- Initialized DVC with Google Drive remote storage 
- Created reproducible data cleaning pipeline 
- Tracked two versions: cleaned data and engineered features 
 
### Task 3: A/B Hypothesis Testing 
- **H₀: No gender risk differences** - [Result] 
 
### Task 4: Statistical Modeling 
- **Claim Severity Model**: Random Forest (R² = [Value]) 
- **Claim Frequency Model**: Random Forest (F1 = [Value]) 
- **Risk-Based Pricing Formula**: Premium = P(claim) × Severity × 1.25 
 
--- 
 
## 🚀 How to Reproduce 
 
```bash 
git clone https://github.com/nardos-tsige/insurance-risk-analytics.git 
cd insurance-risk-analytics 
pip install -r requirements.txt 
dvc pull 
dvc repro 
``` 
 
--- 
 
## 👤 Author 
 
**Nardos Tsige** - Data Analytics Engineer 
 
--- 
 
## 📅 Date 
 
May 2026 
