from django.urls import path
from .views import NewsList, Search, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, subscribe
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(NewsList.as_view())),
    path('news/', cache_page(60)(NewsList.as_view())),
    path('search/', Search.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_add'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('subscribe/<int:pk>', subscribe, name='subscribe'),
]
