from django.urls import path
from . import views
from .views import Blog, PostDetail, AddPostView,UpdatePostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('image_civil_engineering/', views.image_civil_engineering, name='image_civil_engineering'),
    path('mambwe_chafs_portfolio/', views.mambwe_chafs_portfolio, name='mambwe_chafs_portfolio'),
    path('python_password_checker/', views.python_password_checker, name='python_password_checker'),
    path('python_web_scraper/', views.python_web_scraper, name='python_web_scraper'),
    path('python_email_sender/', views.python_email_sender, name='python_email_sender'),
    path('eco_first_innovations/', views.eco_first_innovations, name='eco_first_innovations'),
    path('contact/', views.contact, name='contact'),
    path('essential_elements/', views.essential_elements, name='essential_elements'),
    path('blog/', Blog.as_view(), name='blog_home'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView.as_view(), name='category'),
    path('<slug:slug>/update/', UpdatePostView.as_view(), name='update'),
    path('<slug:slug>/remove/', DeletePostView.as_view(), name='delete'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    ]