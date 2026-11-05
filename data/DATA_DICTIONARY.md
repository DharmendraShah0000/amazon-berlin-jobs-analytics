# Data dictionary

`amazon_berlin_jobs_synthetic.csv` contains only synthetic demo records.

| Field | Meaning |
|---|---|
| job_id | Synthetic ID, not an Amazon requisition ID |
| title | Illustrative job title |
| category | Broad job family |
| team | Illustrative team label |
| location | Sample location label |
| posted_date | Simulated posting date |
| employment_type | Simulated employment type |
| experience_level / experience_band | Simulated seniority |
| german_language | Simulated language indicator; not verified |
| skills | Semicolon-separated illustrative skills |
| source_type | Provenance label |
| source_url | Blank for synthetic rows |

`official_source_snapshot.csv` stores separately observed public search-page counts with date, URL and caveat.
