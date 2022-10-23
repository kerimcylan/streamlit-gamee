from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import plotly.express as px
import time
from google.cloud import bigquery


# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)


sql = """
    SELECT *
    FROM `robust-caldron-365720.games.game`
    WHERE NOT activation_Year_ = 'N/A'
    ORDER BY activation_Year_ DESC
"""

df = client.query(sql).to_dataframe()


st.set_page_config(
    page_title="Real-Time Game Selling Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Real-Time / Live Game Selling Dashboard")

year_filter = st.selectbox("Select the Year", pd.unique(df["activation_Year_"]))
df = df[df["activation_Year_"] == year_filter]

##################################################


fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("### First Chart")
    fig = px.density_heatmap(
        data_frame=df, y="count", x="activation_Year_"
    )
    st.write(fig)
   
with fig_col2:
    st.markdown("### Second Chart")
    fig2 = px.histogram(data_frame=df, x="activations_Genre_")
    st.write(fig2)


