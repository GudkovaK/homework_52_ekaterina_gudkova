from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task
from webapp.forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'webapp/task_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'webapp/task_detail.html', {'task': task})


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(
                description=form.cleaned_data['description'],
                detailed_description=form.cleaned_data['detailed_description'],
                status=form.cleaned_data['status'],
                due_date=form.cleaned_data['due_date']
            )
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'webapp/task_add.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.detailed_description = form.cleaned_data['detailed_description']
            task.status = form.cleaned_data['status']
            task.due_date = form.cleaned_data['due_date']
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(initial={
            'description': task.description,
            'detailed_description': task.detailed_description,
            'status': task.status,
            'due_date': task.due_date
        })
    return render(request, 'webapp/task_edit.html', {'form': form, 'task': task})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'webapp/task_delete.html', {'task': task})