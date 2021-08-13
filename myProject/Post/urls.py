from django.urls import path
from.import views

urlpatterns=[
    path("i",views.index,name="index"),
    path("reg",views.register,name="register"),
    path("logins",views.login,name="login"),
    path("logouts",views.logout,name="logout"),
    path('show',views.postShow,name="postShow"),
    path('create',views.postCreate,name="postCreate"),
    path('delete/<int:id>',views.destroy),
    path('edit/<int:id>',views.update),


]