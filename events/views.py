import calendar
from datetime import date, timedelta
from django.shortcuts import redirect
from django.views import generic
from django.utils.safestring import mark_safe

from .forms import EventModelForm
from .models import *
from .utils import Calendar


class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        form = EventModelForm
        context['form'] = form
        return context

    def post(self, request):
        form = EventModelForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            event = Event.objects.create(title=title, description=description, start_time=start_time, end_time=end_time)
            return redirect('calendar')


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


# class EventAddView(BSModalCreateView):
# #     model = Event
# #     template_name = 'cal/create_event.html'
# #     form_class = EventModelForm
# #     success_message = 'Success: Event was created.'
# #     success_url = reverse_lazy('calendar')


# class EventUpdateView(BSModalUpdateView):
#     model = Event
#     template_name = 'update_task.html'
#     form_class = EventModelForm
#     success_message = 'Success: Event was updated.'
#     success_url = reverse_lazy('calendar')
#
#
# class EventDeleteView(BSModalDeleteView):
#     model = Event
#     template_name = 'delete_task.html'
#     success_message = 'Success: Event was deleted.'
#     success_url = reverse_lazy('calendar')
