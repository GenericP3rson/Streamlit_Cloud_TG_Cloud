# streamlit_app.py

import streamlit as st
import pyTigerGraph as tg

# Initialize connection.
conn = tg.TigerGraphConnection(**st.secrets["tigergraph"])
conn.apiToken = conn.getToken(conn.createSecret())

# Pull data from the graph by running the "mostDirectInfections" query.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def get_data():
    most_infections = conn.runInstalledQuery("mostDirectInfections")[0]["Answer"][0]
    return most_infections["v_id"], most_infections["attributes"]

items = get_data()

# Print results.
st.title(f"Patient {items[0]} has the most direct infections")
for key, val in items[1].items():
    st.write(f"Patient {items[0]}'s {key} is {val}.")

    
