from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "app/index.html")

def todo(request):
    return render(request, 'app/todo.html')

def log(request):
    return render(request, 'app/log.html')