from django.views.generic import TemplateView
from django.db.models import Max
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json
from ..models import EnergyData

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
        'renewables_equivalent',
        'renewable_electricity_capacity',
        'access_to_clean_fuels',
        'low_carbon_electricity'
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
    template_name = 'team.html'
    
class PredictionTemplateView(TemplateView):
    template_name ='prediction.html'
    
class TableTemplateView(TemplateView):
    template_name='table.html'
    
@csrf_exempt
@require_POST
def prediction_view(request):
    from prediction import CO2_prediction
    try:
        
        data = json.loads(request.body)

        electricity = float(data['electricity'])
        clean_fuels = float(data['clean_fuels'])
        fossil = float(data['fossil'])
        renewables = float(data['renewables'])
        nuclear = float(data['nuclear'])
        kWh_per_person = float(data['kWh_per_person'])
        
        cO2 = CO2_prediction(electricity, clean_fuels, 
                             fossil, renewables, nuclear, kWh_per_person) 
        
        return JsonResponse(cO2, safe=False, status=200)
    
    except json.JSONDecodeError as e:
        print(e)
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    
    except Exception as e:
        print(e)
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_GET
def energy_data(request):
    try:
        objects = list(EnergyData.objects.values('entity', 'year',
                                            'electricity_from_fossil_fuels',
                                            'electricity_from_nuclear',
                                            'electricity_from_renewables',
                                            'co2_emissions'))
        
        return JsonResponse(objects, safe=False, status=200)
    except Exception as e:
        print(e)
        return JsonResponse({'error': str(e)}, status=500)
    