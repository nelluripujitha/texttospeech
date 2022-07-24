from django.shortcuts import render, redirect
import pyttsx3


# Create your views here.
def home(request):
    return render(request, "one.html")


def some(request):
    var = request.GET['inp']
    obj = pyttsx3.init()
    obj.say(var)
    obj.runAndWait()
    return redirect('/')
