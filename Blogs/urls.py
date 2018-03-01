from django.conf.urls import url
from Blogs import views

app_name = 'blogs'

urlpatterns = [
    url(r'^createblog/',views.createBlog, name = 'createblog'),
    url(r'^editblog/(?P<title>[a-zA-Z\s!-~]+)/',views.editBlog, name = 'editblog'),
    url(r'^(?P<title>[\s\S]+)/',views.viewBlog, name = 'viewBlog'),

]