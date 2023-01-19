from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {'name' : 'Ritik','age' : '20'}
    # return HttpResponse("This is my home page (/)")
    return render(request,'index.html',context)

def about(request):
    # return HttpResponse("This is my about page")
    return render(request,'about.html')

def contact(request):
    # return HttpResponse("This is my contact number")
    return render(request,'contact.html')

def projects(request):
    # return HttpResponse("This is my project page")
    return render(request,'projects.html')

def support(request):
    context = {'name' : 'Ritik'}
    return render(request,'support.html',context)