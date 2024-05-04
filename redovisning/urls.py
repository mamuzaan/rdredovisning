from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.PostList.as_view(), name='blog'),
    path('', views.home_page, name='home_page'),
    path("contact/", views.ContactFormView.as_view(), name="contact"),
    path("success/", views.SuccessView.as_view(), name="success"),
    path('add/', views.AddView.as_view(), name='add'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
    path('category/<category>/', views.CatListView.as_view(), name='category')
]
