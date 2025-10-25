import sys
import pandas as pd

def profile_dataset(file_path):
    df = pd.read_csv(file_path)

    print("=== DATASET PROFILER REPORT ===\n")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("\nColumn Data Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nStatistical Summary (Numeric Columns):")
    print(df.describe())
    print("\nDuplicate Rows:", df.duplicated().sum())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python profiler.py <dataset.csv>")
    else:
        profile_dataset(sys.argv[1])
