from django.shortcuts import render


def blog(request):
    context = {}
    return render(request, 'blog/index.html', context)


def part2_layout1(request):
    context = {}
    return render(request, 'part2/layout1.html', context)
