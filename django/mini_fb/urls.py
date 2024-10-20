## mini_fb/urls.py
## description: the app-specific URLs for the mini_fb app

from django.urls import path
from . import views

# create a list of URLs for the mini_fb app
urlpatterns = [
    path(r'', views.ShowAllProfilesView.as_view(), name='show_all_profiles'), # the first URL. main page
    path(r'profile/<int:pk>', views.ShowProfilePageView.as_view(), name='show_profile'), # new show_profile path with pk
    path(r'create_profile', views.CreateProfileView.as_view(), name='create_profile'),
    path(r'profile/<int:pk>/create_status', views.CreateStatusMessageView.as_view(), name='create_status'),
    path(r'profile/<int:pk>/update', views.UpdateProfileView.as_view(), name='update_profile'), # new update_profile path
    path(r'status/<int:pk>/delete', views.DeleteStatusMessageView.as_view(), name='delete_status'),
]