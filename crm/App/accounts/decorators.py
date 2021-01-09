from django.http import HttpResponse
from django.shortcuts import redirect

def unathenticated_user(view_func):
    def wrappers(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("accounts:home")
        else:
            return view_func(request, *args, **kwargs)
    return wrappers   

def user_allow(roles=()):
    def wrappers(view_func):
        def arguments_wrappers(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not allow to see this page")
        return arguments_wrappers
    return wrappers

def only_admin(view_func):
    def wrappers_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            if group == 'customer':
                return redirect('accounts:user-page')
            if group == 'admin':
                return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("This user does not have any permision")
    return wrappers_func