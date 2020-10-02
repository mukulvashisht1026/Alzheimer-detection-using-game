from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@login_required
def home(request):
    return render(request,'HomePage/HomePage.html',{})

@csrf_exempt
def profile(request):
    if(request.method == 'POST'):
        print("hello world \n\n\n\n\n\ hello")
        print(request.POST.get('inpH'))
        print(request.POST.get('level'))

    return render(request, 'profile/index.html', {})