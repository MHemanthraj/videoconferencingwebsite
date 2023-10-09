from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def register(request):
    form = CreateUserForm()

    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Registration successful' +""+ user)
            return redirect('login')
        
    context = {'form':form}
    return render(request, 'register.html', context)


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'incorrect credentials. please try again')

    context={}
 
    return render(request, 'login.html' ,context)

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.username})

@login_required
def videocall(request):
    return render(request, 'videocall2.html', {'name': request.user.username})

@login_required
def logout_view(request):
    logout(request)
    return redirect("/login")


@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'joinroom.html')