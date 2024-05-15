from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def remaining(request):
    return render(request, 'remaining.html')

def completed(request):
    return render(request, 'completed.html')

def add(request):
    return render(request, 'add_task.html')

def delete(request):
    return render(request, 'delete_task.html')

def details(request):
    return render(request, 'task_detail.html')