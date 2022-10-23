from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)




# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.experimental_memo to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

def _fetch_data_bigquery(query):
    """
      Take SQL query in Standard SQL and returns a Pandas DataFrame of results
      ref: https://cloud.google.com/bigquery/docs/reference/standard-sql/enabling-standard-sql
    """
    return client.query(query, location="US").to_dataframe()


rows = run_query("SELECT * FROM `robust-caldron-365720.games.game` 
WHERE NOT activation_Year_ = 'N/A'
")

st.altair_char(rows)
