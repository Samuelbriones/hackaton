from django.urls import path
from APP.Core.view import Main

app_name = 'Core'

urlpatterns = [
    path('', Main.MainTemplateView.as_view(), name='index'),
    path('tienda/',Main.TiendaTemplateView.as_view(), name='tienda'),
    path('fertilizante/',Main.FertilizanteTemplateView.as_view(), name= 'fertilizante'),
    path('Team/',Main.TeamTemplateView.as_view(), name= 'team')
]