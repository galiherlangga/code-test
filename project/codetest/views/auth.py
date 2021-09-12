from django.contrib.auth import authenticate, login as auth_login
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from codetest.forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def register(request):
    form = RegistrationForm(request.POST or None)
    error = None
    if (request.method == 'POST'):
        if form.is_valid():
            data = form.save(commit=False)
            data.username = request.POST.get('email')
            data.password = make_password(request.POST.get('mobile_number'))
            data.save()
            messages.success(request,'disable')
            return redirect('register')
        else:
            error = form.errors
    context = {
        'form':form,
        'error_form':error,
    }
    return render(request, 'auth/register.html', context)


def login(request):
    form = LoginForm(request.POST or None)
    if (request.method == 'POST'):
        try:
            user = authenticate(username=form.data['email'], password=form.data['password'])
            if user:
                auth_login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Please check email and use mobile phone number as password')
        except Exception as e:
            return messages.error(request, e)
        # return HttpResponse(form.data['password'])
    context = {
        'form':form
    }
    return render(request, 'auth/login.html', context)