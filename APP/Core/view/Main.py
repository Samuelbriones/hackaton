from django.views.generic import TemplateView

class MainTemplateView(TemplateView):
    template_name = 'index.html'
    
class TiendaTemplateView(TemplateView):
    template_name = 'map.html'

class TeamTemplateView(TemplateView):
    template_name = 'Team.html'

# class Tienda2TemplateView(TeamTemplateView):
#     template_name = 'index2.html'