from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
#from .forms import UserCreateForm
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from .models import TodoList, Category, ArchiveList
from datetime import datetime as dt
from django.template import RequestContext

def archive(request):
    return render(request, "archive.html")

def index(request):
    todos = TodoList.objects.all()
    archives = ArchiveList.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":
        if "categ" in request.POST:
            catname = str(request.POST.get('categ'))
            Cat = Category(name=catname)
            Cat.save()
            return redirect("/")

    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + " -- " + date + " " + category
            try:
                Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
                Todo.save()

                ArchiveTodo = ArchiveList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
                ArchiveTodo.save()
            except:
                return redirect("/")
            return redirect("/")

        if "taskDelete" in request.POST:
            try:
                checkedlist = request.POST["checkedbox"]
                for todo_id in checkedlist:
                    todo = TodoList.objects.get(id=int(todo_id))
                    todo.delete()

                    archivetodo = ArchiveList.objects.get(id=int(todo_id))
                    archivetodo.save()
                    #return render(request, "archive.html")
            except:
                return redirect("/")

    return render(request, "index.html", {"todos": todos, "categories": categories, "archives": archives})
