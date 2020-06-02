import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Two.models import Student


def index(request):
    return HttpResponse("Two Views")



def add_student(request):

    student = Student()
    student.s_name = 'Jerry%d' % random.randrange(100)
    student.save()

    return HttpResponse("<h1>Add Success %s</h1>" % student.s_name)


def get_student(request):

    students = Student.objects.all()

    for student in students:
        print(student.s_name)

    context = {
        "hobby": "Play Game!!",
        "eat": "吃吃吃！！",
        "students": students
    }

    return render(request, 'student_list.html', context=context )


def update_student(request):

    student = Student.objects.get(pk=1)
    student.s_name = 'Jack'
    student.save()

    return HttpResponse("Student Update Success")


def delete_student(request):

    student = Student.objects.get(pk=3)
    student.delete()

    return HttpResponse("Student Delete Success")