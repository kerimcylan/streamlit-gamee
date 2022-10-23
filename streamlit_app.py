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

#fig_col1, fig_col2 = st.columns(2)

#####with fig_col1:
    #####st.markdown("### First Chart")
    #####fig = px.density_heatmap(
#####        data_frame=df, y="count", x="activation_Year_")
    #####st.write(fig)
   
#####with fig_col2:
    #####st.markdown("### Second Chart")
    #####fig2 = px.histogram(data_frame=df, x="activation_Genre_")
 #####   st.write(fig2)

############################################
for seconds in range(200):
#while True: 
    df['activation_Year_new'] = df['activation_Year_'] * np.random.choice(range(1))
    df['activation_Genre_new'] = df['activation_Genre_'] * np.random.choice(range(1))
    df['activation_Platform_new'] = df['activation_Platform_'] * np.random.choice(range(1))

    # creating KPIs 
    avg_count = np.mean(df['count']) 
    

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs 
        kpi1.metric(label="Count ⏳", value=round(avg_count), delta= round(avg_count) - 10)

        # create two columns for charts 

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(
            data_frame=df, y="count", x="activation_Year_new")
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x="activation_Genre_new")
            st.write(fig2)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
    placeholder.empty()

