# 🏦 AlphaCare Insurance Solutions - Risk Analytics Platform 
 
[![CI Pipeline](https://github.com/nardos-tsige/insurance-risk-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/nardos-tsige/insurance-risk-analytics/actions/workflows/ci.yml) 
[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/) 
[![DVC](https://img.shields.io/badge/DVC-Data%20Version%20Control-9cf.svg)](https://dvc.org/) 
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black) 
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) 
[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange.svg)](https://jupyter.org/) 
[![GitHub branches](https://img.shields.io/github/branches/nardos-tsige/insurance-risk-analytics)](https://github.com/nardos-tsige/insurance-risk-analytics/branches) 
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/nardos-tsige/insurance-risk-analytics)](https://github.com/nardos-tsige/insurance-risk-analytics/commits/main) 
 
--- 
 
## 📋 Project Overview 
 
 insurance risk analytics and predictive modeling for premium optimization** 
 
AlphaCare Insurance Solutions (ACIS) is preparing for aggressive growth in the South African auto-insurance market. This project delivers evidence-driven strategies to optimize marketing investments and refine pricing models through: 
 
- ✅ **Exploratory Data Analysis** - Uncovering risk patterns across provinces, vehicle types, and demographics 
- ✅ **Data Version Control** - Reproducible DVC pipeline for audit compliance 
- ✅ **A/B Hypothesis Testing** - Statistical validation of key risk drivers 
- ✅ **Predictive Modeling** - Claim severity and frequency prediction with ML 
- ✅ **Risk-Based Pricing** - Dynamic premium optimization formula 
 
--- 
 
## 📊 Key Metrics 
 
 
--- 
 
## 🗂️ Project Structure 
 
``` 
insurance-risk-analytics/ 
├── .github/workflows/          # CI/CD pipeline 
│   └── ci.yml                  # GitHub Actions workflow 
├── data/                       # Dataset (tracked by DVC) 
├── notebooks/                  # Jupyter notebooks 
│   ├── 01_eda.ipynb           # Task 1: EDA 
│   ├── 02_dvc_setup.ipynb     # Task 2: DVC setup 
│   ├── 03_hypothesis_testing.ipynb  # Task 3: Hypothesis tests 
│   └── 04_modeling.ipynb      # Task 4: ML models 
├── src/                        # Reusable Python modules 
│   ├── __init__.py 
│   ├── data_loader.py         # Data loading utilities 
│   ├── eda_utils.py           # EDA visualization functions 
│   ├── clean_data.py          # DVC cleaning pipeline 
│   ├── hypothesis_tests.py    # Statistical tests 
│   └── modeling.py            # ML models and pricing 
├── reports/                    # Project documentation 
│   ├── interim_report.md      # Interim submission 
│   └── final_report.md        # Final Medium-style report 
├── tests/                      # Unit tests 
│   └── test_sample.py 
├── .dvc/                       # DVC configuration 
├── dvc.yaml                    # DVC pipeline definition 
├── requirements.txt            # Python dependencies 
└── README.md                   # This file 
``` 
 
--- 
 
## 🔬 Task Breakdown 
 
### ✅ Task 1: Exploratory Data Analysis 
 
**Objective:** Understand data quality, risk patterns, and portfolio performance 
 
**Deliverables:** 
- Loss ratio calculation and profitability analysis 
- Risk variation by province, vehicle type, and gender 
- Temporal trend analysis (claim frequency over time) 
- Outlier detection in key financial variables 
- 3 creative visualizations with actionable insights 
 
**Key Finding:** [Your key finding from EDA] 
 
### ✅ Task 2: Data Version Control (DVC) 
 
**Objective:** Establish reproducible data pipeline for audit compliance 
 
**Deliverables:** 
- DVC initialization with Google Drive remote storage 
- Raw data tracking: `data/insurance_data.csv` 
- Data cleaning pipeline: `src/clean_data.py` 
- Version 2 with engineered features 
 
**Reproduce the pipeline:** 
```bash 
dvc pull 
dvc repro 
``` 
 
### ✅ Task 3: A/B Hypothesis Testing 
 
**Objective:** Statistically validate risk drivers for pricing strategy 
 
**Hypotheses Tested (α = 0.05):** 
 
 
### ✅ Task 4: Statistical Modeling 
 
**Objective:** Build predictive models for risk-based pricing 
 
**Claim Severity Model (Random Forest):** 
- RMSE: R[Value] 
- R² Score: [Value] 
 
**Claim Frequency Model (Random Forest):** 
- Accuracy: [Value] 
- F1 Score: [Value] 
 
**Risk-Based Pricing Formula:** 
```python 
Premium = P(claim) × Expected Severity × (1 + Expense Loading + Profit Margin) 
# Where: Expense Loading = 15%%, Profit Margin = 10%% 
``` 
 
--- 
 
## 🚀 Getting Started 
 
### Prerequisites 
 
```bash 
Python 3.10+ 
pip install -r requirements.txt 
``` 
 
### Installation 
 
```bash 
git clone https://github.com/nardos-tsige/insurance-risk-analytics.git 
cd insurance-risk-analytics 
pip install -r requirements.txt 
dvc pull 
``` 
 
### Run the Complete Pipeline 
 
```bash 
# Reproduce data pipeline 
dvc repro 
 
# Run hypothesis tests 
python src/hypothesis_tests.py 
 
# Train models 
python src/modeling.py 
``` 
 
--- 
 
## 📈 Business Recommendations 
 
1. **Geographic Pricing** - Implement province-based premium adjustments (variance of [Value]%) 
2. **Vehicle Segmentation** - Create vehicle-type specific pricing tiers 
3. **Dynamic Pricing Engine** - Deploy risk-based formula with quarterly retraining 
4. **Marketing Optimization** - Target low-risk segments for customer acquisition 
 
--- 
 
## 🛠️ Technologies Used 
 
 
--- 
 
## 📝 Branch Structure 
 
 
--- 
 
## 👥 Contributors 
 
- **Nardos Tsige** - Data Analytics Engineer 
 
--- 
 
## 📄 License 
 
This project is licensed under the MIT License. 
 
--- 
 
## 🙏 Acknowledgments 
 
- AlphaCare Insurance Solutions for the business challenge 
- 10 Academy for the structured learning path 
- Open-source community for amazing tools 
 
--- 
 
[⬆ Back to Top](#-alphacare-insurance-solutions---risk-analytics-platform) 
