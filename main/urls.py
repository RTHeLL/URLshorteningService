from django.urls import path

from .views import index, urls_list, redirect_original, page_not_found, do_logout
from .views import RegisterUser, LoginUser

urlpatterns = [
    path('', index, name='home'),
    path('<slug:url_slug>', redirect_original, name='redirect_original'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', do_logout, name='logout'),
    path('urls/', urls_list, name='url_list')
]


handler404 = page_not_found
