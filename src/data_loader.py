# src/data_loader.py - WITH PROPER ERROR HANDLING
import pandas as pd
from pathlib import Path

def load_insurance_data(file_path):
    """Load the insurance dataset with error handling"""
    try:
        if not Path(file_path).exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        data = pd.read_csv(file_path)
        
        if 'TransactionDate' in data.columns:
            data['TransactionDate'] = pd.to_datetime(data['TransactionDate'])
        
        print(f" Loaded {data.shape[0]} rows and {data.shape[1]} columns")
        return data
    
    except FileNotFoundError as e:
        print(f" Error: {e}")
        return None
    except Exception as e:
        print(f" Unexpected error: {e}")
        return None

def get_data_summary(df):
    """Generate data summary with error handling"""
    try:
        if df is None or df.empty:
            raise ValueError("DataFrame is empty or None")
        
        return {
            'shape': df.shape,
            'columns': df.columns.tolist(),
            'missing_values': df.isnull().sum().to_dict(),
            'missing_percentages': (df.isnull().sum() / len(df) * 100).to_dict(),
            'memory_usage_mb': df.memory_usage(deep=True).sum() / 1024**2
        }
    except Exception as e:
        print(f"Error in get_data_summary: {e}")
        return {}