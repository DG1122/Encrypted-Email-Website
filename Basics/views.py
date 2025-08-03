from django.shortcuts import render

# Create your views here.
def add(request):
    if request.method=="POST":
        a=int(request.POST.get("n1"))
        b=int(request.POST.get("n2"))
        c=a+b
        return render(request,'Basics/Add.html',{'result':c})
    else:
        return render(request,'Basics/Add.html')
def largest(request):
    if request.method=="POST":
        a=int(request.POST.get("n1"))
        b=int(request.POST.get("n2"))
        c=int(request.POST.get("n3"))
        d=max(a,b,c)
        e=min(a,b,c)
        return render(request,'Basics/largestandsmallest.html',{'result1':d,'result2':e})
    else:
        return render(request,'Basics/largestandsmallest.html')
def calculate(request):
    res=""
    if request.method=="POST":
        c=request.POST.get("btn")
        a=int(request.POST.get("n1"))
        b=int(request.POST.get("n2"))
        if c=="+":
            d=a+b
        elif c=="-":
            d=a-b
        elif c=="*":
            d=a*b
        elif c=="/":
            d=a/b            
        return render(request,'Basics/calculator.html',{'result':d})
    else:
        return render(request,'Basics/calculator.html')   
        