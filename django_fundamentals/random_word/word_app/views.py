from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def generate(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    request.session['word'] = get_random_string(length=14)
    print(request.GET)
    return render(request,'index.html')

def reset(request):
    request.session.flush()
    return redirect('/random_word')

