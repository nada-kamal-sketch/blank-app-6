import streamlit as st
st.header('calculate area')
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
  st.write(f'area={area}')
