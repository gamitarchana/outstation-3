from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Login(TemplateView):
    template_name = 'login/login.html'

def login(request):
    return render(request, 'login/login.html')
