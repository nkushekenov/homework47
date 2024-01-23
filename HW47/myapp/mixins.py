from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class LoginRequiredMixin:
    login_url = reverse_lazy('custom_login')

    @method_decorator(login_required(login_url=login_url))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
