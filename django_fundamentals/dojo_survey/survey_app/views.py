from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def output(request):
    if request.method == "POST":
        context = {
            "name" : request.POST["full_name"], 
            "location" : request.POST["location"],
            "language" : request.POST["language"],
            "gender" : request.POST["gender"],
            "vehicle" : {
                "ve1" : request.POST["vehicle1"],
                "ve2" : request.POST["vehicle2"],
                "ve3" : request.POST["vehicle3"],
            },
            "comment" : request.POST["comment"],
        }
        return render(request, 'index2.html', context)
    return render(request, 'index2.html')
       

