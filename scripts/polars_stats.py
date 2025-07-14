# polars_stats.py
# Use polars to compute descriptive statistics

import polars as pl

def summarize_with_polars(file_path: str, group_by: str = None):
    df = pl.read_csv(file_path)
    print(f"Loaded {df.shape[0]} rows from {file_path}\n")

    # Overall summary
    print("=== Overall Descriptive Stats ===")
    print(df.describe())

    # Categorical stats
    print("\n=== Categorical Columns: Unique Counts & Top Values ===")
    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            unique_count = df[col].n_unique()
            most_common = df.group_by(col).len().sort("len", descending=True).head(1)
            print(f"\nColumn: {col}")
            print(f"  Unique Values: {unique_count}")
            print(f"  Most Common: {most_common}")

    # Grouped summary
    if group_by:
        print(f"\n=== Grouped Descriptive Stats by {group_by} ===")
        grouped = df.group_by(group_by).agg([
            pl.count(),
            *[pl.col(c).mean().alias(f"{c}_mean") for c in df.columns if df[c].dtype in [pl.Int64, pl.Float64]]
        ])
        print(grouped)

if __name__ == "__main__":
    summarize_with_polars("../data/2024_fb_posts_president_scored_anon.csv", group_by="Facebook_Id")