import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackaton.settings') 
django.setup()

from APP.Core.models import EnergyData 

file = model = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.csv') 

df = pd.read_csv(file)

for _, row in df.iterrows():
    EnergyData.objects.create(
        entity=row['Entity'],
        year=row['Year'],
        access_to_electricity=row.get('Access to electricity (% of population)', None),
        access_to_clean_fuels=row.get('Access to clean fuels for cooking', None),
        renewable_electricity_capacity=row.get('Renewable-electricity-generating-capacity-per-capita', None),
        financial_flows=row['Financial flows to developing countries (US $)'] if pd.notna(row['Financial flows to developing countries (US $)']) else None,
        renewable_energy_share=row.get('Renewable energy share in the total final energy consumption (%)', None),
        electricity_from_fossil_fuels=row.get('Electricity from fossil fuels (TWh)', None),
        electricity_from_nuclear=row.get('Electricity from nuclear (TWh)', None),
        electricity_from_renewables=row.get('Electricity from renewables (TWh)', None),
        low_carbon_electricity=row.get('Low-carbon electricity (% electricity)', None),
        primary_energy_consumption=row.get('Primary energy consumption per capita (kWh/person)', None),
        energy_intensity=row.get('Energy intensity level of primary energy (MJ/$2017 PPP GDP)', None),
        co2_emissions=row.get('Value_co2_emissions_kt_by_country', None),
        renewables_equivalent=row.get('Renewables (% equivalent primary energy)', None),
        gdp_growth=row.get('gdp_growth', None),
        gdp_per_capita=row.get('gdp_per_capita', None),
        density=row.get('Density\n(P/Km2)', None),
        land_area=row.get('Land Area(Km2)', None),
        latitude=row.get('Latitude', None),
        longitude=row.get('Longitude', None)
    )
    print(f'Create {_}')
