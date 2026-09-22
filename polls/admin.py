from django.contrib import admin
from .models import Question
from .models import Question, Choice

admin.site.site_header = "Polls Administration"
admin.site.site_title = "Polls Admin Portal"
admin.site.index_title = "Welcome to the Polls Admin Portal"

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
