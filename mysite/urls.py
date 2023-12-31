from django.urls import path
from . import views
from .feeds import LatestPostsFeed


app_name = 'mysite'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('projects/', views.all_projects, name='all_projects'),
    path('projects/<slug:project_slug>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('about/', views.about, name='about'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/',
         views.post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
