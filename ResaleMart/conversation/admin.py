from django.contrib import admin

from .models import Conversation,conversationMessage
# Register your models here.
admin.site.register(Conversation)
admin.site.register(conversationMessage)
