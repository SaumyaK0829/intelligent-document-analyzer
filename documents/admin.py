from django.contrib import admin
from .models import Document, Entity

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'status', 'uploaded_at']
    list_filter = ['status']

@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ['text', 'label', 'document']