from django.views.generic import TemplateView
from APP.Core.models import EnergyData
from django.db.models import Max
import json


class MainTemplateView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_year = EnergyData.objects.aggregate(Max('year'))['year__max']
        items = EnergyData.objects.filter(year=latest_year).values(
        'entity',
        'electricity_from_fossil_fuels',
        'electricity_from_nuclear',
        'co2_emissions',
        'renewables_equivalent'
        )
        try:
            context["countries"] = list(items)
            context["json"] = json.dumps(list(items))
        except EnergyData.DoesNotExist:
            context["countries"] = {"error": "data not found"}
        return context

    
class TiendaTemplateView(TemplateView):
    template_name = 'map.html'

class TeamTemplateView(TemplateView):
    template_name = 'Team.html'
    
class PredictionTemplateView(TemplateView):
    template_name ='prediction.html'

# class Tienda2TemplateView(TeamTemplateView):
#     template_name = 'index2.html'