from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a = 5 + 6
    return render(request, 'about.html', {'gretting':a})

# def reverse(request):
#     return render(request, 'reverse.html')
#
def home(request):
    return HttpResponse('This is my home')

