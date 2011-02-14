from django.contrib import admin
from blog.models import Post, Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    exclude = ('about_html', 'content_html')
    filter_horizontal = ('tags',)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
