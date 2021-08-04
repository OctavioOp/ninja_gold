from django.shortcuts import redirect, render
import random


# Create your views here.
def home(request):
    color= ''
    coin  = request.session.get('coin')
    coin1 = request.session.get('log')

    if int(coin1) > 0:
        request.session['activities'].append({
            'text': 'You win some coins!: '+str(coin1) ,
            'gold': coin1
        })
    else:
        request.session['activities'].append({
            'text': 'you loseee ... oohh keep trying!: ' +str(coin1) ,
            'gold': coin1
        })
    if coin < 0:
        return render(request,'lose.html')

  
    request.session.save()

    context={
        'coin': coin,
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

def bet(request):
    if request.method == 'GET':
        return render(request,'form.html')
    else:

        bet = request.POST['bet']
        min_farm = request.POST['min_farm']
        max_farm = request.POST['max_farm']
        min_cave = request.POST['min_cave']
        max_cave = request.POST['min_cave']
        min_house = request.POST['min_house']
        max_house = request.POST['min_house']
        min_casino = request.POST['min_casino']
        max_casino = request.POST['min_casino']
        context={

        }
        return render(request,'home.html',context)
