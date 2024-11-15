from django.db import models

class EnergyData(models.Model):
    entity = models.CharField(max_length=100)
    year = models.IntegerField()
    access_to_electricity = models.FloatField(null=True, blank=True)
    access_to_clean_fuels = models.FloatField(null=True, blank=True)
    renewable_electricity_capacity = models.FloatField(null=True, blank=True)
    financial_flows = models.BigIntegerField(null=True, blank=True)
    renewable_energy_share = models.FloatField(null=True, blank=True)
    electricity_from_fossil_fuels = models.FloatField(null=True, blank=True)
    electricity_from_nuclear = models.FloatField(null=True, blank=True)
    electricity_from_renewables = models.FloatField(null=True, blank=True)
    low_carbon_electricity = models.FloatField(null=True, blank=True)
    primary_energy_consumption = models.FloatField(null=True, blank=True)
    energy_intensity = models.FloatField(null=True, blank=True)
    co2_emissions = models.FloatField(null=True, blank=True)
    renewables_equivalent = models.FloatField(null=True, blank=True)
    gdp_growth = models.FloatField(null=True, blank=True)
    gdp_per_capita = models.FloatField(null=True, blank=True)
    density = models.FloatField(null=True, blank=True)
    land_area = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.entity} - {self.year}"