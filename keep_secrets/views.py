from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from keep_secrets.models import Secret
from keep_secrets.serializers import SecretSerializer
from keep_secrets.services import generate_code
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status


class SecretCreateView(CreateAPIView):
    queryset = Secret.objects.all()
    serializer_class = SecretSerializer

    def perform_create(self, serializer):
        new_secret = serializer.save()
        new_secret.code = generate_code()
        new_secret.save()


class SecretGetView(APIView):
    def get(self, request, code):
        try:
            my_object = Secret.objects.get(code=code)
            my_object.delete()
            return Response({'Секрет': my_object.text})
        except ObjectDoesNotExist:
            return Response({'Ошибка': 'Секрет с указанным кодом не найден'},
                            status=status.HTTP_404_NOT_FOUND)
