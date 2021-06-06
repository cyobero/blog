from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail')
]
