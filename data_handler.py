import pandas as pd

def load_balance_sheet(file_path):
    df = pd.read_excel(file_path)
    return df

def summarize_balance(df):
    total_assets = df['Assets'].sum()
    total_liabilities = df['Liabilities'].sum()
    total_equity = df['Equity'].sum()
    return {
        'Total Assets': total_assets,
        'Total Liabilities': total_liabilities,
        'Total Equity': total_equity
    }
