from django.views.generic import TemplateView
from django.db.models import Max
from django.contrib.auth import get_user_model
from django.shortcuts import render

from writers.models import WritersProfile, Rating, Orders



class IndexView(TemplateView):
    template_name = 'index.html'
    model = Rating


def index(request):
    rating = get_user_model().objects.all()
    return render(request, 'index.html', {'rating': rating})


