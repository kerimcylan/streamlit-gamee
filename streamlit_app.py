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
import numpy as np
import matplotlib.pyplot as plt
import plost
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import random

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

sql1 = """
    SELECT activation_Year_ , count(count) as count
    FROM `robust-caldron-365720.games.game`
    WHERE NOT activation_Year_ = 'N/A'
    GROUP BY activation_Year_
    ORDER BY RAND()
    LIMIT 1
"""


df = client.query(sql).to_dataframe()
df2 = client.query(sql1).to_dataframe()


st.set_page_config(
    page_title="Real-Time Game Count Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Games Count and Year by Year Game Genre's Dashboard")


st.write("Yıllara Göre Çıkan Oyunların Sayısı")
fig = px.histogram(data_frame = df, x="activation_Year_", y = "count")
st.write(fig)


st.write("Yıla ve Türüne göre Platformlara Sürülen Oyunlar")
fig2 = alt.Chart(df).mark_bar().encode(
    x='activation_Year_',
    y='activation_Genre_',
    color='activation_Platform_')
st.write(fig2)

st.metric(label="Year", value=df2, delta='count',
    delta_color="inverse")


def fetch_and_clean_data(df):
    return df

d1= fetch_and_clean_data(df)
st.experimental_rerun()

