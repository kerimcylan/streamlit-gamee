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
    page_title='Real-Time Data Science Dashboard',
    page_icon='✅',
    layout='wide'
)

# dashboard title

st.title("Real-Time / Live Data Science Dashboard")

# top-level filters

job_filter = st.selectbox("Select the Year", pd.unique(df['activation_Year_']))

# creating a single-element container.
placeholder = st.empty()

# dataframe filter

df = df[df['activation_Year_'] == job_filter]

# near real-time / live feed simulation

for seconds in range(200):
    # while True:

    df['Publisher'] = df['activation_Publisher_'] * np.random.choice(range(1,4))
    df['Genre'] = df['activation_Genre_'] * np.random.choice(range(1,4))
    with placeholder.container():

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(data_frame=df, y='count', x='Genre')
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x='Publisher')
            st.write(fig2)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)

