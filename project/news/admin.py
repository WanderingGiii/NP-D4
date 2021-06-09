from django.contrib import admin
from .models import Post, Cathegory, PostCathegory, Comment, Author

admin.site.register(Post)
admin.site.register(Cathegory)
admin.site.register(PostCathegory)
admin.site.register(Comment)
admin.site.register(Author)



# Register your models here.
