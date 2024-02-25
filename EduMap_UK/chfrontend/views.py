from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages

# View para a página inicial
def home(request):
    return render(request, 'chfrontend/home.html')

# View para a página base
def base(request):
    return render(request, 'chfrontend/base.html')

# View para a página de mapas
def maps(request):
    return render(request, 'chfrontend/places_base.html')

# View para o formulário de registro
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já existe.')
            return redirect('chfrontend:register')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('chfrontend:home')
    else:
        return render(request, 'chfrontend/register.html')

# View para autenticação de usuários
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chfrontend:maps')
        else:
            messages.error(request, 'Usuário ou senha inválidos. Por favor, tente novamente ou realize um novo cadastro.')
            return redirect('chfrontend:home')
    return render(request, 'chfrontend/home.html')
