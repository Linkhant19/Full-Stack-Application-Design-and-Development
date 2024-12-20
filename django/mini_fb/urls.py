## mini_fb/urls.py
## description: the app-specific URLs for the mini_fb app

from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

# create a list of URLs for the mini_fb app
urlpatterns = [
    path(r'', views.ShowAllProfilesView.as_view(), name='show_all_profiles'), # the first URL. main page
    path(r'profile/<int:pk>', views.ShowProfilePageView.as_view(), name='show_profile'), # new show_profile path with pk
    path(r'create_profile', views.CreateProfileView.as_view(), name='create_profile'),
    path(r'status/create_status', views.CreateStatusMessageView.as_view(), name='create_status'),
    path(r'profile/update', views.UpdateProfileView.as_view(), name='update_profile'), # new update_profile path
    path(r'status/<int:pk>/delete', views.DeleteStatusMessageView.as_view(), name='delete_status'), # new delete_status path
    path(r'status/<int:pk>/update', views.UpdateStatusMessageView.as_view(), name='update_status'), # new update_status path
    path(r'profile/add_friend/<int:other_pk>', views.CreateFriendView.as_view(), name='add_friend'), # new add_friend path
    path(r'profile/friend_suggestions', views.ShowFriendSuggestionsView.as_view(), name='friend_suggestions'), # new friend_suggestions path
    path(r'profile/news_feed', views.ShowNewsFeedView.as_view(), name='news_feed'), # new news_feed path

    # authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='mini_fb/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mini_fb/logged_out.html'), name='logout'),
]