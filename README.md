# Amazon Berlin Jobs — Data Analytics Portfolio Project

A GitHub-ready portfolio project exploring job-market analytics for Amazon roles associated with Berlin, Germany. Includes a Streamlit dashboard, reproducible Python analysis, synthetic demonstration data, and a separately documented snapshot of public Amazon.jobs search counts.

> **Data integrity notice:** The 520 row-level records in `data/amazon_berlin_jobs_synthetic.csv` are synthetic. They are NOT scraped or verified Amazon vacancies. Never describe sample role/skill counts as actual Amazon hiring trends. Official search counts are isolated in `data/official_source_snapshot.csv` and are dated dynamic website filter counts.

## Goals
- Explore role categories and teams associated with Amazon Berlin.
- Demonstrate skill-frequency analysis and employment-type segmentation.
- Build a filterable dashboard.
- Separate official public-source context from generated sample rows.

## Stack
Python · Pandas · NumPy · Plotly · Streamlit · EDA · Data Visualization

## Structure
```text
amazon-berlin-jobs-analytics/
├── app.py
├── data/
│   ├── amazon_berlin_jobs_synthetic.csv
│   ├── official_source_snapshot.csv
│   └── DATA_DICTIONARY.md
├── src/analysis.py
├── tests/test_data.py
├── reports/ANALYSIS_NOTES.md
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Run locally
Python 3.10+ recommended.
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
Run analysis and checks:
```bash
python src/analysis.py
python tests/test_data.py
```

## Publish
1. Create a public GitHub repository named `amazon-berlin-jobs-analytics`.
2. Extract this ZIP and upload the **contents** of the project folder.
3. Commit files to `main`.
4. Visit https://share.streamlit.io/ and sign in with GitHub.
5. Create an app, select your repository and `main` branch, set main file path to `app.py`, then deploy.
6. Add the resulting dashboard URL here.

## Public sources
- [Amazon.jobs — Berlin location page](https://www.amazon.jobs/de/location/berlin-Germany): Berlin office context, including Merchant Services, AWS technology teams and corporate support functions.
- [Amazon.jobs — Berlin search results](https://www.amazon.jobs/en/search?country=DEU&invalid_location=false&loc_query=Berlin%2C+Deutschland&region=Berlin): dynamic Berlin search page. On 5 Nov 2026, the result snapshot displayed 146 Berlin listings and 68 AWS team listings. Counts change.
- [Amazon.jobs — Software Development filtered search](https://www.amazon.jobs/en/search?category%5B%5D=software-development&country=DEU&distanceType=Mi&loc_query=Germany&radius=24km&result_limit=10): observed filtered result displayed 21 Berlin Software Development listings. Filters and time affect counts.
- [Example Big Data Processing role](https://amazon.jobs/en-gb/jobs/10531401/software-dev-engineer-big-data-processing-s3-data-and-analytics): public listing discussing big-data processing, data warehouses/data lakes and programming qualifications.

The source snapshot is historical, not a live feed or confirmation a vacancy remains open. Verify roles on Amazon.jobs. This project is independent and not affiliated with Amazon.

## Limitations
- No live scraping is performed.
- No actual vacancy-level Amazon dataset is bundled.
- Synthetic skills and role proportions are illustrative only.
- Salary is omitted because comparable salary data is not consistently available.
- Dashboard charts from the synthetic rows demonstrate methods, not actual recruitment trends.

## License
MIT. See `LICENSE`.
