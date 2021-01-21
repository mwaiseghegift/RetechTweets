from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def login_view(request, *args, **kwargs):
    
    form = AuthenticationForm(request, data=request.POST or None)
    
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect('/')
    
    context = {
        "form":form
    }
    
    return render(request, "accounts/login.html", context)

def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect('accounts:login')
    
    context = {
        "form": None
    }
    return render(request, "accounts/logout.html", context)

def UserCreationView(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password1"))
        login(request, user)
        return redirect('accounts/login/')
        
    context = {
        "form":form
    }
    return render(request, "accounts/register.html", context)