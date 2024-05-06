from django.views import generic

from .forms import BlogModelForm
from .models import Blog


# show list of blogs
class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog_listview.html'


# Create new blog post
class CreateBlogPostView(generic.CreateView):
    model = Blog
    form_class = BlogModelForm
    success_url = '/create-blog/'
    template_name = 'create_blog.html'


# Blog details view
class BlogDetailView(generic.DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'details.html'


# Blog update view
class BlogUpdateView(generic.UpdateView):
    model = Blog
    form_class = BlogModelForm
    template_name = 'create_blog.html'
    success_url = '/'


# Blog delete
class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = '/'
    template_name = 'common_delete.html'
