from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect

# def email_login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    # actual_derocator = user_passes_test(
        # lambda condition : 
        # condition.is_active,
        # login_url=login_url,
        # redirect_field_name=redirect_field_name
    # )
    # if function:
        # return actual_derocator(function)
    # return actual_derocator

def email_login_required(function):
    def wrapper(request, *args, **kw):
        user=request.user  
        if not (user.id and request.session.get('code_success')):
            return HttpResponseRedirect('/login/')
        else:
            return function(request, *args, **kw)
    return wrapper
