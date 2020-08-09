from django.shortcuts import render,redirect
from shows_app.models import Show
from django.contrib import messages

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
    errors = Show.objects.basic_validator(request.POST)
    valid_shows = Show.objects.filter(title=request.POST['title'])
    if len(valid_shows) > 0:
        errors['title'] = "The show already exists!"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/shows/new')
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
    errors = Show.objects.basic_validator(request.POST)
    valid_shows = Show.objects.filter(title=request.POST['title'])
    if len(valid_shows) > 0 and valid_shows[0].id != show_id:
        errors['title'] = "The show already exists!"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/shows/'+str(show_id)+'/edit')
    show = Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release']
    show.desc = request.POST['desc']
    show.save()
    path = '/shows/' + str(show.id)
    return redirect(path) 

def delete(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')