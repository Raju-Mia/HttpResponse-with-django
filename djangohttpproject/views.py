


from django.shortcuts import HttpResponse

def home(request, name):
    myname = "My name is " + name
    return HttpResponse(myname)