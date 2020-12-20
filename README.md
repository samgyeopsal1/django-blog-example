OSS_project
=================
# 1. 장고 프레임워크의 개념 알기!

<iframe width="640" height="360" src="https://www.youtube.com/embed/kTcRRaXV-fg?ecver=1"  
 frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>  

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
</br></br>
