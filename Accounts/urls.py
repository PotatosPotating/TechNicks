from django.conf.urls import url
from django.contrib.auth import views as auth_views
from Accounts import views

app_name = 'accounts'

urlpatterns = [
    url(r'^register/$', views.signup, name="register"),
    url(r'^login/$', auth_views.login, {"template_name":"Accounts/login.html"}, name='login'),
    url(r'^logout/$', auth_views.logout, {"next_page":"/"},  name='logout'),
]