"""EDA for the synthetic Amazon Berlin jobs portfolio dataset."""
from pathlib import Path
import pandas as pd
DATA=Path(__file__).resolve().parents[1]/"data"/"amazon_berlin_jobs_synthetic.csv"
def main():
    df=pd.read_csv(DATA,parse_dates=["posted_date"])
    print(f"Rows: {len(df)} | Columns: {len(df.columns)}")
    print("Duplicate IDs:",df.job_id.duplicated().sum())
    print("Missing values:\n",df.isna().sum().to_string())
    print("\nSample records by category:\n",df.category.value_counts().to_string())
    print("\nSample records by team:\n",df.team.value_counts().to_string())
    print("\nSample employment type:\n",df.employment_type.value_counts().to_string())
    skills=df.skills.fillna("").str.split("; ").explode()
    print("\nTop skills in synthetic sample:\n",skills[skills.ne("")].value_counts().head(15).to_string())
    print("\nThese counts describe synthetic sample records, not real Amazon hiring data.")
if __name__=="__main__": main()
