from django.shortcuts import render
#from django.http import HttpResponse
from .forms import InputForm

def home_view(request):
    context={}
    context['form']= InputForm()
    return render(request, "home.html", context)


'''
def index(request):
    return HttpResponse("Hello Django, This is my first page")
# Create your views here.

'''
