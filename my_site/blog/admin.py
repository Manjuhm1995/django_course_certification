from django.contrib import admin

# Register your models here.
from .models import Author,Tag,Post
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug":("title",)}
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
admin.site.register(Author)
