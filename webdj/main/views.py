from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная станица',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BWM',
            'age': 18,
            "hobby": "Football"
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
