import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSV directly from GitHub
url = "https://raw.githubusercontent.com/thqkurneeraj/Data-Visualization-Dashboard/main/covid_sample.csv"
df = pd.read_csv(url)

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")
st.title("COVID-19 Data Visualization Dashboard")
st.write("This dashboard auto-loads COVID data from GitHub.")

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

country_col = [c for c in df.columns if "country" in c or "location" in c or "state" in c][0]
date_col = [c for c in df.columns if "date" in c][0]
cases_col = [c for c in df.columns if "cases" in c or "confirmed" in c][0]
deaths_col = [c for c in df.columns if "death" in c][0]

df[date_col] = pd.to_datetime(df[date_col])

countries = df[country_col].unique()
selected_country = st.selectbox("Select Country", countries)

filtered_df = df[df[country_col] == selected_country]

col1, col2 = st.columns(2)

with col1:
    fig_cases = px.line(filtered_df, x=date_col, y=cases_col, title="COVID-19 Cases Over Time")
    st.plotly_chart(fig_cases, use_container_width=True)

with col2:
    fig_deaths = px.line(filtered_df, x=date_col, y=deaths_col, title="COVID-19 Deaths Over Time")
    st.plotly_chart(fig_deaths, use_container_width=True)

st.subheader("Cases vs Deaths Comparison")
fig_bar = px.bar(filtered_df, x=date_col, y=[cases_col, deaths_col])
st.plotly_chart(fig_bar, use_container_width=True)
