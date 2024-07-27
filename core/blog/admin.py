from django.contrib import admin
from .models import Post,Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_date','status')

admin.site.register(Post,PostAdmin)
admin.site.register(Category)