OSS_project
=================
# 1. 장고 프레임워크의 개념 알기!
## (이미지 클릭시 동영상으로 이동합니다.)

[![장고프레임워크](http://img.youtube.com/vi/04FVxBOX42A/maxresdefault.jpg)](https://youtu.be/04FVxBOX42A?t=0s) 

------------------------------
</br>

# 2. 장고 프레임워크를 사용해 웹페이지 만들어보기
## 2.1 장고 설치하기 
터미널창에서 파이썬 패키지 관리자인 pip를 사용하여 django 프레임워크를 설치한다. 
```bash
$ pip install django
```
</br>

## 2.2 프로젝트 생성하기
장고 프레임워크 명령어인 starproject를 통해 프로젝트를 생성한다.
```bash
$ django-admin startproject OSS_project
```
프로젝트 생성이 완료될 시의 폴더(디렉토리)구조
> 이때 ***manage.py***는 우리가 자주 이용하게 될 유틸리티이다. 
```
OSS_project/
    manage.py
    OSS_project/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
</br>

## 2.3 데이터베이스 생성하기
***manage.py*** 를 사용하여 데이터베이스 생성
> 완료되면 OSS_project/OSS_project 내에 db.sqlite3 파일이 생성된다.
```bash
$ OSS_project
$ python manage.py migrate
```
</br>

## 2.4 서버 가동해보기
***manage.py***를 사용하여 서버를 가동시켜본다. 
```bash
$ python manage.py runserver 
```
> 실행하면 다음과 같은 실행문이 뜨는데 http://127.0.0,1:8000/ 부분이 현재 우리 서버의 주소다
```
PS C:\Users\An\Desktop\Django\OSS_python_django\OSS_project> python manage.py runserver 
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 20, 2020 - 18:37:03
Django version 3.1.4, using settings 'OSS_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[20/Dec/2020 18:37:15] "GET / HTTP/1.1" 200 16351
[20/Dec/2020 18:37:15] "GET /static/admin/css/fonts.css HTTP/1.1" 304 0
[20/Dec/2020 18:37:16] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 304 0
[20/Dec/2020 18:37:16] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 304 0
[20/Dec/2020 18:37:16] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 304 0
Not Found: /favicon.ico
[20/Dec/2020 18:37:16] "GET /favicon.ico HTTP/1.1" 404 1977
```
> 성공후 접속한 초기페이지이다.

![1 초기웹페이지](https://user-images.githubusercontent.com/53415223/102709995-896be300-42f2-11eb-925f-e054d5a47917.png)

</br>




# 3. 기본 프레임워크를 응용하여 게시판 만들어보기
## 3.1 가상환경 세팅
```bash
$ python manage.py startapp main
```
***OSS_project/OSS_project/settings.py*** 파일의 기존 INSTALLED_APPS 구절을 다음코드로 교체 

```
# 어플리케이션에 사용할 라이브러리 정의
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

```
***OSS_project/OSS_project/main/templates/main*** 경로로 폴더를 생성해준다.

templates 폴더를 생성후 그안에 main폴더를 생성!
```
OSS_project/
    OSS_project/
        main/
            templates/            <= 생성1
                main/             <= 생성2
```

***OSS_project/OSS_project/main/views.py*** 에 다음코드를 복사
```python
from django.shortcuts import *
# View에 Model(Post 게시글) 가져오기
from .models import Post

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴 
    return render(request, 'main/blog.html', {'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        new_article=Post.objects.create(
            postname=request.POST['postname'],
            contents=request.POST['contents'],
        )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})
```

***OSS_project/OSS_project/main/urls.py*** 생성후 다음코드를 복사 붙여넣기
```python
from django.contrib import admin
from django.urls import path
# index는 대문, blog는 게시판
from main.views import index, blog, posting, new_post, remove_post



urlpatterns = [
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index이다
    path('', index, name='index'),
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('blog/', blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/', posting, name='posting'),
    # 게시글작성페이지
    path('blog/new_post/', new_post),
    # 게시글 삭제 페이지
    path('blog/<int:pk>/remove/', remove_post),
]
```


***OSS_project/urls.py*** 를 다음코드로 교체
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

***OSS_project/OSS_project/main/admin.py*** 를 다음코드로 교체
```python
from django.contrib import admin
# 게시글(Post) Model을 불러옵니다
from .models import Post

# Register your models here.
# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Post)
```

***OSS_project/OSS_project/main/models.py*** 를 다음코드로 교체
```python
from django.db import models

class Post(models.Model):
    objects = models.Manager()
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    # postname이 Post object 대신 나오기
    def __str__(self):
        return self.postname
```

***superuser(관리자계정)*** 생성하기
```
$ python3 manage.py createsuperuser
```

```
PS C:\Users\An\Desktop\Django\OSS_python_django> python manage.py createsuperuser
C:\Users\An\anaconda3\python.exe: can't open file 'manage.py': [Errno 2] No such file or directory
PS C:\Users\An\Desktop\Django\OSS_python_django> cd .\OSS_project\
PS C:\Users\An\Desktop\Django\OSS_python_django\OSS_project> python manage.py createsuperuser
Username (leave blank to use 'an'): ACH
Email address: leaping96@ajou.ac.kr
Password: 
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```


## 3.1 글 목록 페이지
***OSS_project/OSS_project/main/templates/main/blog.html***생성후 다음 코드를 복사
```html
<html>
    <head>
        <title>Blog List</title>
    </head>
    <body>
        <h1>게시판 페이지입니다</h1>
        <!-- 게시판(postlist)의 게시글(list)을 하나씩 보여줍니다 -->
        <!-- {와 %로 이루어진 구문 내부엔 파이썬이 사용됩니다 -->
        <table>
        {% for list in postlist %}
            <!-- 게시글 클릭시 세부페이지로 넘어갑니다-->
            <ul>
                <li><a href="{{list.pk}}">{{list.postname}}</a></li>
            </ul>
        {% endfor %}
        </table>
        <button><a href="new_post/">글쓰기</a></button>
    </body>
</html>
```


## 3.2 글 상세 페이지
***OSS_project/OSS_project/main/templates/main/posting.html***생성후 다음 코드를 복사
```html
<html>
    <head>
        <title>Posting!</title>
    </head>
    <body>
        <h1>게시글 개별 페이지입니다</h1>
        <p>{{post.postname}}</p>
        <p>{{post.contents}}</p>

        <a href="/blog/{{post.pk}}/remove">삭제</a>
        <a href="/blog/">목록</a>
    </body>
</html>
```


## 3.3 글쓰기 페이지
***OSS_project/OSS_project/main/templates/main/new_post.html***생성후 다음 코드를 복사
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>글쓰기 페이지</title>
</head>
<body>
    <h1>글쓰기 페이지</h1>
    <form method="POST">
        {% csrf_token %}
        제목<br>
        <input type="text" name="postname"><br>
        내용<br>
        <textarea rows="10" cols="50" name="contents"></textarea><br>
        <input type="submit" value="글쓰기">
    </form>
</body>
</html>
```

## 3.4 글삭제 페이지 
***OSS_project/OSS_project/main/templates/main/remove_post.html***생성후 다음 코드를 복사
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>글 삭제</title>
</head>
<body>
    <form method="POST">
        {% csrf_token %}
        <h3>{{ Post.postname }} - 삭제하기</h3>
        <button>삭제</button>
    </form>
</body>
</html>
```
