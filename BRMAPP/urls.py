from BRMAPP import views
from django.urls import re_path
urlpatterns = [
    re_path('view-books',views.viewBook),
    re_path('edit-book',views.editBook),
    re_path('delete-book',views.deleteBook),
    re_path('search-book',views.searchBook),
    re_path('new-book',views.newBook),
    re_path(r'^add',views.add), #regular expression(starts with add)
    re_path('edit',views.edit),
    re_path('search',views.search),
    re_path('login',views.userLogin),
    re_path('logout',views.userLogout),
]
    