import streamlit as st
import pandas as pd
from filter import filter_data
from show_template import view_template
def view_instance():
    st.error("Template not finished yet!")
df=pd.read_csv("processed_data.csv")
template_data=pd.read_csv("template_data.csv")
st.title("Thagora Analytics")
col1=st.sidebar
col2,col3=st.columns((2,1))
col2=st.form('Filter')
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
        "Template":template_source,
        "start_date":start_date,
        "stop_date":stop_date,
        "pace":pace,
        "operator_id":operator_id,
        "all_operators":all_operators,
        "leather_type":leather_type,
        "all_leather_types":all_leather_types,
        "output":output
    },ignore_index=True)
    template_data.to_csv("template_data.csv")
with col3:
    st.table(template_data[['Template','Instance Name']])
    with st.form("Delete Row"):
        delete_row=st.number_input(min_value=0,max_value=template_data.shape[0],step=None,value=0,key="Delete Instance",label="Delete Instance")
        delete=st.form_submit_button("Delete")
    if delete:
        if delete_row >=template_data.shape[0]:
            st.error("This row doesn't exist yet!")
        else:
            template_data=template_data.drop(delete_row)
            template_data.to_csv("template_data.csv")
    with st.form("View Instance"):
        view_row=st.number_input(min_value=0,max_value=template_data.shape[0],value=0,step=None,key="View Instance",label="View Instance")
        view_button=st.form_submit_button("View")
    if view_button:
        if view_row>=template_data.shape[0]:
            st.error("This row doesn't exist yet!")
        else:
            df3=view_template(view_row)
            batch_id=col2.multiselect("Batch ID",list(df3['Batch ID']))
            leather_type=col2.multiselect("Leather type",list(df3['Leather type']))
            operator=col2.multiselect("Operator ID",list(df3['OperatorID']))
            apply=col2.form_submit_button("Apply")
            chart_data=df3[['scan per sqm','date']]
            col2.bar_chart(chart_data['scan per sqm'])
            col2.dataframe(df3)
                