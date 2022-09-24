import pandas as pd 
import streamlit as st 

# Add headers
st.image("./CodeBusters.png", width = 200)
st.header("AI4Good Hackathon")
st.subheader("AI4Good Hackathon text")

# get dfs 
baseDF = pd.read_csv("./data/prod_data_202207_test.csv")
weatherDF = pd.read_csv("./data/hourly_weather_data_202207_test.csv")
baseDF = baseDF.rename(columns = {'LDate': "DATE"})
baseDF["DATEML"] = pd.to_datetime(baseDF["DATE"]).dt.date
# Format date columns
baseDF["HOUR"] = pd.to_datetime(baseDF["DATE"]).dt.hour
baseDF["DATE"] = pd.to_datetime(baseDF["DATE"]).dt.date

weatherDF["DATEML"] = pd.to_datetime(weatherDF["DATE"]).dt.date
weatherDF["HOUR"] = pd.to_datetime(weatherDF["DATE"]).dt.hour
weatherDF["DATE"] = pd.to_datetime(weatherDF["DATE"]).dt.date

baseDF["AVG"] = baseDF[["Jax Solar", "NW Jax"]].mean(axis = "columns")
# st.write(baseDF[["Jax Solar", "NW Jax"]])
col1, col2 = st.columns(2)
col1.write(baseDF)
col2.write(weatherDF)


# Combine the data frames
combinedDF = pd.merge(baseDF, weatherDF, on=["DATE", "HOUR"])
# outputs = outputs.groupby(by=["DATE", "HOUR"]).mean()
# combinedDF["AVG_OUTPUT"] = combinedDF.groupby("DATE").mean()

st.table(combinedDF)
combinedDF = combinedDF.fillna(0)
combinedDF.to_csv("./data.csv")