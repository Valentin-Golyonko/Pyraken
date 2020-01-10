from demo.backend_simulation import check_celery_tasks, task_for_one_cpu, task_for_four_cpus
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView


class DemoPageView(TemplateView):
    template_name = 'demo/main_page.html'

    def get(self, request, *args, **kwargs):
        response = {}
        return render(request=request, template_name=self.template_name, context=response)

    def post(self, request):
        print("DemoPageView.POST:", request.POST)
        pass


class CheckCeleryAjax(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        try:
            ajax_data = int(request.GET['input_data_1']), int(request.GET['input_data_2'])
            response = check_celery_tasks(ajax_data)
        except Exception as ex:
            print('Exception in CheckCeleryAjax\n%s' % ex)
        else:
            return Response(response)

        return Response({'error': 'Exception in request.GET'})


class OneCpuCeleryAjax(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            response = task_for_one_cpu()
        except Exception as ex:
            print('Exception in OneCpuCeleryAjax\n%s' % ex)
        else:
            return HttpResponse(response)

        return HttpResponse()


class FourCpuCeleryAjax(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            response = task_for_four_cpus()
        except Exception as ex:
            print('Exception in FourCpuCeleryAjax\n%s' % ex)
        else:
            return HttpResponse(response)

        return HttpResponse()
