from django.urls import path
from .views import NewsList, Search, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, subscribe

urlpatterns = [
    path('', NewsList.as_view()),
    path('news/', NewsList.as_view()),
    path('search/', Search.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_add'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('subscribe/<int:pk>', subscribe, name='subscribe'),
]
