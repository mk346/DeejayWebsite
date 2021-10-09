from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import FilesAdmin, Item, Popular,Contact,Bookings,Updates,Details


# Register your models here.
admin.site.register(Item)
admin.site.register(Popular)
admin.site.register(Contact)
admin.site.register(Bookings)
admin.site.register(Updates)
admin.site.register(Details)
@admin.register(FilesAdmin)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

class myAdmin(admin.ModelAdmin):
	list_display = ('title',)
	ordering = ('added_date',)
	search_fields = ('genre','title',)
	list_filter = ('genre',)
