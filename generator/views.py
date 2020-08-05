from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    

    characters=[chr(i) for i in range(97,123)]
    if request.GET.get('uppercase'):
        characters.extend([chr(i) for i in range(65,91)])
    if request.GET.get('numbers'):
        characters.extend([str(i) for i in range(0,10)])
    if request.GET.get('special'):
        characters.extend(['!','@','#','$','%','^','&','*','(',')'])    
 


    length=int(request.GET.get('length',12))
    thepassword=''
    for i in range(length):  #pylint: disable=unused-variable
        thepassword+=random.choice(characters)

    return  render(request, 'generator/password.html', {'password':thepassword})
