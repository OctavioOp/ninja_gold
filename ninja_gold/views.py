from django.shortcuts import redirect, render
import random

coin = 0
# Create your views here.
def home(request):
    coin  = request.session.get('coin')
    coin1 = request.session.get('log')

    if int(coin1) > 0:
        log = 'Has ganadooo!: '+str(coin1) 
    elif int(coin1) == 0:
        log = 'Bienvenido!!'
    else:
        log = 'Has perdidooooo!: ' +str(coin1)

    print(log)
    context={
        'coin': coin,
        'log': log
    }
    return render(request,'home.html',context)

def random1(min,max,num=1):
    gold = random.randrange(min,max,num)
    return gold

def login(request):
    request.session['name']= 'user'
    request.session['coin'] = 0
    request.session['log'] = 0
    return redirect('/gold/home')

def process(request,uri):
    if uri == 'farm':
        gold = random1(10,20,1)
    elif uri == 'cave':
        gold = random1(5,10,1)
    elif uri == 'house':
        gold = random1(2,5,1)
    elif uri == 'casino':
        gold = random1(-50,50,1)
    print(gold)
    request.session['coin'] = request.session['coin'] + gold
    request.session['log'] = gold 
    return redirect('/gold/home')