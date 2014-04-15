from django.views.generic.base import TemplateView
from apps.news.models import Entry


class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, request, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update({
            # add key-value pairs here
            'posts': (
                Entry.objects.all()
                if request.user.is_superuser else
                Entry.objects.filter(status=Entry.PUBLISHED)
            )[:10]
        })
        return context


homepage = HomePageView.as_view()
