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

st.metric(label="Platform", value=str('activations_Platform_'), delta=-0.5,
    delta_color="inverse")


st.subheader('Deneme Data')
st.bar_chart(data=df,x = 'activation_Genre_',y='count')







