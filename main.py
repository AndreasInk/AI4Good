import pandas as pd 
import streamlit as st 

# Add headers
st.image("./CodeBusters.png", width = 200)
st.header("AI4Good Hackathon")
st.subheader("Problem 2: Solar Power Generation")


def process(base, weather):
    # get dfs 
    baseDF = pd.read_csv(base)
    weatherDF = pd.read_csv(weather)
   
    # Format date columns
    baseDF = baseDF.rename(columns = {'LDate': "DATE"})
    baseDF["DATEML"] = pd.to_datetime(baseDF["DATE"]).dt.date
    baseDF["HOUR"] = pd.to_datetime(baseDF["DATE"]).dt.hour
    baseDF["DATE"] = pd.to_datetime(baseDF["DATE"]).dt.date

    weatherDF["HOUR"] = pd.to_datetime(weatherDF["DATE"]).dt.hour
    weatherDF["DATE"] = pd.to_datetime(weatherDF["DATE"]).dt.date

    baseDF["AVG"] = baseDF[["Jax Solar", "NW Jax"]].mean(axis = "columns")

    # Combine the data frames
    combinedDF = pd.merge(baseDF, weatherDF, on=["DATE", "HOUR"])

    combinedDF["AVG"] = combinedDF["AVG"].apply(pd.to_numeric)
    combinedDF["AVG"] = combinedDF["AVG"] > 4

    savedDF = combinedDF[["DATE", "HOUR", "AVG", "HourlyVisibility", "HourlyPrecipitation"]]
    savedDF = savedDF[savedDF["HourlyPrecipitation"] != "T"]
    savedDF = savedDF.fillna(0)
    savedDF["HourlyPrecipitation"] = savedDF["HourlyPrecipitation"].map(lambda x: str(x).lstrip('+-').rstrip('aAbBcC'))
    return savedDF

#Download data
training = process("./data/prod_data_2022_train.csv", "./data/hourly_weather_data_train.csv")
with st.expander("Training Table"):
    st.table(training)
    
st.download_button("Download training", training.to_csv().encode('utf-8'))
testing = process("./data/prod_data_202207_test.csv", "./data/hourly_weather_data_202207_test.csv")

with st.expander("Testing Table"):
    st.table(testing)

st.download_button("Download testing", testing.to_csv().encode('utf-8'))