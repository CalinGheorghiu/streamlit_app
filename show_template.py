import pandas as pd
import streamlit as st
from filter import filter_data
from datetime import date
import datetime as dt
df=pd.read_csv("template_data.csv")
print(df.columns)
df1=pd.read_csv("Scan_data.csv")
def view_template(row):
    df3=df[['Template', 'Instance Name', 'all_leather_types', 'all_operators',
       'leather_type', 'operator_id', 'pace', 'start_date', 'stop_date',
       'output']]
    df4=df3[['all_leather_types', 'all_operators',
       'leather_type', 'operator_id', 'pace', 'start_date', 'stop_date',
       'output']]
    print(df4.iloc[row])
    values=list(df4.iloc[row])
    print(values[0],values[1],values[3])
    df2=filter_data(pd.to_datetime(values[5]),pd.to_datetime(values[6]),values[4],values[3],values[2],values[7],values[1],values[0])
    return df2