from django.views import generic
# from .forms import Form

class IndexView(generic.TemplateView):
    template_name = "index.html"

# class RecordListView(generic.ListView):
