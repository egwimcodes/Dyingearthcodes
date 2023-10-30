from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="login-page")
def homePage(request):
    return render(request, "home_body.html")
