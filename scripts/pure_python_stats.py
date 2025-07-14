# pure_python_stats.py
# A base Python script to compute descriptive statistics without Pandas or Polars

import csv
import math
from collections import defaultdict, Counter
from statistics import mean, stdev
from typing import List, Dict, Tuple
import os

def is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False

def detect_column_types(rows: List[Dict[str, str]]) -> Dict[str, str]:
    types = {}
    for column in rows[0]:
        sample_values = [row[column] for row in rows if row[column] not in ('', 'NA', 'N/A')]
        numeric_count = sum(is_float(v) for v in sample_values[:50])
        types[column] = 'numeric' if numeric_count > 0.9 * len(sample_values[:50]) else 'categorical'
    return types

def compute_numeric_stats(values: List[float]) -> Dict[str, float]:
    if not values:
        return {}
    return {
        "count": len(values),
        "mean": mean(values),
        "min": min(values),
        "max": max(values),
        "std": stdev(values) if len(values) > 1 else 0
    }

def compute_categorical_stats(values: List[str]) -> Dict[str, any]:
    if not values:
        return {}
    counter = Counter(values)
    return {
        "count": len(values),
        "unique": len(set(values)),
        "most_common": counter.most_common(1)[0]
    }

def summarize_dataset(file_path: str, group_by: List[str] = None):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]

    print(f"Loaded {len(rows)} rows from {os.path.basename(file_path)}")

    if not rows:
        print("Empty dataset.")
        return

    col_types = detect_column_types(rows)
    grouped_data = defaultdict(list)

    if group_by:
        for row in rows:
            key = tuple(row[col] for col in group_by)
            grouped_data[key].append(row)
    else:
        grouped_data["ALL"] = rows

    for group_key, group_rows in grouped_data.items():
        print(f"\nGroup: {group_key if group_by else 'FULL DATASET'}")
        for col, col_type in col_types.items():
            values = [row[col] for row in group_rows if row[col] not in ('', 'NA', 'N/A')]
            if col_type == 'numeric':
                values = [float(v) for v in values if is_float(v)]
                stats = compute_numeric_stats(values)
            else:
                stats = compute_categorical_stats(values)
            print(f"Column: {col}\n  Type: {col_type}\n  Stats: {stats}")

if __name__ == "__main__":
    summarize_dataset("../data/2024_fb_posts_president_scored_anon.csv", group_by=["Facebook_Id"])