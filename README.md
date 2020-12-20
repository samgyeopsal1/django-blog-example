OSS_project
=================

# 1. 장고 프레임워크를 사용해 웹페이지 만들어보기
## 1.1 장고 설치하기 
터미널창에서 파이썬 패키지 관리자인 pip를 사용하여 django 프레임워크를 설치한다. 
```bash
$ pip install django
```
</br>

## 1.2 프로젝트 생성하기
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

## 1.3 데이터베이스 생성하기
***manage.py*** 를 사용하여 데이터베이스 생성
> 완료되면 OSS_project/OSS_project 내에 db.sqlite3 파일이 생성된다.
```bash
$ cd <프로젝트명>
$ python manage.py migrate
```
</br>

## 1.4 서버 가동해보기
```bash
$ python manage.py runserver 
```
</br>





# 2. 기본 프레임워크를 응용하여 게시판 만들어보기
</br></br>
