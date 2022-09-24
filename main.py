import pandas as pd 
import streamlit as st 

# Add headers
st.image("./CodeBusters.png", width = 200)
st.header("AI4Good Hackathon")
st.subheader("AI4Good Hackathon text")


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

    col1, col2 = st.columns(2)
    col1.write(baseDF)
    col2.write(weatherDF)


    # Combine the data frames
    combinedDF = pd.merge(baseDF, weatherDF, on=["DATE", "HOUR"])

    combinedDF["AVG"] = combinedDF["AVG"].apply(pd.to_numeric)
    combinedDF["AVG"] = combinedDF["AVG"] > 4

    st.write(combinedDF["AVG"])

    savedf = combinedDF[["DATE", "HOUR", "AVG", "HourlyVisibility", "HourlyPrecipitation"]]
    st.table(savedf)
    savedf = savedf.fillna(0)
    savedf = savedf[savedf["HourlyPrecipitation"] != "T"]
    return savedf

process("./data/prod_data_2022_train.csv", "./data/hourly_weather_data_train.csv").to_csv("./train.csv")
process("./data/prod_data_202207_test.csv", "./data/hourly_weather_data_202207_test.csv").to_csv("./test.csv")