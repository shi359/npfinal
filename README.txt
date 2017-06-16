create environment:
python -m venv myvenv

activate environment:
myvenv\Scripts\activate.bat

install django:
pip install django==1.6.6

start new project:
python myvenv\Scripts\django-admin.py startproject mysite

update database:
python manage.py makemigrations NPFinal
python manage.py migrate NPFinal

run server:
python manage.py runserver

interact with database:
python manage.py shell
from NPFinal.forms import *
from NPFinal.models import *
Post.objects.all() # list record
Post.objects.create(title = "test title",img_src = "QQ",text = "test text", hash_tag="['asd', 'a']") # create record

Architecture:
nanoDick(project)-nanoDick(project configuration)
                 -NPFinal(application)

how it works:
1. in browser key "127.0.0.1:8000", server search pattern matched in nanoDick\nanoDick\urls.py (which include url pattern in nanoDick\NPFinal\urls.py)
2. "127.0.0.1" match "url(r'^$', views.post_list, name='post_list')", go to NPFinal\views.py to see what to do
3. in post_list, "render(request, 'NPFinal/index.html', {'srcs':srcs})" return 'templates/NPFinal/index.html' decorated by "srcs"

how upload image works:
1. see upload function in static/js/myutils.js 
2. see upload function in NPFinal\views.py