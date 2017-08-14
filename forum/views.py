from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum/index.html', {'posts': posts})
# Create your views here.

def about(request):
    return render(request, 'forum/about.html', {})

def feeling_down(request):
    return render(request, 'forum/feeling_down.html', {})

@login_required(login_url='/accounts/login/')
def post(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum/post.html', {'posts': posts})

def contact(request):
    return render(request, 'forum/contact.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'forum/signup.html', {'form': form})

def hotlines(request):
    return render(request, 'forum/hotlines.html', {})

def references(request):
    return render(request, 'forum/references.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
    else:
        form = PostForm()
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
    return render(request, 'forum/post_edit.html', {'form': form})
