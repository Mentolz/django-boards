from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.BoardListView.as_view(), name='index'),
    path('boards/<int:pk>/', views.TopicListView.as_view(), name='topic'),
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('boards/<pk>/topics/<topic_pk>/', views.PostListView.as_view(), name='topic_posts'),
    path('boards/<pk>/topics/<topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('boards/<pk>/topics/<topic_pk>)/posts/<post_pk>)/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    path('settings/account/', views.UserUpdateView.as_view(), name='my_account'),
]
