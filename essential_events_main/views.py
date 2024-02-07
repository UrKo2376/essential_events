from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "essential_events_main/index.html")