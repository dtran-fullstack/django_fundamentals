from django.shortcuts import render, redirect
from school_students_app.models import School, Students

def index(request):
    context = {
        "schools": School.objects.all(),
        # "students": Students.objects.all()
    }
    return render(request,'index.html', context)

def school(request):
    name = request.POST['school_name']
    city = request.POST['city']
    state = request.POST['state']
    School.objects.create(name=name,city=city,state=state)
    return redirect('/')

def student(request):
    fname = request.POST['first_name']
    lname = request.POST['last_name']
    school = School.objects.get(id=request.POST['school_id'])
    Students.objects.create(first_name=fname, last_name=lname, school= school)
    count = 0
    for student in school.students.all():
        count += 1
    school.stu_count = count
    school.save()
    return redirect('/')

def delete(request):
    print(request.POST)
    for student in School.objects.get(id=request.POST['school_id']).students.all():
        student.delete()
    School.objects.get(id=request.POST['school_id']).delete()
    return redirect('/')

