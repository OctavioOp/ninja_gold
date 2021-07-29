from typing import Counter
from django.shortcuts import redirect, render, HttpResponse
from django.utils.crypto import get_random_string


# Create your views here.

def home(request):
    counter = request.session.get('counter')
    
    if 'counter' not in request.session:
        request.session['counter'] = 0

    #request.session['counter'] += 1

    if request.session['counter'] == 10:
        word = 'error 404 '
    else:
        request.session['counter'] += 1
        word = get_random_string(length=14)

    

    context = {
        'word': word,
        'counter': counter
        
    }
    return render(request,'index.html',context)


def login(request):
    request.session['user'] = 'user'
    request.session['counter']= 0
    return redirect('../random/home')

def logout(request):
    del request.session['user']
    del request.session['counter']
    return redirect('../random/login')


