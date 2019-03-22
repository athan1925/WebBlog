from django.shortcuts import render


def blog_list(request):
    return render(request, 'blogs-list.html')
# Create your views here.
