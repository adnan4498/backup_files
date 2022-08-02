from django.contrib import admin
from .models import Posts, User
from .models import Labels

# Register your models here.
admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Labels)
