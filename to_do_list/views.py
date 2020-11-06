from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView
from events.models import Event
from to_do_list.forms import ToDoForm, TaskModelForm
from to_do_list.models import Task


class ToDoView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.all().order_by('to_date', 'time').filter(if_done=False, user=request.user)
        form = ToDoForm
        return render(request, 'to_do_list.html', {"tasks": tasks, "form": form})

    def post(self, request):
        form = ToDoForm(request.POST)
        if form.is_valid() and form.cleaned_data['add_to_calendar']:
            name = form.cleaned_data['name']
            deadline = form.cleaned_data['to_date']
            time = form.cleaned_data['time']
            task = Task.objects.create(name=name, to_date=deadline, time=time, add_to_calendar=True, user=request.user)
            event = Event.objects.create(title=name, description=name, end_time=deadline,
                                         user=request.user)
        else:
            name = form.cleaned_data['name']
            deadline = form.cleaned_data['to_date']
            time = form.cleaned_data['time']
            user = form.save(commit=False)
            task = Task.objects.create(name=name, to_date=deadline, time=time, add_to_calendar=False, user=request.user)
        return redirect('todo')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'update_task.html'
    success_url = reverse_lazy('todo')



class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_message = 'Success: Task was deleted.'
    success_url = reverse_lazy('todo')


class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        if request.method == 'POST':
            name = request.POST['lname']
            mail = request.POST['lemail']
            text = request.POST['lmessage']
            subject = request.POST['lsubject']
            message = f"{name} wants a contact!\n\nMessage:\n{text} \n\nPersonal data:\nName: {name}\nE-mail address: {mail}"
            send_mail(subject, message, 'umsiziapp@gmail.com', ["umsiziapp@gmail.com"], fail_silently=False)
            return redirect('home')
