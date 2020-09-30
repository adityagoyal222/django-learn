from django.shortcuts import render
from django.http import HttpResponse
# from AppTwo.models import User
from AppTwo.forms import UserForm

# Create your views here.
def index(request):
    return HttpResponse('Home Page')

def help(request):
    my_dict = {'head_title': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=my_dict)

def users(request):
    form = UserForm

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'AppTwo/signup.html', context={'form':form})