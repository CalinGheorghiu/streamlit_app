import streamlit as st
import pandas as pd
def filters(operator_id,leather_type,pace):
    st.multiselect("Operators",operator_id)
    st.multiselect("Leather Type",leather_type)
    st.selectbox("Pace",pace)