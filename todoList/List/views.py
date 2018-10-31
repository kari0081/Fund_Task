from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Student task list</h1>")

def detail(request, tasks_id):
    return HttpResponse("<h2>tasks id " + str(tasks_id) + "</h2>")

