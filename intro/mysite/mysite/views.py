from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.db.models import F


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'
