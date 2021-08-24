import streamlit as st

def show_form():
     st.empty()
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
