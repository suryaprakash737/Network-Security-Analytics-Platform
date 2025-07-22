"""
import pandas as pd
import numpy as np
import os

def load_kdd_data(dataset_type="test"):
    """Load KDD Cup 1999 dataset."""
    if dataset_type == "test":
        filepath = "data/raw/kdd_cup_1999/Test_data.csv"
    else:
        filepath = "data/raw/kdd_cup_1999/Train_data.csv"
    
    try:
        data = pd.read_csv(filepath)
        print(f"? Loaded {dataset_type} data: {data.shape}")
        return data
    except Exception as e:
        print(f"? Error loading data: {e}")
        return None

def validate_data_structure(df):
    """Validate basic data structure."""
    validation = {
        'shape': df.shape,
        'columns': len(df.columns),
        'missing_values': df.isnull().sum().sum()
    }
    return validation

# Quick test
if __name__ == "__main__":
    print("? Ingestion module ready!")
