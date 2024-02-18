from django.urls import path, include

from . import views

urlpatterns=[
    path('',views.index,name='starting_page'),
    path('posts',views.posts,name='post_page'),
    path('posts/<slug:slug>',views.single_post,name='page_detail'),
    path('Product',views.product_list),
    path('<slug:slug>',views.product_detail),


]