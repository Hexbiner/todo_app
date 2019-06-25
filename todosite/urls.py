from django.contrib import admin
from django.urls import path, include
from todo.views import index, archive
from todo import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index, name="TodoList"),
    url(r'^archive/', archive, name="ArchiveList"),
]


#url(r'^accounts/', include('allauth.urls')),
