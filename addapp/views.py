from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,'base.html')
def add(request):
    try:
        a=request.GET['t1']
        x=int(a)
        b=request.GET['t2']
        y=int(b)
        res={}
        res["add"] = x+y
        res["sub"] = x-y
        res["mul"] = x*y
        res["div"] = x/y
        res["mod"] = x%y
        res["fdiv"] = x//y
        return render(request,'display.html',{"result":res})
    except(ValueError):
        return HttpResponse("invalid input")


# Create your views here.
