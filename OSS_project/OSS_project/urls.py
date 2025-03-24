from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def catalog_view(request):
    return HttpResponse("이건 catalog 페이지입니다!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('catalog/', catalog_view),
]
