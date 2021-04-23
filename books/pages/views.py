from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

def render_home_page(request):
    return render(request, 'home.html')
