from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm

from django.http import HttpResponse


def mainView(request):
    posts = {"posts": Post.objects.all()}
    return render(request, "board/index.html", posts)


def detailView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "board/detail.html", {"post": post})


def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            #post = form.save(commit=False)
            post = form.save()
        return redirect("board:detail", pk=post.id)
    else:
        form = PostForm()
        return render(request, "board/newpost.html", {'form': form})


def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("board:mainview")


def updatePost(request, pk):
    origin_post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=origin_post)
        if form.is_valid():
            #post = form.save(commit=False)
            post = form.save(commit=False)
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['text']
            post.save()
            return redirect("board:detail", pk=pk)
    form = PostForm(instance=origin_post)
    return render(request, "board/newpost.html", {'form': form})