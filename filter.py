import streamlit as st
import datetime
import pandas as pd
import datetime as dt
from datetime import date
def filter_data(df,start_date,stop_date,pace,operator,leather,output,operator_boolean,leather_boolean):
    df['date']=pd.to_datetime(df['date']).dt.date
    df=df.loc[(df['date']>=start_date) & (df['date']<=stop_date)]
    df1=df.copy()
    if not operator_boolean:
        df1=df1[df1['OperatorID'].isin(operator)]
    if not leather_boolean:
        df1=df1[df1['Leather type'].isin(leather)]
    if pace=='Weekly':
        df1=df1.groupby(['Year','week_no','Leather type','OperatorID','Batch ID'],as_index=False).mean()
    elif pace=='Monthly':
        df1=df1.groupby(['Year','month','Leather type','OperatorID','Batch ID'],as_index=False).mean()
    elif pace=='Yearly':
        df1=df1.groupby(['Year','Leather type','OperatorID','Batch ID'],as_index=False).mean()
    if df1.empty:
        st.error("No available data")

    return df1


