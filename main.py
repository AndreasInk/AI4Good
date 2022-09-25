import pandas as pd 
import streamlit as st 

st.image("./Code Busters Logo.png", width = 200)
st.header("AI4Good Hackathon: Code Busters")
st.subheader("Problem 2: Solar Power Generation")

training = pd.read_csv("./training.csv")
testing = pd.read_csv("./testing.csv")
with st.expander("Training Table"):
    st.table(training)

with st.expander("Testing Table"):
    st.table(testing)