
from atexit import register
from django.contrib import admin
from .models import *

# Register your models here.

action = ["export_as_csv"]
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ('title','slug','author','publish','status')
    ordering=['-created']
    list_filter=('status','created','publish','author')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',),'tags':('title',)}
    list_per_page = 10
    raw_id_fields=('author',)
    date_hierarchy= 'publish'
    ordering= ('status', 'publish')
    

def export_as_csv(self, request, queryset):
    pass
export_as_csv.short_description= "Export Selected"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display= ('name', 'email','post','created', 'active')

    list_filter= ('active', 'created', 'updated')
    search_fields =('name', 'email','body')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

