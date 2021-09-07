from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.

def home(request):
    # return HttpResponse("This is my homepage/")
    return render(request,'home.html')

def about(request):
    # return HttpResponse("This is my about/")
    if request.method=="POST":
        FullName=request.POST['FullName']
        emailInfo=request.POST['emailInfo']
        phone=request.POST['phone']
        desc=request.POST['desc']
        contact = Contact(FullName=FullName,emailInfo=emailInfo,phone=phone,desc=desc)
        contact.save()
        print(FullName)
        print("Data has been added to database")
    context = {'myBranch':'CSE'}
    return render(request,'about.html',context)

def info(request):
    # return HttpResponse("This is my info/")
    context = {'name':'Pranav','college':'NITM'}
    return render(request,'info.html',context)

def portfolio(request):
    return HttpResponse("This is my portfolio, with HttpResponse")
    
def help(request):
    # return HttpResponse("This is my help/")
    return render (request,'help.html')

