from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog,BlogType

def blog_list(request):
    blogs_all = Blog.objects.all()
    paginator = Paginator(blogs_all,10)
    page_num = request.GET.get('page',1)
    page_of_blogs = paginator.get_page(page_num)

    context = {}
    context['paginator'] = paginator
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blog_list.html',context)

def blog_detail(request,blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog/blog_detail.html',context)

def blog_with_type(request,blog_type_pk):
    context = {}
    Blog_Type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blogs_type'] = Blog_Type                               
    context['blogs'] = Blog.objects.filter(blog_type=Blog_Type)   
    #过滤器滤出blog_type为Blog_type的
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blog_with_type.html', context)

# 找html时会先找已知的templates文件夹的第一层目录
# 而需要的html在第二层，所以需要加一个路径