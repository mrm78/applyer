from django.shortcuts import render, redirect
from django.contrib import auth
from .models import user
from orders.models import order
from django.contrib.auth.decorators import login_required

def register(req):
    if req.method == 'GET':
        return render(req, 'register.html', {'email_error':'not-visible', 'password_error':'not-visible'})
    else:
        if req.POST.get('password') != req.POST.get('rpt_password'):
            return render(req, 'register.html', {'email_error':'not-visible', 'password_error':'visible'})
        elif user.objects.filter(email=req.POST.get('email')):
            return render(req, 'register.html', {'email_error':'visible', 'password_error':'not-visible'})
        User = user.objects.create_user(req.POST.get('email'), req.POST.get('phone'),req.POST.get('password'))
        auth.login(req,User)
        return redirect('home')



def login(req):
    if req.method == 'GET':
        return render(req, 'login.html', {'error':'not-visible'})
    else:
        User = auth.authenticate(email=req.POST.get('email'), password=req.POST.get('password'))
        if User:
            auth.login(req, User)
            return redirect('home')
        else:
            return render(req, 'login.html', {'error':'visible'})




@login_required
def panel(req):
    orders = order.objects.filter(user=req.user)
    return render(req, 'panel.html', {
        'orders' : orders,
        'orders_amount' : len(orders),
        
    })
