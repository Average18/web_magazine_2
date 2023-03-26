from django.shortcuts import render
from django.views.generic import ListView
from catalog.models import Post


class PostListView(ListView):
    model = Post

   # def get_queryset(self):
   #     return Post.objects.filter(category__title__slug=self.kwargs.get('slug'))


def index(request):
    return render(request, 'index.html')

