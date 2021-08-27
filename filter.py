import streamlit as st
import datetime
import pandas as pd
import datetime as dt
from datetime import date
def filter_data(start_date,stop_date,pace,operator,leather,output,operator_boolean,leather_boolean):
    df=pd.read_csv("Scan_data.csv")
    df['date']=pd.to_datetime(df['date']).dt.date
    df=df.loc[(df['date']>=start_date) & (df['date']<=stop_date)]
    df1=df.copy()
    df1['scan per sqm']=df['time']/df['scanned area']
    print(df1)
    if not operator_boolean:
        df1=df1[df1['OperatorID'].isin(list(operator))]
        print(df1)
    if not leather_boolean:
        df1=df1[df1['Leather type'].isin(list(leather))]
        print(df1)
    if pace=='Weekly':
        df1=df1.groupby(['Year','week_no','Leather type','OperatorID','Batch ID'],as_index=False).mean()
        print(df1)
    elif pace=='Monthly':
        df1=df1.groupby(['Year','month','Leather type','OperatorID','Batch ID'],as_index=False).mean()
        print(df1)
    elif pace=='Yearly':
        df1=df1.groupby(['Year','Leather type','OperatorID','Batch ID'],as_index=False).mean()
        print(df1)
    if df1.empty:
        st.error("No available data")
    else:
        return df1[['Batch ID','Leather type','OperatorID','scan per sqm','scanned area','time','date']]
    return df1


