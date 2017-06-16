from django.shortcuts import render, redirect
from django.conf import settings
from django.http import *
from .models import Post
from .forms import *
from django.contrib import messages
import json
import random
import string

# Create your views here.
def post_list(request):
    srcs = ['/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg', '/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg']
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'NPFinal/index.html', {'srcs':srcs})

# return login html
def login(request):
    # srcs = ['/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg', '/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg']
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        m = form['account'].value()
        p = form['password'].value()
        user = Reg.objects.filter(mail=m)[0]
        if not user:
            return render(request, 'NPFinal/login_redirect.html', {'msg':'user not exist'})
        if not user.password == p:
            return render(request, 'NPFinal/login_redirect.html', {'msg':'oops, wrong password'})
        if form.is_valid():
            return render(request, 'NPFinal/login_redirect.html', {'msg':'login successfully'})
    else:
        form = LoginForm()           
    return render(request, 'NPFinal/login.html', {'form': form})

# return register html
def register(request):
    srcs = ['/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg', '/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg']
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'NPFinal/register_redirect.html', {'msg':'register successfully'})

        else:
            return render(request, 'NPFinal/register_redirect.html', {'msg':'register fail'})
    else:
        form = RegForm()        
    return render(request, 'NPFinal/register.html', {'form': form})

def upload(request):
    if request.method == 'POST':
        # store file
        #print(settings.IMAGES_ROOT+request.FILES['image'].name)
        def rand_name():
            charset = string.ascii_uppercase + string.ascii_lowercase + string.digits
            return ''.join(random.choice(charset) for _ in range(6))

        file_exten = request.FILES['image'].name.split('.')[-1]
        imgname = rand_name() + '.' + file_exten
        destination_path = open(settings.IMAGES_ROOT+ imgname, "wb+")
        image = request.FILES['image']
        for chunk in image.chunks():
            destination_path.write(chunk)
        destination_path.close()
        Post.objects.create(
            title = "test title",
            img_src = settings.IMAGES_ROOT+imgname,
            text = "test text",
            hash_tag = ['1','2','3'],
        )
        
        #handle_uploaded_file(request.FILES['file'])
        return HttpResponse(status=200)

def post(request):
    return render(request, 'NPFinal/demo.html', {'src': '/static/images/home-img-3.jpg'})

def base(request):
    return render(request, 'NPFinal/base.html', {})
	
def login_redirect(request):
    return render(request, 'NPFinal/login_redirect.html',{})






