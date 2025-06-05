from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(query):
    return render(query,"base.html")

def land_registration(query):
    return render(query, "registration.html")
