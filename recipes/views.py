from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'recipes/home.html',context={
        'nome':'Victo Hugo',
    })

def about(request):
    return HttpResponse("Sobre")

def contact(request):
    return HttpResponse("Contato")
