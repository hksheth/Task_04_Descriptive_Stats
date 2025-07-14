# pandas_stats.py
# Use pandas to compute descriptive statistics

import pandas as pd

def summarize_with_pandas(file_path: str, group_by=None):
    df = pd.read_csv(file_path)
    print(f"Loaded {len(df)} rows from {file_path}\n")

    # Basic summary for entire dataset
    print("=== Overall Descriptive Stats ===")
    print(df.describe(include='all'))

    print("\n=== Categorical Value Counts (Top 5) ===")
    for col in df.select_dtypes(include=['object']).columns:
        print(f"\nColumn: {col}")
        print(df[col].value_counts().head(5))

    # Grouped stats
    if group_by:
        print(f"\n=== Grouped Descriptive Stats by {group_by} ===")
        grouped = df.groupby(group_by)
        summary = grouped.describe().T
        print(summary)

if __name__ == "__main__":
    summarize_with_pandas("../data/2024_fb_posts_president_scored_anon.csv", group_by="Facebook_Id")