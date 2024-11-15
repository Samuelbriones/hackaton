from django.urls import path
from APP.Core.view import Main
from APP.Core.view.Main import prediction_view, energy_data

app_name = 'Core'

urlpatterns = [
    path('', Main.MainTemplateView.as_view(), name='index'),
    path('map/',Main.TiendaTemplateView.as_view(), name='map'),
    path('Team/',Main.TeamTemplateView.as_view(), name= 'team'),
    path('prediction/', Main.PredictionTemplateView.as_view(), name = 'prediction'),
    path('CO2/', prediction_view, name='CO2'),
    path('energy_data/', energy_data, name='energy'),
    path('table/', Main.TableTemplateView.as_view(), name='table'),
]