from django.contrib import admin
from django.urls import path, include
from todo.views import index
from todo import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', index, name="TodoList"),
]
