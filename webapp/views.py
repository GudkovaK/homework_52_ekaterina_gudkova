from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task, STATUS_CHOICES


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'webapp/task_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'webapp/task_detail.html', {'task': task})


def task_add(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        detailed_description = request.POST.get('detailed_description')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date') or None
        Task.objects.create(
            description=description,
            detailed_description=detailed_description,
            status=status,
            due_date=due_date
        )
        return redirect('task_list')
    return render(request, 'webapp/task_add.html', {'status_choices': STATUS_CHOICES})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')