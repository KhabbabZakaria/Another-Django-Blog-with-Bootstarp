from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDetailView

urlpatterns = [
    #path('', views.home, name='base-home'),
    path('', PostListView.as_view(), name = 'base-home'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'post-update'),

]