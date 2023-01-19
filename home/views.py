from django.shortcuts import render,HttpResponse
from home.models import Contact
from home.models import Support

# Create your views here.
def index(request):
    
    # return HttpResponse("This is my home page (/)")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("This is my about page")
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name1 = request.POST['name']
        email1= request.POST['email']
        message1=request.POST['message']
        
        ins = Contact(name=name1,email=email1,message=message1)
        ins.save()
        print("the data has been saved to database")
    # return HttpResponse("This is my contact number")
    return render(request,'contact.html')

def projects(request):
    
    # return HttpResponse("This is my project page")
    return render(request,'projects.html')

def support(request):
    if request.method=="POST":
        first=request.POST['first']
        last=request.POST['last']
        email=request.POST['email']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        query=request.POST['query']
        
        ins = Support(firstname=first,lastname=last,email=email,city=city,state=state,zip=zip,query=query)
        ins.save()
        print("works perfectly")
    return render(request,'support.html')