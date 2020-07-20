from django.shortcuts import render
from time import gmtime, strftime
from django.utils import timezone

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "time2": timezone.now(),
    }
    return render(request, 'index.html', context)
