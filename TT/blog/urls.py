from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import post
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$',ListView.as_view(queryset = post.objects.all().order_by("-date")[:25], template_name="blog/blog.html")),
    url(r'(?P<pk>\d+)$',DetailView.as_view(model=post, template_name="blog/post.html")),
    path('index', views.index, name='index'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
]


