from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


def forum_home(request):
    return render(request, 'forum/home.html')

def practice(request):
    data = {
        'title': 'Это практика',
        'text': 'Вася',
        'link_practice': 'style=font-weight:bold;',
        'link_lesson': '',
        'link_about': '',
        'id': 'practice'
    }
    return render(request, 'forum/practice.html', data)

def lesson(request):
    data = {
        'title': 'Это Lesson',
        'text': 'Петя',
        'link_practice': '',
        'link_lesson': 'style=font-weight:bold;',
        'link_about': ''

    }
    return render(request, 'forum/practice.html', data)

def about(request):
    data = {
        'title': 'Это практика',
        'text': 'Дуся',
        'link_practice': '',
        'link_lesson': '',
        'link_about': 'style=font-weight:bold;'
    }
    return render(request, 'forum/practice.html', data)

def some(request):
    date_time = date.today().strftime('%d/%m/%Y')
    data = {
        'time': date_time
    }

    return HttpResponse(data['time'])
