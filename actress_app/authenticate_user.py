from django.shortcuts import render

def authenticate_user(myfun):
    def inner(request):
        if request.user.is_authenticated:
            return render(request,'actress_app/home.html')
        else:
            return myfun(request)
    return inner