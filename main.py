import pandas as pd 
import streamlit as st 

st.image("./CodeBusters.png", width = 200)
st.header("AI4Good Hackathon")
st.subheader("AI4Good Hackathon text")
baseDF = pd.read_csv("./data/prod_data_202207_test.csv")
weatherDF = pd.read_csv("./data/hourly_weather_data_202207_test.csv")
baseDF = baseDF.rename(columns = {'LDate': "DATE"})

baseDF["DATE"] = pd.to_datetime(baseDF["DATE"]).dt.date
weatherDF["DATE"] = pd.to_datetime(weatherDF["DATE"]).dt.date
col1, col2 = st.columns(2)
col1.write(baseDF)
col2.write(weatherDF)
combinedDF = pd.concat([baseDF, weatherDF])

st.write(combinedDF)

combinedDF.to_csv("./data.csv")