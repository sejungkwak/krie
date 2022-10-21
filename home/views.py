from django.views.generic.list import ListView
from django.db.models import Q
from posts.models import Post


class SearchView(ListView):
    """
    Search view for showing a list of the search results.
    """
    model = Post
    template_name = 'home/search_results.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(
                Q(title__icontains=q) | Q(body__icontains=q)).order_by(
                'title', '-created_on').distinct('title')
        return q

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
