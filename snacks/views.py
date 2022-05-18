from django.views.generic import (ListView,
                                DetailView,
                                TemplateView,
                                DeleteView,
                                CreateView,
                                UpdateView)
from .models import snack

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

class SnackListView(ListView):
    template_name = 'snacks_list.html'
    model = snack
    context_object_name = 'snacks_list'

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = snack

class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = snack
    fields = ["title","purshaser","description",]

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = snack
    fields = ["title","description",]

class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = snack
    success_url = '/'