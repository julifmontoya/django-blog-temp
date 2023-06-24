from django.urls import path
from .views import CatListView, AddCommentView, PostList, PostDetail, PostListProvider, PostUpdate, PostCreate, PostDelete, CustomLogin, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', CustomLogin.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register', Register.as_view(), name='register'),
    path('', PostList.as_view(), name='posts-list'),
    path('post-detail/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('post-detail/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('provider/post-list', PostListProvider.as_view(), name='posts'),
    path('provider/post-create/', PostCreate.as_view(), name='post-create'),
    path('provider/post-edit/<int:pk>/', PostUpdate.as_view(), name='post-edit'),
    path('provider/post-delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
    path('category/<category>/', CatListView.as_view(), name='category')
]
