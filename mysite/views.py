from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.
def interface (request):
    return render(request ,'page/index.html')