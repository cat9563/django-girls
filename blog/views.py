from django.shortcuts import render
from django.utils import timezone
from .models import BlogPost
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
    blogposts = BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'blogposts': blogposts})

def post_detail(request, pk):
    blogpost = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'blogpost': blogpost})
