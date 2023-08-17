from django.contrib import admin

from researcher.models import Researcher


class ResearcherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Researcher, ResearcherAdmin)
