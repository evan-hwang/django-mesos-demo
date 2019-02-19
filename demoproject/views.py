from django.http import HttpResponse

def index(request):
    return HttpResponse("Django Mesos demo project by Evan!")