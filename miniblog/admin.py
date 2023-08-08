from django.contrib import admin

from miniblog.models import Post


# Register your models here.
@admin.register(Post)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']
