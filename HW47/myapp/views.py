from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .mixins import LoginRequiredMixin

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('custom_login'))
        return super().dispatch(request, *args, **kwargs)