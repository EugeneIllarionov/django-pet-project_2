from django.contrib import admin
from news.models import *
# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(PostUserLike)
