from django.shortcuts import render
from django.http import HttpResponse

from app.models import People



#create your views here.
def home(request):
    return render(request, 'home.html')

def insert(request):
    if request.method == "POST":
        name=request.POST.get('name')
        school=request.POST.get('school')
        email=request.POST.get('email')

        person=People(name=name,school=school,email=email)
        person.save() #saving in the db

      #  print(name,school,email)

    return render(request, 'home.html')

def people(request):
    d=People.objects.all()
    context={"data":d}
    return render(request,'people.html',context) #we give people.html access to the data