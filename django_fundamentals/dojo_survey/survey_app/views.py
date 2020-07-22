from django.shortcuts import render, redirect

LANGS = (
    'Python',
    'JavaScript',
    'Java',
    'C#',
)
LOCATIONS = (
    'San Jose',
    'Seatle',
    'Chicago',
    'Online',
)
GENDERS = (
    'Male',
    'Female',
    'Other',
)
HOBBIES = (
    'Biking',
    'Swimming',
    'Hiking',
    'Camping',
)
def index(request):
    context = {
        'locations': LOCATIONS,
        'languages': LANGS,
        'genders' : GENDERS,
        'hobbies' : HOBBIES,
    }
    return render(request, 'index.html',context)

def survey(request):
    if request.method == 'GET':
        return redirect('/')

    # print(request.POST)
    
    request.session['result'] = {
        'name' : request.POST['name'],
        'location' : request.POST['location'],
        'language' : request.POST['language'],
        'gender' : request.POST['gender'],
        'hobbies' : request.POST['hobby_list[]'],
        'comment' : request.POST['comment'],
    }
    return redirect('/result')

def result(request):
    context = {
        'result': request.session['result']
    }       
    return render(request, 'result.html', context)
