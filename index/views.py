from django.views.generic import TemplateView

from writers.models import WritersProfile


class IndexView(TemplateView):
    template_name = 'index.html'
    model = WritersProfile


