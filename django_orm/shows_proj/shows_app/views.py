from django.shortcuts import render,redirect
from shows_app.models import Show

def to_shows(request):
    return redirect('/shows')

def main(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request,'main.html',context)

def new(request):
    return render(request,'new.html')

def new_process(request):
    print(request.POST)
    show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release'],
        desc = request.POST['desc']
    )
    path = '/shows/' + str(show.id)
    return redirect(path)

def one_show(request,show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request,'show.html', context)

def edit (request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request,'edit.html',context)

def edit_process(request, show_id):
    print(request.POST)
    show = Show.objects.get(id=show_id)
    if request.POST['title'] != None:
        show.title = request.POST['title']
    if request.POST['network'] != None:
        show.network = request.POST['network']
    if request.POST['release'] != None:    
        show.realease_date = request.POST['release']
    if request.POST['desc'] != None:
        show.desc = request.POST['desc']
    show.save()
    path = '/shows/' + str(show.id)
    return redirect(path) 

def delete(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')