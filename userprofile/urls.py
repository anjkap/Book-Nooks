from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('addbooks/', views.addbooks, name='add-books'),
    path('bookprofile/<book_id>', views.bookprofile, name='book-profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search_books',views.search_books, name='search-books'),
    path('list_books',views.list_books, name='list-books'),
]