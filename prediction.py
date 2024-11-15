import pandas as pd
import os

model = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'co2_model.pkl') 

# Datos de ejemplo para predicción
new_data = {
    'Access to electricity (% of population)': [100.0],
    'Access to clean fuels for cooking' : [100.0],
    'Electricity from fossil fuels (TWh)': [1.0],
    'Electricity from renewables (TWh)': [20.0],
    'Electricity from nuclear (TWh)': [10.0],
    'Primary energy consumption per capita (kWh/person)': [1000.0],
}

new_data_df = pd.DataFrame(new_data)

import joblib

loaded_model = joblib.load(model)

predictions = loaded_model.predict(new_data_df)

print("Predicciones de emisiones de CO2 (kt):", predictions)
