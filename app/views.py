from django.shortcuts import render

# Create your views here.

def condition(request):
    return render(request,'if.html',context={'data':'','data1':'python'})


def image(request):
    return render(request,'image.html')