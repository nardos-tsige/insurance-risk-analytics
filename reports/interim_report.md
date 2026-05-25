# AlphaCare Insurance Solutions - Interim Report

**Project:** Insurance Risk Analytics & Predictive Modeling  
**Date:** May 25, 2026  
**Analyst:** Nardos Tsige  
**Status:** Tasks 1 & 2 Complete | Tasks 3 & 4 In Progress

---

## 1. Executive Summary

This report summarizes progress on the AlphaCare Insurance Solutions (ACIS) risk analytics project. We have completed Exploratory Data Analysis (EDA) and Data Version Control (DVC) setup.

**Key Findings:**
- **Overall Loss Ratio:** 44.3% (85.4% of policies are profitable)
- **Best Province:** Amhara (32% loss ratio)
- **Worst Province:** Addis Ababa (78% loss ratio)
- **Best Vehicle Type:** Sedan (35% loss ratio)
- **Worst Vehicle Type:** Luxury (80% loss ratio)
- **Claim Frequency Trend:** Increased from 14% to 30% over 18 months

---

## 2. Anchor Metrics Definition

Two core metrics anchor this analysis:

| Metric | Formula | Business Meaning |
|--------|---------|------------------|
| **Loss Ratio** | TotalClaims / TotalPremium | Percentage of premiums paid out as claims. Lower is better. |
| **Margin** | TotalPremium - TotalClaims | Profit per policy before expenses. Higher is better. |

**Target:** Loss Ratio < 100% (profitable portfolio)
**Current:** Loss Ratio = 44.3% (healthy profitability)

---

## 3. Data Overview

### 3.1 Dataset Description

| Aspect | Details |
|--------|---------|
| **Time Period** | 18 months (Feb 2014 - Aug 2015) |
| **Total Policies** | 10,000 |
| **Total Features** | 24 columns |
| **Target Variable** | TotalClaims, HasClaim |

### 3.2 Data Quality Assessment

| Column | Missing Count | Missing % | Handling Strategy |
|--------|--------------|-----------|-------------------|
| CustomValueEstimate | 0 | 0% | No action needed |
| VehicleType | 0 | 0% | No action needed |
| Gender | 0 | 0% | No action needed |
| Province | 0 | 0% | No action needed |
| TotalPremium | 0 | 0% | No action needed |
| TotalClaims | 0 | 0% | No action needed |

**No missing values found** - dataset is clean.

### 3.3 Descriptive Statistics

| Variable | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|----------|-------|------|-----|-----|-----|-----|-----|-----|
| TotalPremium | 10,000 | 2,488 | 736 | 951 | 2,028 | 2,307 | 2,676 | 5,105 |
| TotalClaims | 10,000 | 1,314 | 3,922 | 0 | 0 | 0 | 0 | 49,623 |
| CustomValueEstimate | 10,000 | 35,641 | 22,354 | 5,022 | 21,443 | 28,522 | 46,721 | 134,914 |

### 3.4 Outlier Analysis

| Variable | Outliers (>99th percentile) | Treatment |
|----------|----------------------------|-----------|
| TotalClaims | 100 rows (1%) | Capped at 49,623 |
| TotalPremium | 100 rows (1%) | Retained for analysis |
| CustomValueEstimate | 100 rows (1%) | Retained for analysis |

---

## 4. Task 1: Exploratory Data Analysis (COMPLETE)

### 4.1 Portfolio Performance

| Metric | Value |
|--------|-------|
| Total Premium Collected | R24,881,300 |
| Total Claims Paid | R13,141,900 |
| Overall Loss Ratio | **44.3%** |
| Profitable Policies | **85.4%** (Loss Ratio < 1) |
| Claim Frequency | 15.2% |

### 4.2 Loss Ratio by Province

![Loss Ratio by Province](images/loss_ratio_by_province.png)

*Figure 1: Loss ratio varies significantly by province.*

| Province | Loss Ratio | Risk Level | Recommended Action |
|----------|------------|------------|-------------------|
| Amhara | 32% | 🟢 Lowest | Reduce premium 20% |
| Tigray | 38% | 🟢 Low | Reduce premium 15% |
| Oromia | 38% | 🟢 Low | Reduce premium 10% |
| Addis Ababa | 78% | 🔴 Highest | Increase premium 25% |

### 4.3 Loss Ratio by Vehicle Type

![Loss Ratio by Vehicle Type](images/loss_ratio_by_vehicle.png)

*Figure 2: Loss ratio varies significantly by vehicle type.*

| Vehicle Type | Loss Ratio | Risk Level |
|--------------|------------|------------|
| Luxury | 80% | 🔴 High |
| SUV | 50% | 🟡 Medium |
| Hatchback | 38% | 🟢 Low |
| Sedan | 35% | 🟢 Lowest |

### 4.4 Loss Ratio by Gender

| Gender | Loss Ratio | Claim Frequency |
|--------|------------|-----------------|
| Female | 45% | 15% |
| Male | 44% | 15% |

**Insight:** Minimal difference between genders - no gender-based pricing needed.

### 4.5 Loss Ratio Distribution

![Loss Ratio Distribution](images/loss_ratio_distribution.png)

*Figure 3: Distribution of loss ratio across all policies.*

**Key Observations:**
- 85.4% of policies have loss ratio below 1.0 (profitable)
- Mean loss ratio: 0.443
- Median loss ratio: 0.0 (most policies have zero claims)
- Long tail of unprofitable policies (14.6%)

### 4.6 Claim Frequency Trend

![Claim Frequency Trend](images/claim_frequency_trend.png)

*Figure 4: Claim frequency trend over the 18-month observation period.*

| Period | Claim Frequency | Loss Ratio |
|--------|-----------------|------------|
| First 6 months | 14-16% | 0.52-0.50 |
| Last 6 months | 27-30% | 0.39-0.36 |

**Critical Finding:** Claim frequency DOUBLED from 14% to 30% over 18 months.

### 4.7 Correlation Analysis

| Feature | Correlation with Loss Ratio | Interpretation |
|---------|---------------------------|----------------|
| Past Claims | 0.96 | Very Strong positive |
| Risk Score | 0.30 | Moderate positive |
| TotalPremium | 0.23 | Weak positive |
| Age | -0.21 | Weak negative |

**Insight:** Past claims is the strongest predictor of future claims.

---

## 5. Task 2: Data Version Control (COMPLETE)

### 5.1 Why DVC Matters for Insurance

| Requirement | How DVC Addresses It |
|-------------|---------------------|
| **Regulatory audits** | Every data version is tracked and reproducible |
| **Model validation** | Exact data used for training is versioned |
| **Compliance** | Audit trail of all data transformations |
| **Reproducibility** | Any analyst can recreate the exact dataset |

### 5.2 DVC Implementation

| Component | Status |
|-----------|--------|
| DVC Initialization | ✅ Complete |
| Remote Storage (Google Drive) | ✅ Configured |
| Raw Data Tracking | ✅ `data/insurance_data.csv` |
| Cleaning Pipeline | ✅ `src/clean_data.py` |
| Engineered Features (v2) | ✅ `data/insurance_data_v2.csv` |

### 5.3 Reproducibility Commands

```bash
dvc pull
dvc repro

6. Task 3: A/B Hypothesis Testing (IN PROGRESS)
6.1 Hypotheses to Test
Hypothesis	KPI	Statistical Test	Significance Level
H₀: No province risk differences	Loss Ratio	ANOVA	α = 0.05
H₀: No gender risk differences	Loss Ratio	Independent t-test	α = 0.05
H₀: No vehicle type differences	Claim Frequency	Chi-square	α = 0.05
H₀: No zip code margin differences	Margin	ANOVA	α = 0.05
6.2 Expected Outcomes
Hypothesis	Expected Result	Business Action
Province	Reject H₀ (p < 0.05)	Implement province-based pricing
Gender	Fail to reject (p > 0.05)	No gender-based pricing
Vehicle Type	Reject H₀ (p < 0.05)	Create vehicle-type pricing tiers
Zip Code	Reject H₀ (p < 0.05)	Implement zip-code based tiers
7. Task 4: Statistical Modeling (PLANNED)
7.1 Model Specifications
Model Type	Target Variable	Algorithms	Evaluation Metrics
Severity Model	TotalClaims (where >0)	Linear Regression, Random Forest, XGBoost	RMSE, R²
Frequency Model	HasClaim (0/1)	Logistic Regression, Random Forest, XGBoost	Accuracy, Precision, Recall, F1
7.2 Risk-Based Pricing Formula
text
Premium = P(claim) × Expected Severity × (1 + Expense Loading + Profit Margin)

Where:
- P(claim) = Predicted probability from frequency model
- Expected Severity = Predicted claim amount from severity model
- Expense Loading = 15% (operating costs)
- Profit Margin = 10% (target profit)
7.3 Model Interpretability
Method: SHAP (SHapley Additive exPlanations)

Why SHAP:

Provides consistent feature importance rankings

Shows direction of impact (positive/negative)

Compliant with regulatory explainability requirements

8. Next Steps Timeline
Task	Start	End	Status
Task 3: Hypothesis Testing	May 24	May 25	In Progress
Task 4: Modeling	May 25	May 26	Planned
Final Report	May 26	May 26	Planned
9. Risks and Limitations
Risk	Impact	Mitigation
Only 18 months of data	Medium	Acknowledge in final report
Claim frequency increasing	High	Quarterly model retraining
Outliers in TotalClaims	Low	Capped at 99th percentile
External factors missing	Medium	Recommend additional data sources
10. Conclusion
Tasks 1 and 2 are complete with excellent results. Key findings show:

Amhara (32%) and Sedans (35%) are lowest risk - target for premium reduction

Addis Ababa (78%) and Luxury vehicles (80%) are highest risk - require repricing

85.4% of policies are profitable - portfolio is healthy

Claim frequency doubled - requires ongoing monitoring

Task 3 will use ANOVA, t-test, and Chi-square to validate these findings statistically. Task 4 will build Random Forest and XGBoost models with SHAP interpretability.

Prepared by: Nardos Tsige
Date: May 25, 2026
Next Update: Final Report - May 26, 2026