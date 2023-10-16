from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentRegistration
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Create your views here.

@never_cache
@login_required(login_url='signin')
def admin_page(request):
    if request.user.is_superuser:
        
        if request.GET.get('search') is not None :
            search=request.GET.get('search')
            users=User.objects.filter(username__icontains=search)
        else:
             users=User.objects.all()
        context={
            'users':users
             }
          
        return render(request,'admin.html',context)
    else:
        return redirect('home')

@never_cache
@login_required(login_url='signin')
def edit_user(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        
        fm = StudentRegistration(request.POST, instance=pi)
        
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Edited Succefully')
        
    else:
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(instance=pi)
        
    return render(request, 'edit.html', {'form' : fm})

@never_cache
@login_required(login_url='signin')
def delete_user(request,user_id):
    user=User.objects.get(id=user_id)
    user.delete()
    return redirect('admin_page')
    