from pathlib import Path
import pandas as pd
p=Path(__file__).resolve().parents[1]/"data"/"amazon_berlin_jobs_synthetic.csv"
df=pd.read_csv(p)
assert len(df)==520
assert df.job_id.is_unique
assert df.isna().sum().sum()==0
assert df.source_type.eq("Synthetic demonstration record").all()
assert df.source_url.eq("").all()
print("Dataset checks passed; every row is explicitly synthetic.")
