from django.contrib import admin
from blogging.models import Post, Category


# InlineModelAdmin for Categories on the Post admin view
class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    extra = 1
    verbose_name = "Category"
    verbose_name_plural = "Categories"


# Customized ModelAdmin for Post
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, ]


# Customized ModelAdmin for Category
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
    list_display = ('name', 'description',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
