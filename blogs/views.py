from django.db.models import Avg,Max,Min
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Product

# Create your views here.
all_posts = [
    {'slug': 'Python-Programming',
     'title': 'Python',
     'author': 'Isavandi',
     'image': 'python.png',
     'date': date(2019, 2, 10),
     'short_description': 'Python is Open Source.',
     'content': """
     Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming.
     """},

    {'slug': 'Django-Web',
     'title': 'Django',
     'author': 'Tehrani',
     'image': 'Django.png',
     'date': date(2020, 10, 10),
     'short_description': 'Django is Web',
     'content': """
     Django is a free and open-source, Python-based web framework that follows the model–template–views architectural pattern. It is maintained by the Django Software Foundation, an independent organization established in the US as a 501 non-profit.
     """},

    {'slug': 'Java-Programming',
     'title': 'Java',
     'author': 'Ahmadi',
     'image': 'java.jpg',
     'date': date(2020, 6, 9),
     'short_description': 'Java is a Programming languages',
     'content': """
     Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.
     """}

    # {'slug':'',
    #  'title':'',
    #  'author':'',
    #  'image':'',
    #  'date':'',
    #  'short_description':'',
    #  'content':"""
    #  """},
    #
    #
    # {'slug':'',
    #  'title':'',
    #  'author':'',
    #  'image':'',
    #  'date':'',
    #  'short_description':'',
    #  'content':"""
    #  """},

]


def get_date(post):
    return post['date']


def index(request):
    # data=list(all_posts)
    # context={'a':data}
    # return render(request,'blogs/index.html',context)
    post_sorted = sorted(all_posts, key=get_date)
    latest = post_sorted[-2:]
    # context = {'latest_posts':latest}

    return render(request, 'blogs/index.html', {'latest_posts': latest})


def posts(request):
    return render(request, 'blogs/all_post.html',{'all_post':all_posts})


def single_post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, f'blogs/post_details.html', {'post': post})


def product_list(request):
    all_product = Product.objects.all().order_by('-price')
    numbers=all_product.count()
    info = all_product.aggregate(Avg('price'),Max('price'), Min('price'))
    return render(request, 'blogs/product_list.html', {'all_product':all_product,
                                                                            'numbers':numbers,
                                                                              'info':info})

def product_detail(request,slug):
    # try:
    #     pro = Product.objects.get(id = product_id)
    #     return render(request,'blogs/product_details.html',{'pro':pro})
    # except:
    #     raise Http404
    pro = get_object_or_404(Product,slug=slug)
    return render(request,'blogs/product_details.html',{'pro':pro})

