from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy


from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10
    # don't need config template_name
    # cuz template name is '<app_name>/<model_name>_list.html'


class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayFormMixin:
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


class BirthdayCreateView(BirthdayMixin, BirthdayFormMixin, CreateView):
    pass

class BirthdayUpdateView(BirthdayMixin, BirthdayFormMixin, UpdateView):
    pass

class BirthdayDeleteView(BirthdayMixin, DeleteView):
    pass