# Task_04_Descriptive_Stats

## Overview
This project summarizes a dataset of 2024 US Presidential election social media activity using:
- Pure Python (no libraries)
- Pandas
- Polars

Each approach outputs descriptive statistics such as count, mean, min/max, standard deviation, unique values, and most common values.

## Scripts

| Script              | Description                                 |
|---------------------|---------------------------------------------|
| `pure_python_stats.py` | Uses base Python to compute stats |
| `pandas_stats.py`      | Uses Pandas to compute and group stats       |
| `polars_stats.py`      | Uses Polars for fast grouped statistics      |

## Dataset

I used the following dataset:
📁 `2024_fb_posts_president_scored_anon.csv`

📎 Dataset Link   
https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing


## How to Run

```bash
# Run with pure Python
python scripts/pure_python_stats.py

# Run with pandas
pip install pandas
python scripts/pandas_stats.py

# Run with polars
pip install polars
python scripts/polars_stats.py
