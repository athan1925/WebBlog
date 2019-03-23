from django.shortcuts import render
from django.utils import timezone
from .models import Post

def blog_list(request):
    blogs = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogs-list.html', {'blogs': blogs})

def blog_details(request, slug):
    #return HttpResponse(slug)
    poste = Post.objects.get(slug=slug)
    return render(request,'blogs-details.html', {'poste':poste})