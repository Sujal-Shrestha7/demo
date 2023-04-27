from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Tags, Task
from .forms import BlogPostForm, TaskForm, TagsForm
from django.contrib import messages

# Create your views here.


def posts(request):
    posts = BlogPost.objects.all()
    tasks = Task.objects.all()
    context = {'posts': posts, 'tasks': tasks}
    return render(request, 'posts/posts.html', context)


def create_post(request):
    form_type = 'BlogPost'
    author = request.user
    blog_post = BlogPost.objects.filter(author=author)
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = author
            blog_post.save()
            messages.success(request, 'Created Successfully !!!')
            return redirect('account')
    context = {'form': form, 'form_type': form_type, 'blog_posts': blog_post}
    return render(request, 'posts/post_form.html', context)


@login_required(login_url='login')
def edit_post(request, pk):
    form_type = 'post'
    queryset = get_object_or_404(BlogPost, id=pk)
    form = BlogPostForm(instance=queryset)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully !!!')
            return redirect('account')
    context = {'form': form, 'form_type': form_type}
    return render(request, 'posts/post_form.html', context)


@login_required(login_url='login')
def delete_post(request, pk):
    queryset = get_object_or_404(BlogPost, id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Deleted Successfully !!!')
        return redirect('account')
    return render(request, 'confirm_delete.html', context={'queryset': queryset})
