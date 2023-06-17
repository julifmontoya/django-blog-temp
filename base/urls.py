from django.urls import path
from .views import PostList, PostUpdate, PostCreate, PostDelete, CustomLogin, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', CustomLogin.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register', Register.as_view(), name='register'),
    path("", PostList.as_view(), name='posts'),
    path('post-create/', PostCreate.as_view(), name='post-create'),
    path('post-edit/<int:pk>/', PostUpdate.as_view(), name='post-edit'),
    path('post-delete/<int:pk>/', PostDelete.as_view(), name='post-delete')
]
