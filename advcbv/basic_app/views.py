from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from basic_app import models

class SchoolList(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'