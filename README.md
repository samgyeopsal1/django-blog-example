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
## 3.1 어플리케이션 생성
OSS_project/OSS_project 내의 파일들은 전체어플리케이션을 통제하는 장고 프레임워크의 기본 모듈이다.

우리는 우리만의 ***비즈니스로직*** 을 정의하기 위해서 startapp 명령어로 어플 폴더를 따로 정의해주어야 한다. 
```bash
$ python manage.py startapp main
```

어플리케이션 생성후 우리의 어플리케이션을 프레임워크가 인지할 수 있도록 다음 코드를 작성하자

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

이제 프레임워크가 우리의 어플리케이션을 인지했다.

따라서 어플리케이션 차원에서 URL 요청을 받고 MVT 패턴에 의해 페이지를 생성하게끔 작동방식을 변경해주어야 한다.

이는 프레임워크의 urls.py와 어플리케이션의 urls.py를 연동하는것으로 가능하다.

***OSS_project/urls.py*** 를 다음코드로 교체
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

또한 어플리케이션이 URL에 대한 라우팅을 할 수 있도록 정의가 필요하다.

우리는 다음과같이 페이지 URL을 정의하겠다.

1) 게시글 목록 => 127.0.0.1:8000/blog
2) 게시글 상세 => 127.0.0.1:8000/blog/숫자
3) 게시글 생성 => 127.0.0.1:8000/new_post
4) 게시글 삭제 => 127.0.0.1:8000/remove_post

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
    # URL:8000/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('blog/', blog, name='blog'),
    # URL:8000/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/', posting, name='posting'),
    # 게시글작성페이지
    path('blog/new_post/', new_post),
    # 게시글 삭제 페이지
    path('blog/<int:pk>/remove/', remove_post),
]
```
## 3.2 어플리케이션 Model 정의
어플리케이션 생성을 마쳤으니 이제 MVT 패턴의 첫번째인 Model을 정의해주어야 한다.

어플리케이션 폴더 내의 model.py 를 작성하는것으로 완료된다.

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

장고는 데이터의 생성과 수정, 삭제를 직접 정의해주지 않아도 가능하게끔 하는 admin 모듈이 있다.

해당 페이지에서도 글의 수정과 삭제를 가능하게 권한을 허용해주는 절차는 다음 코드로 가능하다.

***OSS_project/OSS_project/main/admin.py*** 를 다음코드로 교체
```python
from django.contrib import admin
# 게시글(Post) Model을 불러옵니다
from .models import Post

# Register your models here.
# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Post)
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
위와 같이 Username, Password, email 등을 입력하면 관리자계정의 생성과 데이터접근허용이 완료된다. 

장고에서 지원하는 관리자페이지는 프레임워크 구성을 마친 후 예시 이미지로 다시 설명하겠다.

## 3.3 어플리케이션 View 정의 

Model을 정의해 주었으니 이제 MVT패턴에서 가장 중추역할을 하는 view.py 코드를 작성하자

view.py 는 urls.py에게 http 요청을 받고 model.py와 template를 사용하여 적절한 페이지를 반환한다.

***OSS_project/OSS_project/main/views.py*** 에 다음코드를 복사
```python
from django.shortcuts import *
# View에 Model(Post 게시글) 가져오기
from .models import Post

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

## 3.4 어플리케이션 Template 정의

MVT 패턴중 마지막인 Template의 정의만 남았다.

Template은 기본적으로 html파일로 정의되며 어플리케이션 폴더에 별도의 templates/main 폴더를
생성하여 만들어준다.

***OSS_project/OSS_project/main/templates/main*** 경로로 폴더를 생성해준다.

templates 폴더를 생성후 그안에 main폴더를 생성!
```
OSS_project/
    OSS_project/
        main/
            templates/            <= 생성1
                main/             <= 생성2
```

## 3.4.1 게시글 목록 페이지
전체 게시글의 목록을 표시해주는 페이지이다. 위에서 정의해놓은 Model 덕분에 각 템플릿을
컴팩트하게 정의할 수 있다. 

또한 동적인 페이지의 구현을 위해 파이썬을 html 내부에서 사용하게 된다.

다음 게시글 목록에서는 list.pk 구문이 각 게시글 상세페이지의 링크를 동적으로 표시해주고,
list.postname 부분이 각 게시글의 이름을 표시하게 된다.

코드를 보면 for문을 통해 모든 게시글들에 대해 차례로 표시되도록 동작하는것을 알 수 있다.

***OSS_project/OSS_project/main/templates/main/blog.html*** 생성후 다음 코드를 복사
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
글 상세 페이지에서는 URL을 통해 받은 게시글 한개에 대하여 글 제목과 내용을 차례로 표시한다.

모델에서 정의해준 postname과 contents를 한 차례만 불러오는것으로 페이지가 완성된다.

***OSS_project/OSS_project/main/templates/main/posting.html*** 생성후 다음 코드를 복사
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


## 3.3 게시글생성 페이지

글쓰기 페이지도 상세 페이지와 반대로 postname과 contents에 대한 1번의 세이브처리이다.

html의 자세한 문법에 대한 설명은 생략하겠지만 form 태그의 Post 방식을 통해 데이터베이스에
저장한다고만 알아두자


***OSS_project/OSS_project/main/templates/main/new_post.html*** 생성후 다음 코드를 복사
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

## 3.4 게시글 삭제 페이지 

마지막 페이지인 게시글 삭제페이지이다. 

게시글 삭제 페이지에서 삭제 버튼을 누를 경우 해당 게시글에 해당하는 정보를 URL로 보내어
삭제페이지로 이동하게 된다.

삭제페이지에서 해당 게시글의 제목을 표시한 후, 한 번 더 삭제 버튼을 누를경우 데이터베이스에서 삭제하도록 되어있다.

***OSS_project/OSS_project/main/templates/main/remove_post.html*** 생성후 다음 코드를 복사
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
# 4. 전체 시연 영상
[![프로젝트시연](http://img.youtube.com/vi/rktyUUtjy38/maxresdefault.jpg)](https://youtu.be/rktyUUtjy38?t=0s) 