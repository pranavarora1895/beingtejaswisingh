from django.shortcuts import get_object_or_404, render
from .models import Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from contactme.models import MyInfo
from django.db.models import Q
import random
from comments.models import Comment
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

def post(request, id):
    single_post = get_object_or_404(Post, pk=id)
    category_search = Post.objects.values_list('category', flat=True).distinct()
    all_posts = Post.objects.all()
    all_posts = all_posts.exclude(title=single_post.title)
    all_posts = list(all_posts)
    all_posts = random.sample(all_posts,3)

    # Comments
    post_comments = Comment.objects.filter(post_title=single_post).filter(is_postable=True)
    
    data = {
        'post': single_post,
        'category_search': category_search,
        'all_posts': all_posts,
        'comments': post_comments,
    }

    return render(request, 'webpages/post.html', data)

def categorysearch(request, cat):

    posts = Post.objects.order_by('-created_date')
    posts = posts.filter(category__iexact=cat)
    data ={
        'posts': posts,
    }
    return render(request, 'webpages/categorysearch.html', data)


def contact(request):
    info = MyInfo.objects.order_by("-created_date").first()

    data = {
        'contact_page': "active",
        'myinfo': info,
    }
    return render(request, 'webpages/contact.html', data)

def search(request):

    posts = Post.objects.order_by("-created_date")

    if 'query' in request.GET:
        query = request.GET['query']
        if query:
            posts = posts.filter(Q(content__icontains=query) | Q(title__icontains=query) | Q(summary__icontains=query) | Q(category__icontains=query) | Q(author__icontains=query))


    data = {
        'home_page': "active",
        'posts': posts,
    }

    return render(request, 'webpages/search.html', data)