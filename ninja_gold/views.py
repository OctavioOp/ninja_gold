from django.shortcuts import redirect, render
import random


# Create your views here.
def home(request):
    color= ''
    coin  = request.session.get('coin')
    coin1 = request.session.get('log')

    if int(coin1) > 0:
        log = 'You win some coins!: '+str(coin1) 
        color = '#33FF46'
    elif int(coin1) == 0:
        log = 'well, continue trying!!'
        color = '#33D7FF'
    else:
        log = 'you loseee ... oohh keep trying!: ' +str(coin1)
        color = '#FF3C33'

    request.session['activities'].append(log)
    request.session.save()
    

    print(log)
    context={
        'coin': coin,
        'log': log,
        'coin1': coin1,
        'color': color
    }
    return render(request,'home.html',context)

def random1(min,max,num=1):
    gold = random.randrange(min,max,num)
    return gold

def login(request):
    request.session['name']= 'user'
    request.session['coin'] = 0
    request.session['log'] = 0
    request.session['activities'] = []
    
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