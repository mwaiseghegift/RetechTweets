from django.shortcuts import render

def ProfileDetailView(request, username, *args, **kwargs):
    
    content = {
        "username":username
    }
    
    return render(request, 'profile/profile_detail.html', content)