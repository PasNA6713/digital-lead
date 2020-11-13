from django.contrib import admin

from .models import UserIdentifierModel, MessageModel


admin.site.register(UserIdentifierModel)
admin.site.register(MessageModel)
