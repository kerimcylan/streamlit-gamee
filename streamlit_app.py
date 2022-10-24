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

st.title("Game Count Dashboard")

st.sidebar.checkbox("Choose Genre", True, key=1)
select = st.sidebar.selectbox("Select a Genre",df['activation_Genre_'])

year_data=df[df['activation_Year_'] == select]
select_status = st.sidebar.radio("Games Status", ('activation_Brand_', 'activation_Publisher'))
