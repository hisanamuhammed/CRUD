from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


# from . models import Phone

from django.contrib.auth import authenticate,login,logout

# Create your views here.

@never_cache
@login_required(login_url='signin')
def home(request):
    # phone = Phone.objects.all()
    # context = {
    #     'phones' : phone
    # }
    return render(request,'home.html')  

@never_cache
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name                                                                                         

        myuser.save()

        messages.success(request, "Successfully created your account.")

        return redirect('signin') #Once all the credentials are saved, it is redirected to signin page

    return render(request, 'signup.html') #If, if case doesn't get saved, it is rendered to signup page itself 

@never_cache
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            pass1 = request.POST['pass1']

            user=authenticate(username=username, password=pass1)

            if user is not None:
                # request.session
                login(request, user)
                # name = user.name
                return render(request,"home.html",)

            else:
                messages.error(request, "Incorrect username or password !")
                return redirect('signin')

        return render(request, 'signin.html')

# @login_required(login_url='signin')
# @never_cache
def signout(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect('home')
