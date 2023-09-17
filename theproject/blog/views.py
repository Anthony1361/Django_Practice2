from django.shortcuts import render
from blog.models import ourBlog

# Create your views here.
def theBlog(request):
    blog = ourBlog.objects.all()
    context  = {
        "blog" : blog
    }
    return render(request, 'blog/index.html', context)
