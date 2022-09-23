import pandas as pd 
import streamlit as st 

st.image("./CodeBusters.png", width = 200)
st.header("AI4Good Hackathon")
st.subheader("AI4Good Hackathon text")
df = pd.read_csv("./data/prod_data_2021_train.csv")
st.table(df)
