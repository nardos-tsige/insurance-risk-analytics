# AlphaCare Insurance Solutions - Interim Report 
 
## Project Overview 
**Project:** Insurance Risk Analytics & Predictive Modeling 
**Date:** May 2026 
**Analyst:** Data Analytics Team 
 
## Business Understanding 
AlphaCare Insurance Solutions (ACIS) needs evidence-driven strategies to optimize marketing investments and refine pricing models for the South African auto-insurance market. 
 
## Data Overview 
- **Time Period:** 18 months (Feb 2014 - Aug 2015) 
- **Total Policies:** [To be filled from EDA] 
- **Key Metrics:** Premium, Claims, Loss Ratio, Margin 
 
## Task 1: Exploratory Data Analysis - COMPLETED 
 
### Key Findings 
1. **Overall Loss Ratio:** [Value]% 
2. **Claim Frequency:** [Value]% of policies have claims 
3. **Geographic Variation:** Significant differences across provinces 
4. **Vehicle Type Impact:** Certain vehicle types show higher risk 
5. **Temporal Trends:** Claim frequency [increased/decreased] over the period 
 
### Data Quality Assessment 
- Missing values handled using median/mode imputation 
- Outliers capped at 99th percentile for TotalClaims 
- Derived metrics created: LossRatio, Margin, HasClaim 
 
## Task 2: Data Version Control - COMPLETED 
 
### DVC Implementation 
- DVC initialized with Google Drive remote storage 
- Raw data tracked: `data/insurance_data.csv` 
- Data cleaning pipeline created: `src/clean_data.py` 
- Two versions available: cleaned data and engineered features 
 
### Reproducibility 
```bash 
dvc pull 
dvc repro 
``` 
 
## Next Steps 
1. Complete Task 3: A/B Hypothesis Testing 
2. Complete Task 4: Statistical Modeling 
3. Deliver final report with recommendations 
 
## Risks and Challenges 
- Data limited to 18 months - may not capture long-term trends 
- External factors (economy, weather) not included 
- Need for regular model retraining 
 
--- 
*Interim Report Submitted: May 2026* 
