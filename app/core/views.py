from time import sleep

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from app.core.draw_flag_scripts.flag import Flag3
from app.core.serializers import DrawFlagSerializer
from app.core.tasks import shared_task_draw_flag
from app.core.web_sockets.send_massage import SendMassageWS


class DrawFlagAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    template_name = 'flag.html'
    serializer_class = DrawFlagSerializer

    @staticmethod
    def get(request, *args, **kwargs):
        return Response()

    def post(self, request, *args, **kwargs):
        SendMassageWS.send_ws_msg(
            chat_name='lobby',
            title='hello',
            msg='world',
        )
        sleep(.5)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)

        if not serializer.is_valid():
            return Response(
                data={'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if (flag_obj := Flag3.get_flag_object()) is None:
            return Response(
                data={'errors': ("Check your data base - you do not have flag object!",)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        even_number = serializer.validated_data.get('number')

        """ normal way """
        # out_data = {
        #     'flag': Flag3(
        #         number=even_number,
        #         flag_obj_id=flag_obj.id
        #     ).print_flag(),
        #     'even_number': even_number,
        # }

        """ with celery """
        celery_result = shared_task_draw_flag.delay(
            even_number=even_number,
            flag_obj_id=flag_obj.id,
        )
        out_data = {
            'flag': celery_result.get(),
            'even_number': even_number,
        }

        return Response(data=out_data, status=status.HTTP_200_OK)
