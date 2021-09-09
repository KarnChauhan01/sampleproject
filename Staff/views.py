from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomerRegister
# from .models import User,Customer
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
def user_registeration(request):
    if request.method== 'POST':
        form = CustomerRegister(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request,'registration successfull!!')
            # return redirect('user_login')
            return HttpResponse('Registerd')
        messages.error(request,'invalid!!')
    
    form = CustomerRegister
    return render(request,template_name='Staff/register.html',context={'register_form':form})