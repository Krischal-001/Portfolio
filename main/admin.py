from django.contrib import admin


from .models import Contact
from .models import About

admin.site.register(Contact)
admin.site.register(About)