from rest_framework import serializers
from keep_secrets.models import Secret


class SecretSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secret
        fields = '__all__'
