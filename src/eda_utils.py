# src/eda_utils.py - FIXED VERSION
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_loss_ratio(df):
    """Calculate loss ratio and margin"""
    try:
        if df is None or df.empty:
            raise ValueError("DataFrame is empty or None")
        
        df_copy = df.copy()
        df_copy['LossRatio'] = np.where(
            df_copy['TotalPremium'] > 0,
            df_copy['TotalClaims'] / df_copy['TotalPremium'],
            np.nan
        )
        df_copy['Margin'] = df_copy['TotalPremium'] - df_copy['TotalClaims']
        df_copy['HasClaim'] = (df_copy['TotalClaims'] > 0).astype(int)
        return df_copy
    except Exception as e:
        print(f"Error in calculate_loss_ratio: {e}")
        return df

def plot_loss_ratio_by_province(df):
    """Plot loss ratio by province"""
    try:
        if df is None or df.empty:
            raise ValueError("DataFrame is empty")
        
        if 'Province' not in df.columns or 'LossRatio' not in df.columns:
            raise KeyError("Required columns missing")
        
        loss_by_province = df.groupby('Province')['LossRatio'].mean().sort_values(ascending=False)
        
        plt.figure(figsize=(12, 6))
        colors = ['red' if x > df['LossRatio'].mean() else 'green' for x in loss_by_province.values]
        loss_by_province.plot(kind='bar', color=colors, edgecolor='black')
        plt.axhline(y=df['LossRatio'].mean(), color='blue', linestyle='--', 
                    label=f'Overall Avg: {df["LossRatio"].mean():.3f}')
        plt.title('Loss Ratio by Province')
        plt.xlabel('Province')
        plt.ylabel('Loss Ratio')
        plt.legend()
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        return plt.gcf()
    except Exception as e:
        print(f"Error in plot_loss_ratio_by_province: {e}")
        return None