from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from Three.models import Student, Grade


# 原生加载
def index(request):
    three_index = loader.get_template('three_index.html')

    context = {
        "student_name": "Sunck"
    }
    result = three_index.render(context=context)
    print(result)

    return HttpResponse(result)

def get_grade(request):

    # Student表里的ID为4的行
    student = Student.objects.get(pk=4)
    # 获取所在班级  "student的外键是grade的主键"
    grade = student.s_grad

    return HttpResponse("Grade %s" % grade.g_name)


# 获取所有学生
def get_student(request):

    # 获取ID为1的所有数
    grade = Grade.objects.get(pk=1)
    # set和objects类似
    students = grade.student_set.all()

    context = {
        "students": students
    }

    return render(request, 'student_three_list.html', context=context)