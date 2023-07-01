from django.contrib import admin  # noqa: F401
import json
from triangle.middleware import LogEntry


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('method', 'path', 'timestamp')
    readonly_fields = ('method', 'path',  'timestamp', 'request_data')
    search_fields = ('path', )
    list_filter = ('method', )

    def request_data(self, obj):
        data = obj.request_data
        return json.dumps(data, indent=4)
