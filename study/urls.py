from django.urls import path
from . import views

urlpatterns = [
    path('<int:study_id>/', views.study),
    path('<int:study_id>/signup/',
         views.signup, name='signup'),
]
