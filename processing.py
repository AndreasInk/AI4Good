import pandas as pd 
import streamlit as st 

# Add headers
st.image("./Code Busters Logo.png", width = 200)
st.header("AI4Good Hackathon")
st.subheader("Problem 2: Solar Power Generation")
       
def process(base, weather, isClassification = False):
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
    if isClassification:
        combinedDF["AVG"] = combinedDF["AVG"] > 4
   
    savedDF = combinedDF[["DATE", "HOUR", "AVG", "HourlyVisibility", "HourlyPrecipitation", "Coverage 1", "Coverage 2", "Coverage 3", "Layer 1", "Layer 2", "Layer 3", "Cloud Height 1", "Cloud Height 2", "Cloud Height 3"]]
    #savedDF = combinedDF[["DATE", "HOUR", "AVG", "HourlyVisibility", "HourlyPrecipitation"]]
    savedDF = savedDF[savedDF["HourlyPrecipitation"] != "T"]
    savedDF = savedDF.fillna(0)
    savedDF["HourlyPrecipitation"] = savedDF["HourlyPrecipitation"].map(lambda x: str(x).lstrip('+-').rstrip('aAbBcC'))
    return savedDF

#Download data
training = process("./data/prod_data_2022_train.csv", "./data/Parsed_Hourly_Weather_Data_Train.csv")
with st.expander("Training Table"):
    st.table(training)
    
training.to_csv("./training.csv")
st.download_button(label="Download training", data= "./training.csv")
testing = process("./data/prod_data_202207_test.csv", "./data/Parsed_Hourly_Weather_Data_Test.csv")
testing.to_csv("./testing.csv")
with st.expander("Testing Table"):
    st.table(testing)

st.download_button("Download testing", testing.to_csv().encode('utf-8'))