from django.shortcuts import render
from .models import staticModel
from django.conf import settings

# Create your views here.
def index(request):
    sliderData = staticModel.objects.filter(staticType='HS').values()
    heroData = staticModel.objects.filter(staticType="HH").values()
    mediaURL = 'essential_events_main/static/images/'
    context = {
        'slider': sliderData,
        'hero': heroData,
        'media': mediaURL,
    }
    return render(request, "essential_events_main/index.html", context)