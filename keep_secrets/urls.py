from django.urls import path
from keep_secrets.apps import KeepSecretsConfig
from keep_secrets.views import SecretCreateView, SecretGetView

app_name = KeepSecretsConfig.name


urlpatterns = [
    path('create/', SecretCreateView.as_view(), name='secret_create'),
    path('check/<str:code>/', SecretGetView.as_view(), name='secret_check'),
]
