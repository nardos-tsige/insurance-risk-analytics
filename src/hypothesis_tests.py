import pandas as pd
import numpy as np
from scipy.stats import f_oneway, ttest_ind, chi2_contingency

def test_province_risk(df):
    '''H0: No risk differences across provinces'''
    try:
        # Input validation
        if df is None or df.empty:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'DataFrame is empty or None'}
        
        if 'Province' not in df.columns or 'LossRatio' not in df.columns:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'Required columns missing: Province or LossRatio'}
        
        groups = [df[df['Province'] == p]['LossRatio'].dropna() for p in df['Province'].unique()]
        groups = [g for g in groups if len(g) > 0]
        
        if len(groups) < 2:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'Insufficient groups for comparison'}
        
        f_stat, p_value = f_oneway(*groups)
        return {'test': 'ANOVA', 'p_value': round(p_value, 6), 'significant': p_value < 0.05}
    
    except Exception as e:
        return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': str(e)}

def test_gender_risk(df):
    '''H0: No risk difference between genders'''
    try:
        # Input validation
        if df is None or df.empty:
            return {'test': 'T-test', 'p_value': 1.0, 'significant': False, 'error': 'DataFrame is empty or None'}
        
        if 'Gender' not in df.columns or 'LossRatio' not in df.columns:
            return {'test': 'T-test', 'p_value': 1.0, 'significant': False, 'error': 'Required columns missing: Gender or LossRatio'}
        
        male = df[df['Gender'] == 'Male']['LossRatio'].dropna()
        female = df[df['Gender'] == 'Female']['LossRatio'].dropna()
        
        if len(male) == 0 or len(female) == 0:
            return {'test': 'T-test', 'p_value': 1.0, 'significant': False, 'error': 'One or both gender groups are empty'}
        
        t_stat, p_value = ttest_ind(male, female)
        return {
            'test': 'T-test', 
            'p_value': round(p_value, 6), 
            'significant': p_value < 0.05,
            'male_mean': round(male.mean(), 4), 
            'female_mean': round(female.mean(), 4)
        }
    
    except Exception as e:
        return {'test': 'T-test', 'p_value': 1.0, 'significant': False, 'error': str(e)}

def test_vehicle_risk(df):
    '''H0: No risk difference between vehicle types'''
    try:
        # Input validation
        if df is None or df.empty:
            return {'test': 'Chi-square', 'p_value': 1.0, 'significant': False, 'error': 'DataFrame is empty or None'}
        
        if 'VehicleType' not in df.columns or 'HasClaim' not in df.columns:
            return {'test': 'Chi-square', 'p_value': 1.0, 'significant': False, 'error': 'Required columns missing: VehicleType or HasClaim'}
        
        contingency = pd.crosstab(df['VehicleType'], df['HasClaim'])
        
        if contingency.shape[0] < 2 or contingency.shape[1] < 2:
            return {'test': 'Chi-square', 'p_value': 1.0, 'significant': False, 'error': 'Contingency table too small for valid test'}
        
        chi2, p_value, dof, expected = chi2_contingency(contingency)
        return {'test': 'Chi-square', 'p_value': round(p_value, 6), 'significant': p_value < 0.05}
    
    except Exception as e:
        return {'test': 'Chi-square', 'p_value': 1.0, 'significant': False, 'error': str(e)}

def test_zipcode_margin_differences(df, top_n=10):
    '''H0: No margin difference between zip codes'''
    try:
        # Input validation
        if df is None or df.empty:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'DataFrame is empty or None'}
        
        if 'ZipCode' not in df.columns or 'Margin' not in df.columns:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'Required columns missing: ZipCode or Margin'}
        
        top_zips = df['ZipCode'].value_counts().head(top_n).index
        df_top = df[df['ZipCode'].isin(top_zips)]
        
        groups = [df_top[df_top['ZipCode'] == z]['Margin'].dropna() for z in top_zips]
        groups = [g for g in groups if len(g) > 0]
        
        if len(groups) < 2:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'Insufficient zip codes for comparison'}
        
        f_stat, p_value = f_oneway(*groups)
        return {'test': 'ANOVA', 'p_value': round(p_value, 6), 'significant': p_value < 0.05}
    
    except Exception as e:
        return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': str(e)}

def run_all_tests(df):
    '''Run all hypothesis tests with comprehensive error handling'''
    results = []
    
    # Run each test and catch any issues
    results.append(test_province_risk(df))
    results.append(test_gender_risk(df))
    results.append(test_vehicle_risk(df))
    results.append(test_zipcode_margin_differences(df))
    
    # Convert to DataFrame
    results_df = pd.DataFrame(results)
    
    # Add summary column for easy reading
    results_df['interpretation'] = results_df.apply(
        lambda row: f"Reject H0: {row['significant']} (p={row['p_value']})", axis=1
    )
    
    return results_df

if __name__ == "__main__":
    # Test the module
    print("Testing hypothesis_tests module...")
    print("All functions defined successfully!")