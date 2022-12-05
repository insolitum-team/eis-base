from django.views.generic import ListView

from eis.utils import DataMixin
from eis.models import Article


class IndexView(DataMixin, ListView):
    model = Article
    template_name = "eis/index.html"
    context_object_name = "articles"

    def get_context_data(self, *, object_list=None, **kwargs):
        pass

    def get_queryset(self):
        return Article.objects.all()[:2]
