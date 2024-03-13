from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def machine(request):
    return HttpResponse('welcome to Django, studymart')
    # return render(request)