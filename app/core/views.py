from time import sleep

from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from app.core.draw_flag_scripts.flag import Flag3
from app.core.serializers import DrawFlagSerializer
from app.core.tasks import shared_task_draw_flag
from app.core.web_sockets.send_massage import SendMassageWS


class DrawFlagAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'flag.html'

    @classmethod
    def get(cls, request, *args, **kwargs):
        return Response(data={'serializer': DrawFlagSerializer()}, status=status.HTTP_200_OK)

    @classmethod
    def post(cls, request, *args, **kwargs):
        SendMassageWS.send_ws_msg(
            chat_name='lobby',
            title='hello',
            msg='world'
        )
        sleep(.5)
        serializer = DrawFlagSerializer(data=request.data)

        if not serializer.is_valid():
            out_data = {
                'serializer': DrawFlagSerializer(),
                'errors': [
                    *serializer.errors.get('non_field_errors', []),
                    *serializer.errors.get('even_number', [])
                ]
            }
            return Response(data=out_data, status=status.HTTP_400_BAD_REQUEST)

        if not (flag_obj := Flag3.get_flag_object()):
            out_data = {
                'serializer': DrawFlagSerializer(),
                'errors': ["Check your data base - you do not have flag object!"]
            }
            return Response(data=out_data, status=status.HTTP_400_BAD_REQUEST)

        """ normal way """
        # out_data = {
        #     'serializer': DrawFlagSerializer(),
        #     'flag': Flag3(
        #         number=serializer.validated_data.get('even_number'),
        #         flag_obj_id=flag_obj.id
        #     ).print_flag()
        # }

        """ celery """
        celery_result = shared_task_draw_flag.delay(
            even_number=serializer.validated_data.get('even_number'),
            flag_obj_id=flag_obj.id
        )
        out_data = {
            'serializer': DrawFlagSerializer(),
            'flag': celery_result.get()
        }

        return Response(data=out_data, status=status.HTTP_200_OK)
