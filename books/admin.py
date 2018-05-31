from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Category,Book,Comment,Rate

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_per_page = 5
    pass

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_filter = ('author','timestamp','category')
    list_display = ('title','author','release_date','description')
    list_display_links = ('title',)
    pass

admin.site.register(Comment)
admin.site.register(Rate)

