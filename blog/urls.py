from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('home/<item>/<item2>', views.home, name='homepage'),
    path('search/', views.post_search, name='post_search'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
]
