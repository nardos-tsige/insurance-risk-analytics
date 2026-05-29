"""
Hypothesis Testing Module for Insurance Risk Analytics

This module contains statistical tests for validating risk drivers:
- Province risk differences (ANOVA)
- Gender risk differences (T-test)
- Vehicle type risk differences (Chi-square)
- Zip code margin differences (ANOVA)
"""

import pandas as pd
import numpy as np
from scipy.stats import f_oneway, ttest_ind, chi2_contingency


def test_province_risk(df):
    """
    Test H0: No risk differences across provinces
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with 'Province' and 'LossRatio' columns
    
    Returns:
    --------
    dict
        Test results with p-value and decision
    """
    try:
        # Input validation
        if df is None or df.empty:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'DataFrame is empty'}
        
        if 'Province' not in df.columns or 'LossRatio' not in df.columns:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'Missing required columns'}
        
        # Create groups for each province
        groups = [df[df['Province'] == p]['LossRatio'].dropna() for p in df['Province'].unique()]
        groups = [g for g in groups if len(g) > 0]
        
        # Check if we have enough groups
        if len(groups) < 2:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'Insufficient groups'}
        
        # Perform ANOVA
        f_stat, p_value = f_oneway(*groups)
        
        return {
            'test': 'ANOVA',
            'p_value': round(p_value, 6),
            'significant': p_value < 0.05,
            'test_statistic': round(f_stat, 4),
            'interpretation': f"There {'is' if p_value < 0.05 else 'is not'} significant risk variation across provinces"
        }
    
    except Exception as e:
        return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': str(e)}


def test_gender_risk(df):
    """
    Test H0: No risk difference between genders
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with 'Gender' and 'LossRatio' columns
    
    Returns:
    --------
    dict
        Test results with p-value and decision
    """
    try:
        # Input validation
        if df is None or df.empty:
            return {'test': 'T-test', 'p_value': 1.0, 'significant': False, 'error': 'DataFrame is empty'}
        
        if 'Gender' not in df.columns or 'LossRatio' not in df.columns:
            return {'test': 'T-test', 'p_value': 1.0, 'significant': False, 'error': 'Missing required columns'}
        
        # Separate by gender
        male = df[df['Gender'] == 'Male']['LossRatio'].dropna()
        female = df[df['Gender'] == 'Female']['LossRatio'].dropna()
        
        # Check if we have data for both groups
        if len(male) == 0 or len(female) == 0:
            return {'test': 'T-test', 'p_value': 1.0, 'significant': False, 'error': 'One or both gender groups empty'}
        
        # Perform t-test
        t_stat, p_value = ttest_ind(male, female)
        
        return {
            'test': 'T-test',
            'p_value': round(p_value, 6),
            'significant': p_value < 0.05,
            'test_statistic': round(t_stat, 4),
            'male_mean': round(male.mean(), 4),
            'female_mean': round(female.mean(), 4),
            'interpretation': f"There {'is' if p_value < 0.05 else 'is not'} a significant risk difference between genders"
        }
    
    except Exception as e:
        return {'test': 'T-test', 'p_value': 1.0, 'significant': False, 'error': str(e)}


def test_vehicle_risk(df):
    """
    Test H0: No risk difference between vehicle types
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with 'VehicleType' and 'HasClaim' columns
    
    Returns:
    --------
    dict
        Test results with p-value and decision
    """
    try:
        # Input validation
        if df is None or df.empty:
            return {'test': 'Chi-square', 'p_value': 1.0, 'significant': False, 'error': 'DataFrame is empty'}
        
        if 'VehicleType' not in df.columns or 'HasClaim' not in df.columns:
            return {'test': 'Chi-square', 'p_value': 1.0, 'significant': False, 'error': 'Missing required columns'}
        
        # Create contingency table
        contingency = pd.crosstab(df['VehicleType'], df['HasClaim'])
        
        # Check if table is valid
        if contingency.shape[0] < 2 or contingency.shape[1] < 2:
            return {'test': 'Chi-square', 'p_value': 1.0, 'significant': False, 'error': 'Contingency table too small'}
        
        # Perform Chi-square test
        chi2, p_value, dof, expected = chi2_contingency(contingency)
        
        return {
            'test': 'Chi-square',
            'p_value': round(p_value, 6),
            'significant': p_value < 0.05,
            'test_statistic': round(chi2, 4),
            'degrees_freedom': dof,
            'interpretation': f"There {'is' if p_value < 0.05 else 'is not'} a significant risk difference across vehicle types"
        }
    
    except Exception as e:
        return {'test': 'Chi-square', 'p_value': 1.0, 'significant': False, 'error': str(e)}


def test_zipcode_margin(df, top_n=10):
    """
    Test H0: No margin difference between zip codes
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with 'ZipCode' and 'Margin' columns
    top_n : int
        Number of top zip codes to analyze
    
    Returns:
    --------
    dict
        Test results with p-value and decision
    """
    try:
        # Input validation
        if df is None or df.empty:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'DataFrame is empty'}
        
        if 'ZipCode' not in df.columns or 'Margin' not in df.columns:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'Missing required columns'}
        
        # Get top zip codes by count
        top_zips = df['ZipCode'].value_counts().head(top_n).index
        df_top = df[df['ZipCode'].isin(top_zips)]
        
        # Create groups for each zip code
        groups = [df_top[df_top['ZipCode'] == z]['Margin'].dropna() for z in top_zips]
        groups = [g for g in groups if len(g) > 0]
        
        # Check if we have enough groups
        if len(groups) < 2:
            return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': 'Insufficient zip code groups'}
        
        # Perform ANOVA
        f_stat, p_value = f_oneway(*groups)
        
        return {
            'test': 'ANOVA',
            'p_value': round(p_value, 6),
            'significant': p_value < 0.05,
            'test_statistic': round(f_stat, 4),
            'zip_codes_analyzed': len(top_zips),
            'interpretation': f"There {'are' if p_value < 0.05 else 'are not'} significant margin differences across zip codes"
        }
    
    except Exception as e:
        return {'test': 'ANOVA', 'p_value': 1.0, 'significant': False, 'error': str(e)}


def run_all_tests(df):
    """
    Run all hypothesis tests and return results as DataFrame
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with all required columns
    
    Returns:
    --------
    pandas.DataFrame
        Summary of all test results
    """
    results = []
    
    # Run each test
    results.append(test_province_risk(df))
    results.append(test_gender_risk(df))
    results.append(test_vehicle_risk(df))
    results.append(test_zipcode_margin(df))
    
    # Convert to DataFrame
    results_df = pd.DataFrame(results)
    
    # Add recommendation column
    results_df['recommendation'] = results_df.apply(
        lambda row: ' IMPLEMENT' if row.get('significant', False) else ' SKIP',
        axis=1
    )
    
    return results_df


# Example usage
if __name__ == "__main__":
    # Load data
    df = pd.read_csv('data/insurance_data.csv')
    
    # Calculate required columns
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    df['HasClaim'] = (df['TotalClaims'] > 0).astype(int)
    
    # Run all tests
    results = run_all_tests(df)
    
    print("\n" + "="*60)
    print("HYPOTHESIS TESTING RESULTS")
    print("="*60)
    print(results.to_string(index=False))