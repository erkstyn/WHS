from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update({
            # add key-value pairs here
        })
        
        return context

homepage = HomePageView.as_view()

