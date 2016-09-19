from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Post

def index(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:20]
    paginator = Paginator(post_list, 5) # Show posts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/index.html", {
        'posts': posts
    })

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post.html", {"post": post})
