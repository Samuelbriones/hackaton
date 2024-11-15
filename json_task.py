import os
import django
import pandas as pd
import json

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackaton.settings') 
django.setup()

# Leer el archivo CSV
df = pd.read_csv('/home/crowstar/Escritorio/Programación/Hackaton/backend/data.csv')

# Crear una lista de diccionarios para convertir en JSON
json_data = []

for _, row in df.iterrows():
    record = {
        "entity": row['Entity'],
        "year": row['Year'],
        "access_to_electricity": row.get('Access to electricity (% of population)', 0),
        "access_to_clean_fuels": row.get('Access to clean fuels for cooking', 0),
        "renewable_electricity_capacity": row.get('Renewable-electricity-generating-capacity-per-capita', 0),
        "financial_flows": row.get('Financial flows to developing countries (US $)', 0),
        "renewable_energy_share": row.get('Renewable energy share in the total final energy consumption (%)', 0),
        "electricity_from_fossil_fuels": row.get('Electricity from fossil fuels (TWh)', 0),
        "electricity_from_nuclear": row.get('Electricity from nuclear (TWh)', 0),
        "electricity_from_renewables": row.get('Electricity from renewables (TWh)', 0),
        "low_carbon_electricity": row.get('Low-carbon electricity (% electricity)', 0),
        "primary_energy_consumption": row.get('Primary energy consumption per capita (kWh/person)', 0),
        "energy_intensity": row.get('Energy intensity level of primary energy (MJ/$2017 PPP GDP)', 0),
        "co2_emissions": row.get('Value_co2_emissions_kt_by_country', 0),
        "renewables_equivalent": row.get('Renewables (% equivalent primary energy)', 0),
        "gdp_growth": row.get('gdp_growth', 0),
        "gdp_per_capita": row.get('gdp_per_capita', 0),
        "density": row.get('Density\n(P/Km2)', 0),
        "land_area": row.get('Land Area(Km2)', 0),
        "latitude": row.get('Latitude', 0),
        "longitude": row.get('Longitude', 0)
    }
    json_data.append(record)

# Guardar los datos en un archivo JSON
output_path = '/home/crowstar/Escritorio/Programación/Hackaton/backend/output_data.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print(f'Datos guardados en {output_path}')
