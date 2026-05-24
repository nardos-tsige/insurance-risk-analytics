import pandas as pd
import numpy as np
from scipy.stats import f_oneway, ttest_ind, chi2_contingency

def test_province_risk(df):
    '''H0: No risk differences across provinces'''
    try:
        # Input validation
        if df is None or df.empty:
            raise ValueError("DataFrame is empty or None")
        
        if 'Province' not in df.columns or 'LossRatio' not in df.columns:
            raise KeyError("Required columns 'Province' or 'LossRatio' missing")
        
        groups = [df[df['Province']==p]['LossRatio'].dropna() for p in df['Province'].unique()]
        groups = [g for g in groups if len(g) > 0]
        
        if len(groups) < 2:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'Insufficient groups for comparison'}
        
        f_stat, p_value = f_oneway(*groups)
        return {'test': 'ANOVA', 'p_value': p_value, 'significant': p_value < 0.05}
    
    except Exception as e:
        return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': str(e)}

def test_gender_risk(df):
    '''H0: No risk difference between genders'''
    try:
        # Input validation
        if df is None or df.empty:
            raise ValueError("DataFrame is empty or None")
        
        if 'Gender' not in df.columns or 'LossRatio' not in df.columns:
            raise KeyError("Required columns 'Gender' or 'LossRatio' missing")
        
        male = df[df['Gender']=='Male']['LossRatio'].dropna()
        female = df[df['Gender']=='Female']['LossRatio'].dropna()
        
        if len(male) == 0 or len(female) == 0:
            return {'test': 'T-test', 'p_value': 1.0, 'significant': False, 'error': 'One or both gender groups empty'}
        
        t_stat, p_value = ttest_ind(male, female)
        return {
            'test': 'T-test', 
            'p_value': p_value, 
            'significant': p_value < 0.05,
            'male_mean': male.mean(), 
            'female_mean': female.mean()
        }
    
    except Exception as e:
        return {'test': 'T-test', 'p_value': 1.0, 'significant': False, 'error': str(e)}

def test_vehicle_risk(df):
    '''H0: No risk difference between vehicle types'''
    try:
        # Input validation
        if df is None or df.empty:
            raise ValueError("DataFrame is empty or None")
        
        if 'VehicleType' not in df.columns or 'HasClaim' not in df.columns:
            raise KeyError("Required columns 'VehicleType' or 'HasClaim' missing")
        
        contingency = pd.crosstab(df['VehicleType'], df['HasClaim'])
        
        if contingency.shape[0] < 2 or contingency.shape[1] < 2:
            return {'test': 'Chi-square', 'p_value': 1.0, 'significant': False, 'error': 'Contingency table too small'}
        
        chi2, p_value, dof, expected = chi2_contingency(contingency)
        return {'test': 'Chi-square', 'p_value': p_value, 'significant': p_value < 0.05}
    
    except Exception as e:
        return {'test': 'Chi-square', 'p_value': 1.0, 'significant': False, 'error': str(e)}

def run_all_tests(df):
    '''Run all hypothesis tests with error handling'''
    results = []
    results.append(test_province_risk(df))
    results.append(test_gender_risk(df))
    results.append(test_vehicle_risk(df))
    return pd.DataFrame(results)