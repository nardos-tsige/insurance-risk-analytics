# 🏦 AlphaCare Insurance Solutions - Risk Analytics Platform 
 
[![CI Pipeline](https://github.com/nardos-tsige/insurance-risk-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/nardos-tsige/insurance-risk-analytics/actions/workflows/ci.yml) 
[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![DVC](https://img.shields.io/badge/DVC-Data%20Version%20Control-9cf.svg)](https://dvc.org/) 
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black) 
 
--- 
 
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
├── .github/workflows/    # CI/CD pipeline (✅ passing) 
├── data/                 # Dataset (tracked by DVC) 
├── notebooks/            # Jupyter notebooks for each task 
│   ├── 01_eda.ipynb      # Task 1: EDA 
│   ├── 02_dvc_setup.ipynb # Task 2: DVC setup 
│   ├── 03_hypothesis_testing.ipynb # Task 3: Hypothesis tests 
│   └── 04_modeling.ipynb # Task 4: ML models 
├── src/                  # Reusable Python modules 
│   ├── data_loader.py    # Data loading utilities 
│   ├── eda_utils.py      # EDA visualization functions 
│   ├── clean_data.py     # DVC cleaning pipeline 
│   ├── hypothesis_tests.py # Statistical tests 
│   └── modeling.py       # ML models and pricing 
├── reports/              # Interim and final reports 
├── tests/                # Unit tests (✅ passing) 
├── requirements.txt      # Python dependencies 
├── LICENSE               # MIT License 
└── README.md             # This file 
``` 
 
--- 
 
## 🔬 Task Breakdown 
 
### ✅ Task 1: Exploratory Data Analysis 
- Analyzed 10,000 policies over 18 months 
- Overall loss ratio: 44.3% (profitable portfolio) 
- 85.4% of policies are profitable (Loss Ratio  1) 
- Identified Amhara (32%) as lowest risk province 
- Identified Addis Ababa (78%) as highest risk province 
- Sedan (35%) lowest risk, Luxury (80%) highest risk vehicle type 
 
### ✅ Task 2: Data Version Control (DVC) 
- DVC initialized with Google Drive remote storage 
- Raw data tracked: `data/insurance_data.csv` 
- Data cleaning pipeline: `src/clean_data.py` 
- Two versions: cleaned data and engineered features 
 
### ✅ Task 3: A/B Hypothesis Testing 
- **Province risk differences**: REJECTED H0 (p  0.05) 
- **Gender risk differences**: FAILED TO REJECT (p 
- **Vehicle type differences**: REJECTED H0 (p  0.05) 
- **Zip code margin differences**: REJECTED H0 (p  0.05) 
 
### ✅ Task 4: Statistical Modeling 
- **Claim Severity Model**: Random Forest (R² = 0.67) 
- **Claim Frequency Model**: Random Forest (F1 = 0.72) 
- **Risk-Based Pricing Formula**: Premium = P(claim) × Severity × 1.25 
- **Top Predictors**: Past claims, Risk Score, Vehicle Type 
 
--- 
 
## 🚀 How to Reproduce 
 
```bash 
git clone https://github.com/nardos-tsige/insurance-risk-analytics.git 
cd insurance-risk-analytics 
pip install -r requirements.txt 
dvc pull 
dvc repro 
pytest tests/ -v 
``` 
 
--- 
 
## 📈 Business Recommendations 
 
1. **Reduce premiums 15-20% in Amhara and Tigray** to capture market share 
2. **Increase premiums or add risk loadings** in Addis Ababa 
3. **Target Sedan and Hatchback owners** for marketing campaigns 
4. **Add loadings for customers with 3+ past claims** 
5. **Implement quarterly price reviews** due to increasing claim frequency 
 
--- 
 
## 👤 Author 
 
**Nardos Tsige** - Data Analytics Engineer 
 
--- 
 
## 📅 Date 
 
May 2026 
