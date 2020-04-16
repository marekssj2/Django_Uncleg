from django.shortcuts import render
from django.views import generic
from post.models import Post

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'uncleg/index.html'
    context_object_name = 'all_post'

    def get_queryset(self):
        return Post.objects.all()