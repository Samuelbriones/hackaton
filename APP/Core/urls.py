from django.urls import path
from APP.Core.view import Main

app_name = 'Core'

urlpatterns = [
    path('', Main.MainTemplateView.as_view(), name='index'),
    path('map/',Main.TiendaTemplateView.as_view(), name='map'),
    path('Team/',Main.TeamTemplateView.as_view(), name= 'team')
]