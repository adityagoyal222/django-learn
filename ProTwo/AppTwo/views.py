from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(request):
    return HttpResponse('Home Page')

def help(request):
    my_dict = {'head_title': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=my_dict)

def users(request):
    user_list = User.objects.order_by('first_name')
    my_dict = {'user_list': user_list}
    return render(request, 'AppTwo/user.html', context=my_dict)