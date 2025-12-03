import streamlit as st
import pandas as pd
import plotly.express as px

st.title("COVID-19 Data Visualization Dashboard")

uploaded_file = st.file_uploader("Upload COVID-19 CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    df.columns = df.columns.str.strip().str.lower()

    country = df.columns[df.columns.str.contains('country|location|state')][0]
    date = df.columns[df.columns.str.contains('date|day')][0]
    cases = df.columns[df.columns.str.contains('cases|confirmed')][0]
    deaths = df.columns[df.columns.str.contains('death')][0]

    df[date] = pd.to_datetime(df[date])

    countries = df[country].unique()
    chosen = st.selectbox("Select Country", countries)

    new_df = df[df[country] == chosen]

    fig1 = px.line(new_df, x=date, y=cases, title="COVID Cases Over Time")
    st.plotly_chart(fig1)

    fig2 = px.line(new_df, x=date, y=deaths, title="COVID Deaths Over Time")
    st.plotly_chart(fig2)

else:
    st.info("Upload a CSV file to continue.")
