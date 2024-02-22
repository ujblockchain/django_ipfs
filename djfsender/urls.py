from django.urls import path
from .views import HomeView, FileDetails


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('file/<str:file_id>/details/', FileDetails.as_view(), name='file_details'),
]
