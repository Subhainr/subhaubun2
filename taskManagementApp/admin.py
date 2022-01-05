from django.contrib import admin

from . models import TaskDb
from . modelsML import TaskML

admin.site.register(TaskDb)
admin.site.register(TaskML)
