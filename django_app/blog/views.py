from django.shortcuts import render


def blog(request):
    context = {}
    return render(request, 'blog/index.html', context)
