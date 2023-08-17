from django.contrib import admin

from study.models import Study


class StudyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Study, StudyAdmin)
