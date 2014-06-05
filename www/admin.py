from django.contrib import admin
from .models import Post, www
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','date','author','text',)
    list_filter = ('title','author','date',)
    search_fields = ('title','text','author__username',)

class SiteAdmin(admin.ModelAdmin):
    list_display = ('title','about')

admin.site.register(Post,PostAdmin)
admin.site.register(www, SiteAdmin)