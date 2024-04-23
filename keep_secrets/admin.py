from django.contrib import admin
from keep_secrets.models import Secret


@admin.register(Secret)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'text',)
