from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Posts
from .forms import PostForm
from django.core.paginator import Paginator


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Associate the post with the current user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('posts:post_list')  # Redirect to the post list view
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})


def post_list(request):
    posts = Posts.objects.all().order_by('-created_at')  # Get all posts ordered by creation date
    paginator = Paginator(posts, 3)  # Show 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/post_list.html', {'page_obj': page_obj})
