from django.shortcuts import render, redirect
from django.http import Http404

from .models import Profile
from .forms import ProfileForm

def ProfileDetailView(request, username, *args, **kwargs):  
    qs = Profile.objects.filter(user__username=username)
    if not qs.exists():
        raise Http404
    profile_obj = qs.first()
    
    content = {
        "username":username,
        "profile":profile_obj,
    } 
    return render(request, 'profiles/profile_detail.html', content)

def ProfileUpdateView(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("accounts/login?next=profile/update")
    user = request.user
    user_data = {
        "first_name":user.first_name,
        "last_name":user.last_name,
        "email":user.email,
        }
    user_profile = user.profile
    form = ProfileForm(request.POST or None, instance=user_profile, initial=user_data)
    if form.is_valid():
        profile_obj = form.save(commit=False)
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email_address = form.cleaned_data.get("email_address")
        
        user.first_name = first_name
        user.last_name = last_name
        user.email_address = email_address
        user.save()
        profile_obj.save()
        
    context = {
        "form":form
    }
    return render(request, 'profiles/profile_form.html', context)