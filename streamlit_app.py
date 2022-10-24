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
df_utils=df.dropna(axis=0)
df_utils.reset_index(drop=True,inplace=True)
a=df_utils['activation_Year_'].str.split(" ")
# for publish date
b=[]
for i in range(0,len(a)):
 c=a[i][0]
 b.append(c)
#for status date
d=df_utils['activation_Genre_'].str.split(" ")
e=[]
for i in range(0,len(a)):
 f=d[i][0]
 e.append(f)
df_utils['activation_Publisher_']=b
df_utils['activation_Year_']=e
g=df_utils['count'].str.split('/')
h=[]
for i in range(0,len(a)):
 f=g[i][2]
 h.append(f)
df_utils['activation_Genre_']=h

st.header("Real-Time Dashboard")
chart_selector = st.sidebar.selectbox("Select the type of chart", ['Pie chart','Bar chart'])
if chart_selector=='Pie chart':
  st.write("## Pie chart analysis for various crime")
  pie_chart = px.pie(df_utils, values='activation_Year_', names='activation_Publisher_')
  st.plotly_chart(pie_chart,use_container_width = True)
else:
  st.write("## Bar chart analysis for crime varying according time")
  bar_chart = px.histogram(df_utils, x="count", color="activation_Genre")
  st.plotly_chart(bar_chart,use_container_width = True)
