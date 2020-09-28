from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Home Page')

def help(request):
    my_dict = {'head_title': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=my_dict)