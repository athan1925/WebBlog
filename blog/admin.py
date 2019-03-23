from django.contrib import admin
from . models import Post

#modified Customized Admin Option
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "published_date","author"]
    list_display_links = ["title", "published_date"]
    list_filter = ["published_date","author"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)