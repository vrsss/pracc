from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter()
    return render(request, 'blog/index.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog-single-post.html', {'post': post})
def gallery(request):
    return render(request, 'blog/gallery.html', {})
