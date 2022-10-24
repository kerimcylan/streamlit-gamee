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
    page_title="Real-Time Game Selling Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Real-Time / Live Game Selling Dashboard")



##################################################

fig_col1, fig_col2 = st.columns(2)


with fig_col1:
    st.markdown("### First Chart")
    fig = px.pie(ddf,title="Pie Deneme" ,value="count", names="activation_Year_")
    st.write(fig)
   
with fig_col2:
    st.markdown("### Second Chart")
    fig2 = px.histogram(data_frame=df, x="activation_Genre_",color='count')
    st.write(fig2)
  

st.markdown("### Detailed Data View")
st.dataframe(df)

