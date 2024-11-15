import pandas as pd
import os
import joblib

def CO2_prediction (electricity: float, clean_fuels: float, fossil: float, 
                    renewables: float, nuclear: float, kWh_per_person: float):
    
    model = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'co2_model.pkl') 

    new_data = {
        'Access to electricity (% of population)': [electricity],
        'Access to clean fuels for cooking' : [clean_fuels],
        'Electricity from fossil fuels (TWh)': [fossil],
        'Electricity from renewables (TWh)': [renewables],
        'Electricity from nuclear (TWh)': [nuclear],
        'Primary energy consumption per capita (kWh/person)': [kWh_per_person],
    }

    new_data_df = pd.DataFrame(new_data)

    loaded_model = joblib.load(model)

    predictions = loaded_model.predict(new_data_df)

    print("Predicciones de emisiones de CO2 (kt):", predictions)
    
    return predictions[0]
