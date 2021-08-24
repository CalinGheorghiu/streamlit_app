import streamlit as st
import pandas as pd
from filter import filter_data
def view_instance():
    st.error("Template not finished yet!")
df=pd.read_csv("processed_data.csv")
template_data=pd.read_csv("template_data.csv")
col1=st.sidebar
col2,col3=st.columns((2,1))
col1.header('Create Template')
instance_name=col1.text_input("Instance Name")
template_source=col1.selectbox("Template",[1,2])
start_date=col1.date_input("Start Date")
stop_date=col1.date_input("Stop Date")
pace=col1.selectbox("Pace",['Daily','Weekly','Monthly','Yearly','All'])
operator_id=col1.multiselect("OperatorID",list(df['OperatorID']))
all_operators=col1.checkbox("All Operators")
leather_type=col1.multiselect("Leather Type",list(df['Leather type']))
all_leather_types=col1.checkbox("All Leather Types")
if template_source==1:
    output=col1.multiselect("Output",["Scan time"," Recuts"])
elif template_source==2:
    output=col1.multiselect("Output",["Yield","Price"])
button=col1.button("Add Instance")
if button:
    template_data=template_data.append({
        "Instance Name":instance_name,
        "Template":template_source
    },ignore_index=True)
    template_data.to_csv("template_data.csv")
    col2.table(template_data[['Template','Instance Name']])
    col2.header(instance_name)
    col2.dataframe(filter_data(df,start_date,stop_date,pace,operator_id,leather_type,output,all_operators,all_leather_types))
with col3:
    with st.form("Delete Row"):
        delete_row=st.number_input(min_value=0,max_value=template_data.shape[0],step=None,value=0,key="Delete Instance",label="Delete Instance")
        delete=st.form_submit_button("Delete")
    if delete:
        if delete_row >=template_data.shape[0]:
            st.error("This row doesn't exist yet!")
            col2.table(template_data[['Template','Instance Name']])
        else:
            template_data=template_data.drop(delete_row)
            col2.table(template_data[['Template','Instance Name']])
            template_data.to_csv("template_data.csv")
    with st.form("View Instance"):
        view_row=st.number_input(min_value=0,max_value=template_data.shape[0],value=0,step=None,key="View Instance",label="View Instance")
        view_button=st.form_submit_button("View")
    if view_button:
        if view_row>=template_data.shape[0]:
            st.error("This row doesn't exist yet!")
            col2.table(template_data[['Template','Instance Name']])
        else:
            view_instance(template_data.iloc(view_row))
            col2.table(template_data[['Template','Instance Name']])