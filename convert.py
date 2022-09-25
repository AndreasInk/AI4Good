# https://github.com/mfpierre/coreml-scikit-example/blob/master/main.py
import coremltools
import pickle 

with open("model.pkl", 'rb') as file:  
    model = pickle.load(file)
    coreml_model = coremltools.converters.sklearn.convert(model, ["DATE", "HOUR", "HourlyVisibility", "HourlyPrecipitation", "Coverage 1", "Coverage 2", "Coverage 3", "Layer 1", "Layer 2", "Layer 3", "Cloud Height 1", "Cloud Height 2", "Cloud Height 3"], 'solar class')
    coreml_model.save('solar.mlmodel')  

