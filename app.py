from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Amazon Berlin Jobs | Analytics", page_icon="💼", layout="wide")
st.title("💼 Amazon Berlin Jobs — Market Analytics")
st.caption("Explore role mix, skill demand and hiring patterns. Synthetic sample records are separated from official source context.")

@st.cache_data
def load_jobs():
    d=pd.read_csv(Path(__file__).parent/"data"/"amazon_berlin_jobs_synthetic.csv",parse_dates=["posted_date"])
    d["month"]=d.posted_date.dt.to_period("M").dt.to_timestamp()
    d["skill_list"]=d.skills.fillna("").str.split("; ")
    return d
@st.cache_data
def load_snapshot():
    return pd.read_csv(Path(__file__).parent/"data"/"official_source_snapshot.csv")

df=load_jobs(); snap=load_snapshot()
st.warning("The 520 row-level job records are synthetic demonstration data, NOT actual Amazon vacancies. Official live listing counts are shown separately as a dated snapshot. Verify all vacancies on Amazon.jobs.")
st.sidebar.header("Explore sample dataset")
dr=st.sidebar.date_input("Posted date",(df.posted_date.min().date(),df.posted_date.max().date()))
cats=st.sidebar.multiselect("Job category",sorted(df.category.unique()),default=sorted(df.category.unique()))
teams=st.sidebar.multiselect("Team",sorted(df.team.unique()),default=sorted(df.team.unique()))
types=st.sidebar.multiselect("Employment type",sorted(df.employment_type.unique()),default=sorted(df.employment_type.unique()))
levels=st.sidebar.multiselect("Experience level",sorted(df.experience_level.unique()),default=sorted(df.experience_level.unique()))
f=df.copy()
if len(dr)==2: f=f[(f.posted_date>=pd.Timestamp(dr[0]))&(f.posted_date<=pd.Timestamp(dr[1])+pd.Timedelta(days=1)-pd.Timedelta(seconds=1))]
f=f[f.category.isin(cats)&f.team.isin(teams)&f.employment_type.isin(types)&f.experience_level.isin(levels)]
if f.empty: st.info("No rows match your filters."); st.stop()
a,b,c,d=st.columns(4)
a.metric("Sample job records",f"{len(f):,}"); b.metric("Job categories",f.category.nunique()); c.metric("Teams represented",f.team.nunique()); d.metric("Distinct skills",f.skill_list.explode().nunique())
st.subheader("Official Amazon.jobs source snapshot")
cols=st.columns(len(snap))
for col,(_,r) in zip(cols,snap.iterrows()): col.metric(r.metric.replace(" shown on Amazon.jobs","").replace(" shown in Berlin filter",""),f"{int(r.value)}")
st.caption("Observed 5 November 2026. Dynamic website filter counts; not counts from the synthetic sample.")
l,r=st.columns(2)
with l:
    st.subheader("Sample roles by category")
    x=f.groupby("category").size().reset_index(name="records").sort_values("records")
    st.plotly_chart(px.bar(x,x="records",y="category",orientation="h"),use_container_width=True)
with r:
    st.subheader("Sample postings over time")
    x=f.groupby("month").size().reset_index(name="records")
    st.plotly_chart(px.line(x,x="month",y="records",markers=True),use_container_width=True)
l,r=st.columns(2)
with l:
    st.subheader("Most-mentioned skills in sample")
    x=f.skill_list.explode().value_counts().head(15).rename_axis("skill").reset_index(name="mentions")
    st.plotly_chart(px.bar(x,x="mentions",y="skill",orientation="h"),use_container_width=True)
with r:
    st.subheader("Employment type mix")
    x=f.employment_type.value_counts().rename_axis("employment_type").reset_index(name="records")
    st.plotly_chart(px.pie(x,names="employment_type",values="records",hole=.4),use_container_width=True)
st.subheader("Experience level by category")
st.dataframe(f.pivot_table(index="category",columns="experience_level",values="job_id",aggfunc="count",fill_value=0).reset_index(),use_container_width=True,hide_index=True)
st.subheader("Sample job records")
show=f.drop(columns=["month","skill_list"]).sort_values("posted_date",ascending=False)
st.dataframe(show,use_container_width=True,hide_index=True)
st.download_button("Download filtered sample CSV",show.to_csv(index=False).encode(), "filtered_amazon_berlin_jobs_sample.csv","text/csv")
st.subheader("Data limitations")
st.markdown("- Synthetic records do not represent actual vacancies, hiring volumes, skill frequencies or employment mix.\n- Official snapshot counts are dated dynamic search-filter counts.\n- Salary is omitted because comparable salary data is not consistently available.\n- This project is not affiliated with or endorsed by Amazon.")
