from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PostForm, ImageForm
from .models import *


def index(request):
    return render(request, 'index.html')


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category_id=slug)
    return render(request, 'category-detail.html', locals())


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    image = post.get_image
    images = post.images.exclude(id=image.id)
    return render(request, 'post-detail.html', locals())


def add_post(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        formset = ImageFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.none())
        if post_form.is_valid() and formset.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()

            for form in formset.cleaned_data:
                 image = form['image']
                 Image.objects.create(image=image, post=post)
            return redirect(post.get_absolute_url())
    else:
        post_form = PostForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'add-post.html', locals())


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.user:
        ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
        post_form = PostForm(request.POST or None, instance=post)
        formset = ImageFormSet(request.POST or None, request.FILES or None, queryset=Image.objects.filter(post=post))
        if post_form.is_valid() and formset.is_valid():
            post = post_form.save()
            images = formset.save(commit=False)
            for image in images:
                image.post = post
                image.save()
            return redirect(post.get_absolute_url())
        return render(request, 'update-post.html', locals())
    else:
        return HttpResponse('<h1>403 Forbidden</h1>')


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.add_message(request, messages.SUCCESS,'Успешно удалено!')
        return redirect('home')
    return render(request, 'delete-post.html')








