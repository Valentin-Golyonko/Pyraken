from demo.backend_simulation import check_celery_tasks
from django.shortcuts import render
from django.views.generic import TemplateView


class DemoPageView(TemplateView):
    template_name = 'demo/demo_page.html'

    def get(self, request, *args, **kwargs):
        response = {'data': check_celery_tasks()}
        return render(request=request, template_name=self.template_name, context=response)

    def post(self):
        pass
