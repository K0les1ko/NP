from django.contrib import admin
from .models import Post
from .models import Comment
from .models import Category
from .models import PostCategory
from .models import Author


admin.site.register(Post)

admin.site.register(PostCategory)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Category)

# Register your models here.
