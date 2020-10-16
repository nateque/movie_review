from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)

admin.site.site_header = "Movie Review Admin"
admin.site.site_title = "Welcome to Movie Review Admin"
admin.site.index_title = "Admin"