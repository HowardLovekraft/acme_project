from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import UserCreationForm


class MyUserCreateView(CreateView):
    template_name = 'registration/registration_form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('page:homepage')