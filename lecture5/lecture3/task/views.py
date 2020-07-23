from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

task = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
    return render(request, "task/index.html", {
        "task": task
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data["task"]
            task.append(item)
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request, "task/add.html", {
                "form": form
            })

    return render(request, "task/add.html", {
        "form":NewTaskForm()
    })