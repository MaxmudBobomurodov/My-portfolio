from django.shortcuts import render


def my_profile(request):
    return render(request, 'about_me.html')


def teacher_profile(request):
    return render(request, 'teacher.html')