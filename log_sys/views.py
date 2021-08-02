from typing import ContextManager
from django.shortcuts import redirect, render

'''
user = {
    'name': ['marco', 'polo','juan'],
    'pass': ['1234', 'asd','soto'],
}
'''
lista = [{'name': 'juan', 'pass': 'soto'}, {'name': 'amigo', 'pass': 'pass'}]
# Create your views here.


def login(request):
    mensaje = ''

    if request.method == 'GET':
        return render(request, 'log.html')
    else:
        user = next(
            (u for u in lista if u['name'] == request.POST['name']), None)
        print(user)
        if user == None:
            mensaje = 'Not found'
            context = {
            'mensaje': mensaje
            }
            return render(request, 'log.html', context)

        elif user['pass'] != request.POST['pass']:
            mensaje = 'Not found'
            context={
            'mensaje': mensaje
            }
            return render(request,'log.html',context)

        elif user['name']==request.POST['name'] and user['pass']==request.POST['pass']:
            request.session['name'] = request.POST['name']
            return redirect('/log/home')

            

            
'''
    if request.method == 'GET':
        return render(request, 'log.html')
    else:
        if request.POST['name'] in user['name']:
            aux = user['name'].index(request.POST['name'])
            if request.POST['pass'] == user['pass'][aux]:
                request.session['name'] = request.POST['name']
                return redirect('/log/home')
            else:
                mensaje = 'Not found'
                context={
                'mensaje': mensaje
                 }
            return render(request,'log.html',context)

        else:
            mensaje = 'Not found'
            context={
                'mensaje': mensaje
            }
            return render(request,'log.html',context)

    print(aux)  

    
        print('Nombre: ', request.POST['name'])
        print('Pass: ', request.POST['pass'])
        if request.POST['pass']== user['pass']:
         request.session['name'] = request.POST['name']
         return redirect('/log/home')
        else:
            context= {
                'mensaje' : 'error Usuario o pass no encontrado'
            }
            return render(request,'log.html',context)
'''     
def home(request):
    return render(request,'home.html')
'''
def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html')
    else:
        new_user = {'name' : request.POST['name'],'pass': request.POST['pass']}
        lista.append(new_user)
        mensaje = 'Usuario creado'
        redirect ('/login')
'''
