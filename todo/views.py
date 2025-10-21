from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

def task_list(request):
    tasks = Task.objects.order_by("-created_at")
    return render(request, "todo/task_list.html", {"tasks": tasks})

def task_create(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    Task.objects.create(
        title=(request.POST.get("title") or "").strip(),
        notes=(request.POST.get("notes") or "").strip(),
    )
    return redirect("task-list")

def task_update(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    task = get_object_or_404(Task, pk=pk)
    task.title = (request.POST.get("title") or task.title).strip()
    task.notes = (request.POST.get("notes") or task.notes).strip()
    task.save()
    return redirect("task-list")

def task_toggle(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect("task-list")


def task_delete(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("task-list")