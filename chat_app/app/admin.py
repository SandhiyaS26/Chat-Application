from django.contrib import admin
from app.models import MyChats
# Register your models here.

@admin.register(MyChats)
class MyChatsAdmin(admin.ModelAdmin):
    list_display=('id','me','frnd','chats')
