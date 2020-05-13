from django.urls import path
from management import views
urlpatterns=[
	path('',views.index,name='index'),
	#path('sign_up/',views.sign_up,name='sign_up'),
	#path('login/',views.login,name='login'),
#	path('logout/'views.logout,name='logout'),
#	path('change_password/',views.change_password,name='change_password'),
	path('add_book/',views.add_book,name='add_book'),
	path('add_image/',views.add_image,name='add_image'),
	path('book_list/<str:category>/',views.book_list,name='book_list'),
	path('content/<int:book_id>/',views.content,name='content'),
	path('edit_book/<int:book_id>/',views.edit_book,name='edit_book'),
	path('delete/<int:book_id>/',views.delete,name='delete'),
]
