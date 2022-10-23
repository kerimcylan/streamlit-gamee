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

st.set_page_config(page_title="Dashboard",layout='wide')

st.markdown("<h1 style='text-align: center; color: black;'>My Dashboard</h1>", unsafe_allow_html=True)


st.markdown('***') #separator

buffer, col3, col4 = st.columns([1,7,7,7])


with col3:
    st.markdown("<h5 style='text-align: center; color: black;'>Age Distribution</h1>", unsafe_allow_html=True)
    st.bar_chart(get_distribution(sql, 'activation_Year_'))

with col4:
    st.markdown("<h5 style='text-align: center; color: black;'>Country Distribution</h1>", unsafe_allow_html=True)
    st.pyplot(pie_chart(get_distribution(sql, 'activation_Genre_')))

st.markdown('***') #separator






