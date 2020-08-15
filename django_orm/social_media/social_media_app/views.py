from django.shortcuts import render, redirect
from social_media_app.models import *
from django.contrib import messages
import bcrypt

# LOGIN

def to_login(request):
    return redirect('/login')

def render_login_register(request):
    return render(request,'reg_log.html')

def register(request):
    errors = User.objects.validator(request.POST)
    users = User.objects.filter(email = request.POST['email'])
    if len(users) > 0:
        errors['email_address'] = "This email is already registered!"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()    
        User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            dob = request.POST['dob'],
            email = request.POST['email'], 
            password=pw_hash,
        ) 
    return redirect("/")   

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if user: 
            logged_user = user[0] 
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['name'] = logged_user.first_name + " " + logged_user.last_name
                request.session['uid'] = logged_user.id
                return redirect('/wall')
    messages.error(request,"Invalid email or incorrect password!")
    return redirect("/")

def logout(request):
    request.session.flush()
    return redirect('/')

#WALL

def render_wall(request):
    if 'name' not in request.session:
        return redirect('/')
    context = {
        "messages" : Message.objects.all()
    }
    return render(request,'wall.html',context)

def post(request):
    Message.objects.create(
        message = request.POST['message'],
        user = User.objects.get(id = request.session['uid']),
    )
    return redirect('/wall')

def profile(request, uid):
    context = {
        'user': User.objects.get(id=uid)
    }
    return render(request, 'profile.html', context)

def edit(request,mess_id):
    message = Message.objects.get(id = mess_id)
    if request.method == 'POST':
        message.content = request.POST['content']
        message.save()
        return redirect(f'/profile/{str(message.user.id)}')
    context = {
        'edit_mess': message
    }
    return render(request, 'edit.html', context)

def delete(request, mess_id):
    return redirect('/wall')

def comment(request,mess_id):
    Comment.objects.create(
        content = request.POST['comment'],
        message = Message.objects.get(id = mess_id),
        user = User.objects.get(id = request.session['uid']),
    )
    return redirect('/wall')