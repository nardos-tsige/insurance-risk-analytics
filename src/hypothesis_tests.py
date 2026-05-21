\"\"\"Statistical hypothesis testing for insurance risk analysis\"\""
 
import pandas as pd 
import numpy as np 
from scipy.stats import f_oneway, ttest_ind, chi2_contingency 
 
def test_province_risk_differences(df): 
    \"\"\"H0: No risk differences across provinces\"\"\" 
    groups = [df[df['Province'] == p]['LossRatio'].dropna() for p in df['Province'].unique()] 
    groups = [g for g in groups if len(g) 
    if len(groups) 
        f_stat, p_value = f_oneway(*groups) 
        return {'hypothesis': 'No province risk differences', 'p_value': p_value, 'reject_null': reject_null} 
    return None 
 
def test_gender_risk_difference(df): 
    \"\"\"H0: No risk difference between genders\"\"\" 
    male = df[df['Gender'] == 'Male']['LossRatio'].dropna() 
    female = df[df['Gender'] == 'Female']['LossRatio'].dropna() 
    t_stat, p_value = ttest_ind(male, female) 
    return {'hypothesis': 'No gender risk difference', 'p_value': p_value, 'reject_null': reject_null, 'male_mean': male.mean(), 'female_mean': female.mean()} 
 
def test_vehicle_type_risk(df): 
    \"\"\"H0: No risk difference between vehicle types\"\"\" 
    contingency = pd.crosstab(df['VehicleType'], df['HasClaim']) 
    chi2, p_value, dof, expected = chi2_contingency(contingency) 
    return {'hypothesis': 'No vehicle type risk difference', 'p_value': p_value, 'reject_null': reject_null} 
 
def run_all_tests(df): 
    \"\"\"Run all hypothesis tests and return results\"\"\" 
    results = [] 
    results.append(test_province_risk_differences(df)) 
    results.append(test_gender_risk_difference(df)) 
    results.append(test_vehicle_type_risk(df)) 
    return pd.DataFrame([r for r in results if r is not None]) 
