from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "Pages/home.html"
    
class GameListView(TemplateView):
    template_name = "Pages/game_list.html"
    
class DevlogView(TemplateView):
    template_name = "Pages/devlog.html"
    
class ManifestoView(TemplateView):
    template_name = "Pages/manifesto.html"
    
class ContactView(TemplateView):
    template_name = "Pages/contact.html"