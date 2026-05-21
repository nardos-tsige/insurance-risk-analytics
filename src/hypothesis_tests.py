import pandas as pd 
import numpy as np 
from scipy.stats import f_oneway, ttest_ind, chi2_contingency 
 
def test_province_risk(df): 
    '''H0: No risk differences across provinces''' 
    groups = [df[df['Province']==p]['LossRatio'].dropna() for p in df['Province'].unique()] 
    groups = [g for g in groups if len(g) 
    if len(groups) 
        f_stat, p_value = f_oneway(*groups) 
    return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False} 
 
def test_gender_risk(df): 
    '''H0: No risk difference between genders''' 
    male = df[df['Gender']=='Male']['LossRatio'].dropna() 
    female = df[df['Gender']=='Female']['LossRatio'].dropna() 
    t_stat, p_value = ttest_ind(male, female) 
 
def test_vehicle_risk(df): 
    '''H0: No risk difference between vehicle types''' 
    contingency = pd.crosstab(df['VehicleType'], df['HasClaim']) 
    chi2, p_value, dof, expected = chi2_contingency(contingency) 
 
def run_all_tests(df): 
    results = [] 
    results.append(test_province_risk(df)) 
    results.append(test_gender_risk(df)) 
    results.append(test_vehicle_risk(df)) 
    return pd.DataFrame(results) 
