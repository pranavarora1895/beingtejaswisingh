from django.contrib import admin
from .models import Contact, MyInfo, About
# Register your models here.

class ContactDisplay(admin.ModelAdmin):

    list_display = ('id', 'name', 'email', 'subject', 'created_date',)
    search_fields = ('name', 'email',)
    list_display_links = ('id', 'name', 'email',)


admin.site.register(Contact, ContactDisplay)
admin.site.register(MyInfo)
admin.site.register(About)