from django.urls import path
from books_authors_app import views

urlpatterns = [
    path('', views.root, name="root"),
    path('create_book/', views.create_book, name="create_book"),
    path('books/<int:id>/', views.view_book, name="view_book"),
    path('update_book_authors', views.update_book_authors, name="update_book_authors"),
    path('author', views.author, name="author"),
    path('create_author', views.create_author, name="create_author"),
    path('authors/<int:id>/', views.view_author, name="view_author"),
    path('update_author_books', views.update_author_books, name="update_author_books")
]