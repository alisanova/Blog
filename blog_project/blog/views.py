from django.shortcuts import render
from .models import Post, Category

def post_list(request):
    category_list = Category.objects.all()
    search_query = request.GET.get("search", None)
    if search_query:
        post_list = Post.objects.filter(title__icontains=search_query)
    else:
        post_list = Post.objects.all()
    return render(request, "blog/post_list.html", context={
        "post_list": post_list,
        "category_list": category_list
        })


def post_detail(request, pk):
    category_list = Category.objects.all()
    post = Post.objects.get(pk=pk)
    category_list = Category.objects.all()
    return render(request, "blog/post_detail.html", context={
        "post": post,
        "category_list": category_list,
    })



def category_detail(request, pk):
    category_list = Category.objects.all()
    category = Category.objects.get(pk=pk)
    return render(request, "blog/category_detail.html", context={
        "category": category,
        "category_list": category_list,
    })