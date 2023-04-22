from django.shortcuts import render
from .models import Blogs

# Create your views here.


def blogs(request):
    queryset = Blogs.objects.all()
    context = {'blogs': queryset}
    return render(request, 'blogs/blogs.html', context)


def blog_details(request, pk):
    queryset = Blogs.objects.get(id=pk)
    context = {'blog':queryset}
    return render(request, 'blogs/blog_details.html', context)

