from django.views import generic
import logging
from django.urls import reverse_lazy
# from .forms import InquiryForm, DiaryCreateForm
logger = logging.getLogger(__name__)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from . models import Diary
from django.shortcuts import get_object_or_404
class IndexView(generic.TemplateView):
    template_name = "index.html"

# class RecordListView(generic.ListView):
