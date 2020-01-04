from django.urls import path
from . import views

urlpatterns=[
				path('',views.index,name='index'),
				path('signup/',views.signup,name='signup'),
				path('login/',views.login_view,name='login'),
				path('signout/',views.logout_view,name='logout'),
				path('create_post/',views.create_post,name='create_post'),
				path('home/',views.home,name='home'),
				path('home/<key>/confirm_delete',views.confirm_delete,name='post-confirm-delete'),
				path('home/<key>/confirm_delete/deleted',views.delete_post,name='post-delete'),
				path('home/<key>/',views.view_post,name='post-detail'),
				path('home/<key>/update',views.update_post,name='post-update'),
				path('home/<key>/create_comment',views.create_comment,name='create-comment'),
				path('home/<key>/like_api/', views.LikePostAPI, name='post_like_api'),
				path('home/<key>/like_post', views.like_post, name='like-post'),
			]