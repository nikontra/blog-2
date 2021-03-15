from django.shortcuts import render

def home(request):
    news = [
        {
            'title': 'Наша первая статья',
            'text': 'Полный текст статьи',
            'date': '1 марта 2021 года',
            'autor': 'Джон'
        },
        {
            'title': 'Наша вторая статья',
            'text': 'Полный текст статьи',
            'date': '14 марта 2021 года',
        }
    ]
    data = {
        'news': news,
        'title': 'Главная страница'
    }

    return render(request, 'blog/home.html', data)

def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Страница контакты'})
