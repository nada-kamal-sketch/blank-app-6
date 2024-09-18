'''import streamlit as st
st.sidebar.title('sidbar')
st.header('calculate area')
with sidebar:
choose=st.selectbox('choose the shape',['circle','rectangle'])
if choose=='circle':
  r=st.number_input('enter the radius',min_value=1,max_value=100)
  area=3.14*r*r
elif choose=='rectangle':
  l=st.number_input('enter the length',min_value=1,max_value=100)
  b=st.number_input('enter the breadth',min_value=1,max_value=100)
  area=l*b
btn=st.button('calculate')
if btn:
  st.write(f'area={area}')'''
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
      st.write(df[names_column][:num_row])
    else:

 st.write(df[:num_row])
