from django.contrib import admin
from django.urls import path, include
import study.urls
import researcher.urls

import study

urlpatterns = [
    path('admin/', view=admin.site.urls),
    path('study', include(study.urls)),
    path('researcher', include(researcher.urls)),
]
