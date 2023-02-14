from django.views.generic import ListView, DetailView
from .models import News


from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import News


class NewsList(ListView):
    model = News
    ordering = 'name'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Приятного чтения!"
        return context


class NewDetail(DetailView):

    model = News
    ordering = '-name'
    template_name = 'new.html'
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Приятного чтения!"
        return context
