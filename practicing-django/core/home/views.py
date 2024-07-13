from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    people = [
        {'name':'Pranit','age' : 23},
        {'name':'Pratik','age' : 20},
        {'name':'Biku','age' : 13},
        {'name':'Vicky','age' : 21},
        {'name':'Aaru','age' : 13}
    ]

    data = ['fruits','vegetables','meat']


    return render(request,"index.html",context={'people':people,'data':data ,'page':'home'})
def contact(request):
    context = { 'page':'contact' }
    return render(request,"contact.html",context)

def about(request):
    context = { 'page':'about' }
    return render(request,"about.html",context)



