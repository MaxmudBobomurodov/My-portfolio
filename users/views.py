from django.shortcuts import render


def my_profile(request):
    return render(request, 'index.html')


def teacher_profile(request):
    return render(request, 'teacher.html')