from django.shortcuts import render
from .models import Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def home(request):
    posts = Post.objects.order_by("-created_date")

    p = Paginator(posts, 4)

    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    data = {
        'home_page': "active",
        'home_posts': posts,
        'page_obj': page_obj,
        'no_of_pages': p.page_range,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    data = {'about_us_page': "active"}
    return render(request, 'webpages/about.html', data)

def post(request):
    return render(request, 'webpages/post.html')

def contact(request):
    data = {'contact_page': "active"}
    return render(request, 'webpages/contact.html', data)
