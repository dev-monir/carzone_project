from django.urls import path
from .views import BlogListView, CreateBlogPostView, BlogDetailView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create-blog/', CreateBlogPostView.as_view(), name='blog_create'),
    path('blog/<pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog-update/<pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog-delete/<pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
