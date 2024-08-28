from django.http import HttpResponse
from django.shortcuts import render
def home(Request):
    return HttpResponse("My name ia Anees Zafar Iqbal")


def contact(request):
    return render(request,'index.html')