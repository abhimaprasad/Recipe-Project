from django.shortcuts import render,redirect

from users.forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def register(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"users/login.html")
    return render(request,"users/registration.html",context)

def Login(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request, "usershome.html", context)
            else:
                return render(request, "users/login.html", context)

    return render(request,"users/login.html",context)


def Logout(request):
    logout(request)
    return redirect("signin")