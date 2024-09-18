import pandas as pd
import streamlit as st
st.header('file upload app2')
file=st.file_uploader('upload dataset',type=['csv'])
if file is not None:
     df=pd.read_csv(file)
     st.write(df)
     num_row=st.slider('choose num rows',min_value=1,max_value=len(df),step=1)
     names_column=st.multiselect('choose columns',df.columns.to_list)
     st.write(df[:num_row][names_column])
     if names_column:
           st.write(df[:num_row][names_column])
     else:
          st.write(df[:num_row])
          
          
       
      
   
    
   

