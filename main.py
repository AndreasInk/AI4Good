import pandas as pd 
import streamlit as st 

# Add headers
st.image("./Code Busters Logo.png", width = 200)
st.header("AI4Good Hackathon")
st.subheader("Problem 2: Solar Power Generation")

# TODO: Split sky conditions into 3 parts with a column name for each
def parse_sky_condition(df):
   newDF = pd.DataFrame()
   newDF["sky_condition"] = []
   newDF["sky_cloud_height"] = []
   for line in df["HourlySkyConditions"]:

        cloudLayers = str(line).split(" ")
        st.write(cloudLayers)
        try:
            cloudLayer = cloudLayers[0].split(":")
            newDF["sky_condition"] = cloudLayer[0]
            newDF["sky_cloud_height"] = cloudLayer[1]
            
        except:
            st.write()
        try:
            cloudLayer = cloudLayers[1].split(":")
            newDF["sky_condition"] = cloudLayer[0]
            newDF["sky_cloud_height"] = cloudLayer[1]
           
        except:
            st.write()
        try:
            cloudLayer = cloudLayers[2].split(":")
            newDF["sky_condition"] = cloudLayer[0]
            newDF["sky_cloud_height"] = cloudLayer[1]
        except:
            st.write()
                
   st.write(newDF["sky_cloud_height"])      
       
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
   # parse_sky_condition(combinedDF)
    savedDF = combinedDF[["DATE", "HOUR", "AVG", "HourlyVisibility", "HourlyPrecipitation"]]
    savedDF = savedDF[savedDF["HourlyPrecipitation"] != "T"]
    savedDF = savedDF.fillna(0)
    savedDF["HourlyPrecipitation"] = savedDF["HourlyPrecipitation"].map(lambda x: str(x).lstrip('+-').rstrip('aAbBcC'))
    return savedDF

#Download data
training = process("./data/prod_data_2022_train.csv", "./data/Parsed_Hourly_Weather_Data_Train.csv")
with st.expander("Training Table"):
    st.table(training)
training.to_csv("./training.csv")
st.download_button(label="Download training", data=training.to_csv().encode('utf-8'))
testing = process("./data/prod_data_202207_test.csv", "./data/hourly_weather_data_202207_test.csv")

with st.expander("Testing Table"):
    st.table(testing)

st.download_button("Download testing", testing.to_csv().encode('utf-8'))