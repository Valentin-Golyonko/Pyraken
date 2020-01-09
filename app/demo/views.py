from demo.backend_simulation import check_celery_tasks
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class DemoPageView(TemplateView):
    template_name = 'demo/demo_page.html'

    def get(self, request, *args, **kwargs):
        response = {}
        return render(request=request, template_name=self.template_name, context=response)

    def post(self):
        pass


class CheckCeleryAjax(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            ajax_data = int(request.GET['input_data_1']), int(request.GET['input_data_2'])
            response = check_celery_tasks(ajax_data)
        except Exception as ex:
            print('Exception in CheckCeleryAjax\n%s' % ex)
        else:
            return HttpResponse(response)

        return HttpResponse(None)
