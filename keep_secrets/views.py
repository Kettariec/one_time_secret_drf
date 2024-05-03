from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from keep_secrets.models import Secret
from keep_secrets.serializers import SecretSerializer
from keep_secrets.services import generate_code
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import timedelta


class SecretCreateView(CreateAPIView):
    queryset = Secret.objects.all()
    serializer_class = SecretSerializer

    def perform_create(self, serializer):
        new_secret = serializer.save()
        new_secret.code = generate_code()
        days = timedelta(days=new_secret.days)
        new_secret.time = new_secret.time + days
        new_secret.save()


class SecretGetView(APIView):
    queryset = Secret.objects.all()
    serializer_class = SecretSerializer

    def get(self, request, code: str):
        my_object = get_object_or_404(Secret, code=code)
        my_object.delete()
        return Response({'Secret': my_object.text})
