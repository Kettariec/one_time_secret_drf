from django.db import models
from cryptography.fernet import Fernet


"""Кастомное шифрующее текст с помощью библиотеки cryptography"""
class EncryptedTextField(models.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cipher_suite = Fernet(Fernet.generate_key())

    def to_python(self, value: str):
        if not value:
            return value
        return self.cipher_suite.decrypt(value.encode()).decode()

    def from_db_value(self, value: str, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value: str):
        if not value:
            return value
        return self.cipher_suite.encrypt(value.encode()).decode()


class Secret(models.Model):
    text = EncryptedTextField()
    code = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = 'секрет'
        verbose_name_plural = 'секреты'
