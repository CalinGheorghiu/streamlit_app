import streamlit as st
import pandas as pd
from datetime import date
st.session_state['df'] = pd.read_csv("Scan_data.csv")
instance_df=pd.DataFrame(
    columns=['Template','Instance Name']
)
instance_dict={}
k=0
col1,col2=st.columns(2)
templates=[]
names=[]
login=st.container()
username=st.text_input("Username",value="")
password=st.text_input("Password",value="")
with login:
    st.write(username)
    st.write(password)
    submit=st.button("Log in")

if submit:
    if username=="admin" and password=="admin":
        with st.form(key='template-form'):
                instance_name=st.text_input("Instance Name")
                template_source=st.selectbox("Template",[1,2,3])
                start_date=st.date_input("Start Date")
                stop_date=st.date_input("Stop Date")
                pace=st.selectbox("Pace",['Daily','Weekly','Monthly'])
                operator_id=st.multiselect("OperatorID",list(df['OperatorID']))
                all_operators=st.checkbox("All Operators")
                leather_type=st.multiselect("Leather Type",list(df['Leather type']))
                all_leather_types=st.checkbox("All Leather Types")
                output=st.multiselect("Output",["Scan time"," Recuts", "Yield"])
                submit=st.form_submit_button("Submit")
        if submit:
            my_table = st.table(instance_df)
            st.write(instance_name)
            df1=st.session_state['df'].copy()
            if all_operators is False:
                df1=df1[df1['OperatorID'].isin(operator_id)]
            if all_operators is False:
                df1=df1[df1['Leather type'].isin(leather_type)]
            st.write(df1[['OperatorID','Leather type','scanned area','time','date']])
            st.session_state['df']=st.session_state['df'].append(df1)
        

