from bootstrap_modal_forms.generic import BSModalUpdateView, BSModalCreateView, BSModalDeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from events.models import Event
from to_do_list.forms import ToDoForm, TaskModelForm
from to_do_list.models import Task


class ToDoView(View):
    def get(self, request):
        tasks = Task.objects.all().order_by('to_date', 'time').filter(if_done=False)
        form = ToDoForm
        return render(request, 'to_do_list.html', {"tasks": tasks, "form": form})

    def post(self, request):
        form = ToDoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            deadline = form.cleaned_data['to_date']
            time = form.cleaned_data['time']
            task = Task.objects.create(name=name, to_date=deadline, time=time)
            event = Event.objects.create(title=name, description=name, start_time=deadline, end_time=deadline)
            return redirect('todo')

class TaskUpdateView(BSModalUpdateView):
    model = Task
    template_name = 'update_task.html'
    form_class = TaskModelForm
    success_message = 'Success: Task was updated.'
    success_url = reverse_lazy('todo')


class TaskDeleteView(BSModalDeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_message = 'Success: Task was deleted.'
    success_url = reverse_lazy('todo')


