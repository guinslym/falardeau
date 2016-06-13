from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.utils import timezone

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

from .models import Film

class MoviesListView(ListView):

    model = Film
    template_name = "movies_list.html"
    ordering = '-created'
    paginate_by=3

    def get_context_data(self, **kwargs):
        context = super(MoviesListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
