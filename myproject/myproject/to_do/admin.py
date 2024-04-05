from django.contrib import admin

from .models import to_do_item


class ToDoItemAdmin(admin.ModelAdmin):
    list_display = [
        "to_do_name",
        "who_added",
        "who_assigned",
        "add_date",
        "due_date",
        "completed",
    ]
    search_fields = ["to_do_name", "who_added", "who_assigned"]
    list_filter = ["completed"]


# Register your models here.
admin.site.register(to_do_item, ToDoItemAdmin)
